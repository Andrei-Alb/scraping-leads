"""Carrega o JSON (uma linha por lugar) do gosom/google-maps-scraper num SQLite.
Uso: python3 coleta/carregar.py data/resultados.json leads.db
"""
import json
import sqlite3
import sys

SCHEMA = """
CREATE TABLE IF NOT EXISTS empresas (
  place_id TEXT PRIMARY KEY,
  nome TEXT NOT NULL,
  categoria TEXT,
  telefone TEXT,
  site TEXT,
  nota REAL,
  avaliacoes INTEGER,
  status TEXT,
  descricao TEXT,
  faixa_preco TEXT,
  link_maps TEXT,
  latitude REAL,
  longitude REAL,
  dono_nome TEXT,
  coletado_em TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS enderecos (
  place_id TEXT PRIMARY KEY REFERENCES empresas(place_id),
  completo TEXT, rua TEXT, bairro TEXT, cidade TEXT, cep TEXT, estado TEXT, pais TEXT
);
CREATE TABLE IF NOT EXISTS categorias (
  id INTEGER PRIMARY KEY,
  nome TEXT UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS empresa_categorias (
  place_id TEXT REFERENCES empresas(place_id),
  categoria_id INTEGER REFERENCES categorias(id),
  PRIMARY KEY (place_id, categoria_id)
);
CREATE TABLE IF NOT EXISTS contatos (
  place_id TEXT REFERENCES empresas(place_id),
  tipo TEXT NOT NULL CHECK (tipo IN ('telefone', 'email', 'site')),
  valor TEXT NOT NULL,
  origem TEXT NOT NULL,
  PRIMARY KEY (place_id, tipo, valor)
);
CREATE INDEX IF NOT EXISTS idx_empresas_categoria ON empresas(categoria);
CREATE INDEX IF NOT EXISTS idx_enderecos_bairro ON enderecos(bairro);
"""


def carregar(caminho_json: str, caminho_db: str) -> None:
    db = sqlite3.connect(caminho_db)
    db.executescript(SCHEMA)
    total = ignorados = 0
    with open(caminho_json, encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue
            e = json.loads(linha)
            place_id = e.get("place_id") or e.get("data_id") or e.get("cid")
            if not place_id or not e.get("title"):
                ignorados += 1
                continue
            total += 1
            db.execute(
                """INSERT INTO empresas (place_id, nome, categoria, telefone, site, nota, avaliacoes,
                   status, descricao, faixa_preco, link_maps, latitude, longitude, dono_nome)
                   VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                   ON CONFLICT(place_id) DO UPDATE SET nome=excluded.nome, categoria=excluded.categoria,
                   telefone=excluded.telefone, site=excluded.site, nota=excluded.nota,
                   avaliacoes=excluded.avaliacoes, status=excluded.status""",
                (
                    place_id, e["title"], e.get("category"), e.get("phone") or None,
                    e.get("web_site") or None, e.get("review_rating"), e.get("review_count"),
                    e.get("status"), e.get("description"), e.get("price_range"), e.get("link"),
                    e.get("latitude"), e.get("longitude", e.get("longtitude")),
                    (e.get("owner") or {}).get("name"),
                ),
            )
            end = e.get("complete_address") or {}
            db.execute(
                "INSERT OR REPLACE INTO enderecos VALUES (?,?,?,?,?,?,?,?)",
                (place_id, e.get("address"), end.get("street"), end.get("borough"), end.get("city"),
                 end.get("postal_code"), end.get("state"), end.get("country")),
            )
            for nome in e.get("categories") or []:
                db.execute("INSERT OR IGNORE INTO categorias (nome) VALUES (?)", (nome,))
                db.execute(
                    "INSERT OR IGNORE INTO empresa_categorias SELECT ?, id FROM categorias WHERE nome = ?",
                    (place_id, nome),
                )
            contatos = [("telefone", e.get("phone"), "google_maps"), ("site", e.get("web_site"), "google_maps")]
            contatos += [("email", m.lower(), "site_da_empresa") for m in e.get("emails") or []]
            for tipo, valor, origem in contatos:
                if valor:
                    db.execute("INSERT OR IGNORE INTO contatos VALUES (?,?,?,?)", (place_id, tipo, valor, origem))
    db.commit()
    print(f"{total} lugares carregados, {ignorados} ignorados sem identificador")


if __name__ == "__main__":
    carregar(sys.argv[1], sys.argv[2])
