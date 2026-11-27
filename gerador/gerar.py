#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["jinja2>=3.1", "pyyaml>=6", "questionary>=2", "rich>=13"]
# ///
"""Gerador de landing pages para os leads do leads.db.

Interativo: `uv run gerador/gerar.py`
Lote:       `uv run gerador/gerar.py --presenca sem_nada --prioridade quente --nicho alto --limite 5`
Um lead:    `uv run gerador/gerar.py --place-id <id> [--template 03]`
Repetir:    `uv run gerador/gerar.py --receita gerador/receitas/<arquivo>.yaml`
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import sqlite3
import subprocess
import sys
import time
import webbrowser
from html import escape as esc
from pathlib import Path
from string import Template
from urllib.parse import quote

import questionary as q
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup, escape
from rich.console import Console
from rich.progress import track
from rich.table import Table

RAIZ = Path(__file__).resolve().parent
BANCO = RAIZ.parent / "leads.db"
SAIDA = RAIZ / "saida"
PROMPT = RAIZ / "prompts" / "conteudo-v1.md"
# O banco não guarda horário de funcionamento; ele só existe na coleta bruta.
BRUTOS = [RAIZ.parent / "data" / "resultados.json", RAIZ.parent / "data" / "grade.json"]
DIAS = ["domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado"]


def _lum(cor: str) -> float:
    c = [int(cor[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]


def contraste(a: str, b: str) -> float:
    claro, escuro = sorted([_lum(a), _lum(b)], reverse=True)
    return (claro + .05) / (escuro + .05)


def checar_paleta(nome: str, claro: dict, escuro: dict) -> None:
    """AA (4,5:1) em todo par que vira texto sobre fundo; falha cedo, antes de gerar página ruim."""
    pares = [(claro, a, b) for a, b in [("texto", "fundo"), ("texto", "superficie"), ("suave", "fundo"),
                                       ("suave", "superficie"), ("texto", "destaque"), ("acento", "fundo"),
                                       ("acento", "superficie")]]
    pares += [(escuro, a, b) for a, b in [("texto", "fundo"), ("texto", "superficie"), ("suave", "fundo"),
                                         ("suave", "superficie"), ("acento", "fundo"), ("acento", "superficie"),
                                         ("destaque", "fundo")]]
    ruins = [f"{a}/{b} {contraste(p[a], p[b]):.2f}" for p, a, b in pares if contraste(p[a], p[b]) < 4.5]
    # Botão com texto branco sobre o acento.
    ruins += [f"branco/acento {contraste('#ffffff', claro['acento']):.2f}"] if contraste("#ffffff", claro["acento"]) < 4.5 else []
    if ruins:
        raise ValueError(f"paleta {nome} sem contraste AA: {', '.join(ruins)}")


def carregar_segmentos() -> list[dict]:
    segs = []
    for arq in sorted((RAIZ / "segmentos").glob("*.yaml")):
        s = yaml.safe_load(arq.read_text()) | {"id": arq.stem}
        for acento in s["claro"]["acentos"]:
            checar_paleta(arq.stem, s["claro"] | {"acento": acento}, s["escuro"])
        segs.append(s)
    return sorted(segs, key=lambda s: s["ordem"])


SEGMENTOS = carregar_segmentos()


def segmento_de(categoria: str) -> dict:
    cat = (categoria or "").lower()
    return next(s for s in SEGMENTOS if not s["categorias"] or re.search(s["categorias"], cat))


# Como cada template recebe a paleta: variável própria do template -> papel da paleta do segmento.
# `@titulo`/`@texto` são as fontes. Os templates escuros (04, 07) usam a paleta `escuro`.
MAPA_TEMA = {
    "01": ("claro", {"--papel": "fundo", "--tinta": "texto", "--fio": "texto", "--tinta2": "suave", "--vinho": "acento",
                     "--display": "@titulo", "--texto": "@texto"}, ""),
    "02": ("claro", {"--br": "fundo", "--pr": "texto", "--am": "destaque", "--g": "@titulo"}, ""),
    "03": ("claro", {"--papel": "fundo", "--tinta": "texto", "--cinza": "suave", "--vermelho": "acento"},
           "body{font-family:var(--seg-texto)}h1,h2,h3{font-family:var(--seg-titulo)}"),
    "04": ("escuro", {"--fundo": "fundo", "--fundo-2": "superficie", "--painel": "superficie", "--texto": "texto",
                      "--texto-2": "suave", "--ouro": "acento", "--champanhe": "destaque",
                      "--serifa": "@titulo", "--sans": "@texto"}, ""),
    "05": ("claro", {"--creme": "fundo", "--papel": "superficie", "--folha": "acento", "--tinta": "texto", "--tinta-2": "suave"},
           "body{font-family:var(--seg-texto)}h1,h2,h3,.marca,.placa,.rodape-nome{font-family:var(--seg-titulo)}"),
    "06": ("claro", {"--gelo": "fundo", "--tile": "superficie", "--tinta": "texto", "--suave": "suave", "--indigo": "acento",
                     "--lima": "destaque", "--sans": "@texto"}, ":root{--indigo-esc:color-mix(in srgb,var(--indigo) 70%,#000)}"),
    "07": ("escuro", {"--pet": "fundo", "--pet2": "superficie", "--cre": "texto", "--cre2": "suave", "--cor": "destaque",
                      "--serif": "@titulo", "--sans": "@texto"}, ""),
    "08": ("claro", {"--osso": "fundo", "--osso-2": "superficie", "--tinta": "texto", "--suave": "suave",
                     "--laranja": "destaque", "--laranja-esc": "acento", "--disp": "@titulo", "--txt": "@texto"}, ""),
}


def css_segmento(seg: dict, template: str, acento: str) -> str:
    modo, mapa, regras = MAPA_TEMA[template]
    paleta = seg[modo] | ({"acento": acento} if modo == "claro" else {})
    (ft, rt), (fx, rx) = seg["fontes"]["titulo"], seg["fontes"]["texto"]
    fontes = {"@titulo": f'"{ft}",{rt}', "@texto": f'"{fx}",{rx}'}
    decl = "".join(f"{var}:{fontes.get(papel) or paleta[papel]};" for var, papel in mapa.items())
    # Os blocos de efeito leem só --ef-*: o segmento troca a cor deles sem tocar no movimento.
    decl += "".join(f"--ef-{k}:{paleta[p]};" for k, p in
                    {"fundo": "fundo", "tinta": "texto", "acento": "acento", "destaque": "destaque", "sup": "superficie"}.items())
    familias = "&".join(f"family={f.replace(' ', '+')}:wght@400;700" for f in dict.fromkeys([ft, fx]))
    return (f'<link href="https://fonts.googleapis.com/css2?{familias}&display=swap" rel="stylesheet">'
            f'<style>:root{{{decl}--seg-titulo:{fontes["@titulo"]};--seg-texto:{fontes["@texto"]}}}{regras}</style>')


def bruto(place_id: str) -> dict:
    """A linha do lead na coleta bruta (tem o que o banco não guarda: horário, foto, avaliações escritas)."""
    for arq in BRUTOS:
        if not arq.exists():
            continue
        with arq.open() as f:
            for linha in f:
                if place_id in linha:
                    return json.loads(linha)
    return {}


def depoimentos(place_id: str) -> list[dict]:
    """Avaliações escritas reais, com nota 4+. Só o primeiro nome do autor (LGPD); texto cortado em palavra."""
    saida = []
    for a in bruto(place_id).get("user_reviews") or []:
        texto_ = " ".join((a.get("Description") or "").split())
        if not texto_ or (a.get("Rating") or 0) < 4:
            continue
        if len(texto_) > 220:
            texto_ = texto_[:220].rsplit(" ", 1)[0] + "…"
        saida.append({"nome": (a.get("Name") or "Cliente").split()[0], "nota": int(a["Rating"]), "texto": texto_})
    return saida


# Assinatura de movimento de cada template: efeitos ligados à rolagem + extras. Nenhuma combinação se repete
# (o verificador confere). Tabela em efeitos/README.md.
ASSINATURAS = {
    "01": ["revela", "zoom", "progresso", "contagem", "magnetico"],
    "02": ["horizontal", "marquee", "cor", "contagem", "magnetico"],
    "03": ["progresso", "pilha", "cor", "contagem"],
    "04": ["parallax", "revela", "contagem", "marquee"],
    "05": ["parallax", "pilha", "marquee", "magnetico"],
    "06": ["zoom", "contagem", "horizontal", "progresso"],
    "07": ["revela", "pilha", "cor", "progresso"],
    "08": ["horizontal", "parallax", "marquee", "zoom", "magnetico"],
}
EFEITOS = {
    "horizontal": "Scroll horizontal fixado com os serviços (4+ serviços)",
    "parallax": "Parallax em camadas com a foto do negócio",
    "zoom": "Foto que abre do recorte ao rolar",
    "revela": "Frase que acende palavra a palavra",
    "pilha": "Cartões empilhados com os passos",
    "progresso": "Barra de progresso de leitura",
    "contagem": "Nota e avaliações contando (só números reais)",
    "marquee": "Faixa de avaliações escritas do Google",
    "cor": "Faixa que troca de cor ao rolar",
    "magnetico": "Botões magnéticos no mouse",
}


def efeitos_possiveis(seg: dict, conteudo: dict, nota: str | None, foto: str | None, depo: list) -> set[str]:
    """O que os dados do negócio sustentam. Efeito sem dado real não entra (nada de número ou foto inventados)."""
    pode = {"revela", "progresso", "magnetico"}
    pode |= {"horizontal"} if len(conteudo["servicos"]) >= 4 else set()
    pode |= {"pilha"} if len(conteudo["passos"]) >= 3 else set()
    pode |= {"cor"} if conteudo["diferenciais"] else set()
    pode |= {"contagem"} if nota else set()
    pode |= {"parallax", "zoom"} if foto else set()
    # Advocacia: depoimento de cliente na página é captação vedada pela OAB (Provimento 205/2021).
    pode |= {"marquee"} if len(depo) >= 3 and seg["id"] != "advocacia" else set()
    return pode


def horario(place_id: str) -> list[dict] | None:
    """Lê `open_hours` do bruto. Devolve 7 dias (0 = domingo) com faixas em minutos, ou None."""
    horas = bruto(place_id).get("open_hours") or {}
    if not all(d in horas for d in DIAS):
        return None
    semana = []
    for d in DIAS:
        # Word joiner em volta do traço: a faixa "14:00–18:00" quebra entre faixas, nunca no meio.
        texto = re.sub(r"\s*[–-]\s*", "\u2060–\u2060", " ".join(horas[d]))
        faixas = [[int(a) * 60 + int(b), int(c) * 60 + int(e)]
                  for a, b, c, e in re.findall(r"(\d{1,2}):(\d{2})[\s\u2060]*[–-][\s\u2060]*(\d{1,2}):(\d{2})", texto)]
        if "24 horas" in texto.lower():
            faixas = [[0, 1440]]
        semana.append({"dia": d.split("-")[0].capitalize(), "faixas": faixas, "texto": texto})
    return semana if any(s["faixas"] for s in semana) else None


def vcard(lead: dict, nome: str, tel: str) -> str:
    linhas = ["BEGIN:VCARD", "VERSION:3.0", f"FN:{nome}", f"ORG:{nome}", f"TEL;TYPE=WORK,VOICE:+55{tel}"]
    if lead.get("endereco"):
        linhas.append(f"ADR;TYPE=WORK:;;{lead['endereco'].replace(';', ',')};;;;")
    if lead.get("site"):
        linhas.append(f"URL:{lead['site']}")
    return "\r\n".join(linhas + ["END:VCARD"]) + "\r\n"

# Quem escreve o texto. `claude` exige `claude /login`; `omp` usa o login do omp.
ESCRITORES = {
    "claude": ["claude", "-p", "--model", "{modelo}", "--output-format", "text"],
    "omp": ["omp", "-p", "--no-session", "--no-tools", "--model", "{modelo}",
            "--system-prompt", "Você é redator de landing pages. Responda só com o JSON pedido."],
}

# Ticket alto primeiro (estudo/00-sintese.md). A ordem da lista é a ordem de prioridade.
NICHOS_ALTOS = [
    ("odonto", ["%odont%", "%dentist%"]),
    ("clinica", ["%clínica%", "%médic%", "%fisioterap%", "%dermatolog%", "%oftalm%", "%ortoped%"]),
    ("construcao", ["%constru%", "%empreiteir%", "%engenh%", "%arquitet%"]),
    ("ar_condicionado", ["%ar condicionado%", "%ar-condicionado%", "%refrigera%", "%climatiza%"]),
    ("energia_solar", ["%solar%", "%fotovolt%"]),
    ("advocacia", ["%advoga%", "%jurídic%", "%advocacia%"]),
]

# Tom = como o texto é escrito (vai para o prompt). Template = o design inteiro da página.
TOM_POR_PADRAO = [
    ("clinica", r"odont|dentist|clínica|médic|fisio|dermat|oftalm|ortop|saúde|veterin|psicólog|nutri|laborat|ótica|estética"),
    ("liberal", r"advog|jurídic|contab|arquitet|imobili|consultor|despachant|seguro|cartório"),
]
# Galeria: cada número é um design completo e próprio (templates/template-NN.html.j2). Nome e direção vão para a galeria.
TEMPLATES = {
    "01": ("Revista", "Editorial de revista: capa tipográfica, colunas e fios finos"),
    "02": ("Concreto", "Brutalista: amarelo e preto, bordas grossas, sombra dura"),
    "03": ("Suíço", "Minimal suíço: grade de 12 colunas visível, vermelho e branco"),
    "04": ("Noite", "Luxo escuro: preto profundo, dourado, revelação lenta"),
    "05": ("Quintal", "Orgânico e acolhedor: verde, formas arredondadas, mola"),
    "06": ("Mosaico", "Bento moderno: o hero já é a grade de blocos"),
    "07": ("Capítulos", "Storytelling com scroll preso, palavra a palavra"),
    "08": ("Vitrine", "Vitrine com scroll horizontal e cartazes"),
}


def tom_sugerido(categoria: str) -> str:
    cat = (categoria or "").lower()
    for nome, padrao in TOM_POR_PADRAO:
        if re.search(padrao, cat):
            return nome
    return "tecnico"


def conectar() -> sqlite3.Connection:
    if not BANCO.exists():
        sys.exit(f"Banco não encontrado: {BANCO}")
    con = sqlite3.connect(BANCO)
    con.row_factory = sqlite3.Row
    return con


def listar_candidatos(con, presenca, prioridade, nicho, limite):
    """Leads com avaliações (>0), filtrados por segmento, ticket alto primeiro."""
    # Sem telefone não há botão de ligar nem WhatsApp: a página não converte.
    filtros = ["s.avaliacoes > 0", "s.telefone IS NOT NULL", "s.presenca = ?", "s.prioridade = ?"]
    params: list = [presenca, prioridade]
    ordem_casos, ordem_params = [], []
    for i, (_, padroes) in enumerate(NICHOS_ALTOS):
        ordem_casos.append(f"WHEN {' OR '.join('s.categoria LIKE ?' for _ in padroes)} THEN {i}")
        ordem_params += padroes
    ordem = f"CASE {' '.join(ordem_casos)} ELSE 99 END"
    if nicho == "alto":
        filtros.append(f"{ordem} < 99")
    elif nicho:
        padroes = dict(NICHOS_ALTOS).get(nicho, [f"%{nicho}%"])
        filtros.append("(" + " OR ".join("s.categoria LIKE ?" for _ in padroes) + ")")
        params += padroes
    sql = f"""SELECT s.place_id, s.nome, s.categoria, s.telefone, s.nota, s.avaliacoes, s.bairro
              FROM segmentos s WHERE {' AND '.join(filtros)}
              ORDER BY {ordem}, s.avaliacoes DESC LIMIT ?"""
    alto_params = ordem_params if nicho == "alto" else []
    return con.execute(sql, params + alto_params + ordem_params + [limite]).fetchall()


def carregar_lead(con, place_id: str) -> dict:
    lead = con.execute(
        """SELECT e.*, en.completo AS endereco, en.rua, en.bairro, en.cidade, en.cep
           FROM empresas e JOIN enderecos en USING (place_id) WHERE place_id = ?""",
        (place_id,),
    ).fetchone()
    if not lead:
        sys.exit(f"place_id não encontrado: {place_id}")
    dados = dict(lead)
    dados["categorias"] = [r[0] for r in con.execute(
        """SELECT c.nome FROM empresa_categorias ec JOIN categorias c ON c.id = ec.categoria_id
           WHERE ec.place_id = ?""", (place_id,))]
    return dados


def whatsapp(telefone: str | None) -> str | None:
    digitos = re.sub(r"\D", "", telefone or "")
    if len(digitos) in (10, 11):
        digitos = "55" + digitos
    # Só celular (9 dígitos após o DDD) costuma ter WhatsApp.
    return digitos if len(digitos) == 13 and digitos[4] == "9" else None


# Voz escolhida no assistente; sem escolha, vale a voz do segmento.
VOZES = {
    "formal": "Formal: trata por 'o senhor/a senhora', frases completas, sem gíria.",
    "proximo": "Próximo: trata por 'você', frases curtas, como quem conversa no balcão.",
    "tecnico": "Técnico: nomeia serviço e equipamento pelo nome certo, explica o processo sem enrolar.",
}


def montar_prompt(lead: dict, tom: str, voz: str | None = None) -> str:
    seg = segmento_de(lead["categoria"])
    return Template(PROMPT.read_text()).safe_substitute(
        nome=lead["nome"], categoria=lead["categoria"] or "",
        categorias=", ".join(lead["categorias"]) or lead["categoria"] or "",
        endereco=lead["endereco"] or "", bairro=lead["bairro"] or "",
        nota=lead["nota"] or "", avaliacoes=lead["avaliacoes"] or 0,
        descricao=lead["descricao"] or "(sem descrição)", template=tom,
        voz=VOZES.get(voz or "") or seg["voz"], secoes=", ".join(seg["secoes"]), faq="; ".join(seg["faq"]),
    )


def escrever_conteudo(lead: dict, tom: str, escritor: str, modelo: str, voz: str | None = None) -> dict:
    prompt = montar_prompt(lead, tom, voz)
    proc = subprocess.run(
        [arg.replace("{modelo}", modelo) for arg in ESCRITORES[escritor]],
        input=prompt, capture_output=True, text=True, timeout=300,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"{escritor} falhou: {(proc.stderr or proc.stdout).strip()[:400]}")
    bruto = proc.stdout.strip()
    inicio, fim = bruto.find("{"), bruto.rfind("}")
    if inicio < 0:
        raise RuntimeError(f"{escritor} não devolveu JSON: {bruto[:300]}")
    conteudo = json.loads(bruto[inicio:fim + 1])
    proibidas = re.compile(r"\b(IA|inteligência artificial|robô|algoritmo)\b", re.I)
    if proibidas.search(json.dumps(conteudo, ensure_ascii=False)):
        raise RuntimeError("texto citou IA/robô; rode de novo com --refazer-texto")
    return conteudo


def schema_org(lead: dict, conteudo: dict, tom: str) -> str:
    tipo = {"clinica": "MedicalBusiness", "liberal": "ProfessionalService"}.get(tom, "LocalBusiness")
    if re.search(r"odont|dentist", (lead["categoria"] or "").lower()):
        tipo = "Dentist"
    if re.search(r"advog|jurídic", (lead["categoria"] or "").lower()):
        tipo = "LegalService"
    dados = {
        "@context": "https://schema.org", "@type": tipo,
        "name": conteudo["nome_exibicao"], "description": conteudo["meta_description"],
        "telephone": lead["telefone"],
        "address": {"@type": "PostalAddress", "streetAddress": lead["rua"] or lead["endereco"],
                    "addressLocality": lead["cidade"] or "Santarém", "addressRegion": "PA",
                    "postalCode": lead["cep"], "addressCountry": "BR"},
        "areaServed": "Santarém - PA",
    }
    if lead["latitude"] and lead["longitude"]:
        dados["geo"] = {"@type": "GeoCoordinates", "latitude": lead["latitude"], "longitude": lead["longitude"]}
    if lead["link_maps"]:
        dados["hasMap"] = lead["link_maps"]
    if lead["nota"] and lead["avaliacoes"]:
        dados["aggregateRating"] = {"@type": "AggregateRating", "ratingValue": lead["nota"],
                                    "reviewCount": lead["avaliacoes"]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q["pergunta"],
         "acceptedAnswer": {"@type": "Answer", "text": q["resposta"]}} for q in conteudo["faq"]]}
    # `</` dentro de <script> fecharia a tag antes da hora.
    return json.dumps([dados, faq], ensure_ascii=False, indent=2).replace("</", "<\\/")


def paginas_geradas() -> list[dict]:
    return [json.loads(m.read_text()) for m in sorted(SAIDA.glob("*/meta.json"))]


def escolher(opcoes: list[str], lead: dict, tom: str, campo: str) -> str:
    """Ordem própria do lead (hash) e pula o que os 4 vizinhos mais próximos do mesmo tom já usam.

    Assim dois concorrentes do mesmo bairro nunca recebem a mesma página.
    """
    semente = hashlib.sha1(f"{campo}:{lead['place_id']}".encode()).digest()[0]
    ordem = opcoes[semente % len(opcoes):] + opcoes[:semente % len(opcoes)]
    lat, lng = lead["latitude"] or 0, lead["longitude"] or 0
    vizinhos = sorted(
        (p for p in paginas_geradas() if p["tom"] == tom and p["place_id"] != lead["place_id"]),
        key=lambda p: math.hypot((p["lat"] or 0) - lat, (p["lng"] or 0) - lng),
    )[:4]
    usados = [p.get(campo) for p in vizinhos]
    return min(ordem, key=lambda o: (usados.count(o), ordem.index(o)))




def texto(s) -> Markup:
    """Escapa e prende termos com hífen numa linha só: o navegador quebra `ar-condicionado` no hífen."""
    return Markup(re.sub(r"(\S+-\S+)", r'<span class="nw">\1</span>', str(escape(s or ""))))


def maior_palavra(s: str) -> int:
    return max((len(p) for p in (s or "").split()), default=1)


# A raiz do gerador também entra no loader: os templates incluem o catálogo como "efeitos/...".
AMBIENTE = Environment(loader=FileSystemLoader([RAIZ / "templates", RAIZ]), autoescape=select_autoescape(["html", "j2"]))
AMBIENTE.filters.update(t=texto, maior=maior_palavra)


def galeria_dados() -> list[tuple[str, str, str]]:
    return [(n, nome, d) for n, (nome, d) in TEMPLATES.items() if (RAIZ / "templates" / f"template-{n}.html.j2").exists()]


def gerar(con, place_id: str, args) -> Path:
    lead = carregar_lead(con, place_id)
    if not lead["telefone"]:
        raise ValueError(f"{lead['nome']} não tem telefone no banco; página sem contato não serve")
    tom = tom_sugerido(lead["categoria"])
    pasta = SAIDA / place_id
    pasta.mkdir(parents=True, exist_ok=True)
    cache = pasta / "conteudo.json"
    if cache.exists() and not args.refazer_texto:
        conteudo = json.loads(cache.read_text())
    else:
        print(f"  escrevendo texto de {lead['nome']} ({tom})…", flush=True)
        conteudo = escrever_conteudo(lead, tom, args.escritor, args.modelo, getattr(args, "voz", None))
        cache.write_text(json.dumps(conteudo, ensure_ascii=False, indent=2))
    meta_arq = pasta / "meta.json"
    anterior = json.loads(meta_arq.read_text()) if meta_arq.exists() and not args.reescolher else {}
    seg = segmento_de(lead["categoria"])
    prontos = [n for n, _, _ in galeria_dados()]
    # Só templates que o segmento aceita; `escolher` evita repetir os vizinhos, então
    # dois negócios do mesmo segmento caem em layouts parecidos, mas não idênticos.
    combinam = [n for n in seg["templates"] if n in prontos] or prontos
    template = args.template or anterior.get("template") or escolher(combinam, lead, tom, "template")
    # Mesmo segmento no mesmo template: a cor precisa mudar, senão as duas páginas ficam idênticas.
    tomadas = [p.get("acento") for p in paginas_geradas()
               if p.get("segmento") == seg["id"] and p.get("template") == template and p["place_id"] != place_id]
    livres = [a for a in seg["claro"]["acentos"] if a not in tomadas] or seg["claro"]["acentos"]
    acento = (getattr(args, "acento", None) or (anterior.get("acento") if anterior.get("acento") in livres else None)
              or escolher(livres, lead, tom, "acento"))
    # O assistente pode tirar blocos da página; sem escolha, entra tudo que tem dado.
    incluir = set(getattr(args, "incluir", None) or INCLUIR)
    if "faq" not in incluir:
        conteudo = conteudo | {"faq": []}
    wa = whatsapp(lead["telefone"])
    tel = re.sub(r"\D", "", lead["telefone"])
    nota = f"{lead['nota']:.1f}".replace(".", ",") if lead["nota"] and lead["avaliacoes"] and "avaliacoes" in incluir else None
    # vCard em data URI: a página continua um arquivo só, sem servidor.
    vcf = ("data:text/vcard;charset=utf-8," + quote(vcard(lead, conteudo["nome_exibicao"], tel))) if "contato" in incluir else None
    foto = bruto(place_id).get("thumbnail") or None
    depo = depoimentos(place_id)
    # Liga só o que a assinatura do template pede, os dados sustentam e a receita não desmarcou.
    marcados = getattr(args, "efeitos", None)
    efeitos = [e for e in ASSINATURAS[template] if e in efeitos_possiveis(seg, conteudo, nota, foto, depo)
               and (marcados is None or e in marcados)]
    html = AMBIENTE.get_template(f"template-{template}.html.j2").render(
        lead=lead, c=conteudo, nota=nota, schema=schema_org(lead, conteudo, tom), wa=wa, tel=tel,
        horario=horario(place_id) if "horario" in incluir else None, vcf=vcf,
        efeitos=efeitos, foto=foto, depoimentos=depo[:8],
    ).replace("</head>", css_segmento(seg, template, acento) + "</head>", 1)
    destino = Path(args.saida) if args.saida else pasta / "index.html"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(html)
    if args.saida:  # amostra (galeria): não mexe no meta nem no índice do lead
        return destino
    meta_arq.write_text(json.dumps({
        "place_id": place_id, "nome": conteudo["nome_exibicao"], "categoria": lead["categoria"],
        "bairro": lead["bairro"], "tom": tom, "template": template, "segmento": seg["id"], "acento": acento,
        "efeitos": efeitos, "lat": lead["latitude"], "lng": lead["longitude"],
    }, ensure_ascii=False, indent=2))
    escrever_indice()
    return destino


def escrever_indice() -> None:
    linhas = "\n".join(
        f'<tr><td><a href="{esc(p["place_id"])}/index.html">{esc(p["nome"])}</a></td><td>{esc(p["categoria"] or "")}</td>'
        f'<td>{esc(p["bairro"] or "")}</td><td><b>{esc(p.get("template", "?"))}</b> {esc(TEMPLATES.get(p.get("template"), ("",))[0])}</td></tr>'
        for p in sorted(paginas_geradas(), key=lambda p: (p["tom"], p["nome"])))
    (SAIDA / "index.html").write_text(
        '<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Landings geradas</title><style>body{font:16px/1.5 system-ui;max-width:960px;margin:40px auto;padding:0 16px}'
        'table{border-collapse:collapse;width:100%}td,th{text-align:left;padding:8px;border-bottom:1px solid #ddd}</style>'
        '<h1>Landings geradas</h1><table><tr><th>Negócio</th><th>Categoria</th><th>Bairro</th><th>Template</th></tr>'
        f"{linhas}</table>")


GALERIA = RAIZ / "galeria"


# Visão "por segmento": o lead mais forte de três ramos bem diferentes, lido do banco local.
SEGMENTOS_EXEMPLO = ("refrigeracao", "construcao", "advocacia")


def leads_exemplo(con) -> list[str]:
    return [linhas[0]["place_id"] for s in SEGMENTOS_EXEMPLO if (linhas := leads_do_segmento(con, s))]


def cartao(href: str, titulo: str, legenda: str) -> str:
    # Miniatura = a própria página num iframe reduzido: sem screenshot para manter atualizada.
    return (f'<a class="t" href="{href}"><div class="m"><iframe src="{href}" loading="lazy" tabindex="-1" '
            f'title="Miniatura: {esc(titulo)}"></iframe></div><b>{esc(titulo)}</b><span>{esc(legenda)}</span></a>')


def gerar_galeria(con, place_id: str, args) -> Path:
    """Todos os templates com o MESMO lead (compara o design) e cada template em 3 segmentos (compara a identidade)."""
    cartoes, linhas = [], []
    for n, nome, direcao in galeria_dados():
        args.template, args.saida = n, str(GALERIA / n / "index.html")
        gerar(con, place_id, args)
        cartoes.append(cartao(f"{n}/index.html", f"{n} · {nome}", direcao))
        trio = []
        for pid in leads_exemplo(con):
            args.saida = str(GALERIA / "segmentos" / n / pid / "index.html")
            gerar(con, pid, args)
            seg = segmento_de(carregar_lead(con, pid)["categoria"])
            trio.append(cartao(f"segmentos/{n}/{pid}/index.html", seg["nome"], ""))
        linhas.append(f'<h3>{n} · {esc(nome)}</h3><div class="g">{"".join(trio)}</div>')
    (GALERIA / "index.html").write_text(
        '<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="robots" content="noindex"><title>Galeria de templates</title><style>'
        'body{font:16px/1.5 system-ui;margin:0;padding:24px 16px 48px;background:#f4f4f2;color:#141414}'
        'h1{font-size:28px;margin:0 0 4px}h2{font-size:24px;margin:48px 0 4px}h3{margin:32px 0 12px}p{margin:0 0 24px;color:#555}'
        'nav a{display:inline-block;min-height:48px;line-height:48px;margin-right:16px;color:#141414}'
        '.g{display:grid;gap:24px;grid-template-columns:repeat(auto-fill,minmax(min(100%,300px),1fr))}'
        '.t{display:grid;gap:6px;color:inherit;text-decoration:none}.t b{font-size:18px}.t span{color:#555}'
        '.m{aspect-ratio:375/700;overflow:hidden;border-radius:12px;border:1px solid #ccc;background:#fff;position:relative}'
        '.m iframe{width:375px;height:700px;border:0;transform-origin:0 0;position:absolute;pointer-events:none}'
        '</style><h1>Galeria de templates</h1><nav><a href="#templates">Por template</a><a href="#segmentos">Por segmento</a></nav>'
        '<h2 id="templates">Por template</h2><p>Todos com o mesmo negócio de exemplo. Toque para abrir.</p>'
        f'<div class="g">{"".join(cartoes)}</div>'
        '<h2 id="segmentos">Por segmento</h2><p>O mesmo template com a cor, a fonte e o texto de cada ramo.</p>'
        f'{"".join(linhas)}<script>'
        # O iframe tem 375 px de largura (celular); escala para caber no cartão.
        'const f=()=>document.querySelectorAll(".m").forEach(m=>m.firstChild.style.transform=`scale(${m.clientWidth/375})`);'
        'f();addEventListener("resize",f)</script>')
    return GALERIA / "index.html"


INCLUIR = {"mapa": "Mapa e como chegar (obrigatório se há endereço)", "avaliacoes": "Nota e avaliações do Google",
           "faq": "Perguntas frequentes", "horario": "Horário com 'aberto agora'", "contato": "Botão 'Salvar contato'"}
RECEITAS = RAIZ / "receitas"
VOLTAR = "← Voltar"


def leads_do_segmento(con, seg_id: str | None = None) -> list:
    linhas = con.execute(
        """SELECT s.place_id, s.nome, s.categoria, s.telefone, s.nota, s.avaliacoes, s.bairro, s.prioridade,
                  en.completo AS endereco
           FROM segmentos s LEFT JOIN enderecos en USING (place_id)
           WHERE s.avaliacoes > 0 AND s.telefone IS NOT NULL
           ORDER BY s.prioridade = 'quente' DESC, s.avaliacoes DESC""").fetchall()
    return [r for r in linhas if seg_id is None or segmento_de(r["categoria"])["id"] == seg_id]


def aplicar(con, args, receita: dict) -> list[Path]:
    """Gera a partir de uma receita (do assistente ou de `--receita`). Devolve as páginas prontas."""
    feitas = []
    for k in ("acento", "voz", "incluir", "escritor", "modelo"):
        setattr(args, k, receita.get(k) or getattr(args, k, None))
    # Lista vazia é escolha (nenhum efeito); só a chave ausente deixa a assinatura inteira.
    args.efeitos = receita.get("efeitos", getattr(args, "efeitos", None))
    # A prévia da galeria deixa `args.saida` apontando para a galeria; aqui a página vai para saida/<id>.
    args.saida = None
    for pid in track(receita["leads"], description="Gerando"):
        args.template = receita.get("template")
        try:
            feitas.append(gerar(con, pid, args))
        except Exception as erro:  # um lead ruim não derruba o lote
            print(f"✗ {pid}: {erro}", file=sys.stderr)
    return feitas


def modo_interativo(con, args) -> None:
    """Assistente em 7 etapas. Cada etapa tem "Voltar"; no fim a escolha vira receita para repetir com --receita."""
    tela, r, etapa = Console(), {}, 0
    contagem: dict[str, list[int]] = {}
    for lead in leads_do_segmento(con):
        n = contagem.setdefault(segmento_de(lead["categoria"])["id"], [0, 0])
        n[0] += 1
        n[1] += lead["prioridade"] == "quente"
    por_id = {s["id"]: s for s in SEGMENTOS}

    def pedir(pergunta):
        resposta = pergunta.ask()
        if resposta is None:  # Ctrl+C
            sys.exit("Cancelado.")
        return resposta

    while etapa < 7:
        tela.rule(f"Etapa {etapa + 1}/7")
        if etapa == 0:
            opcoes = [q.Choice(f"{s['nome']}  ({contagem[s['id']][1]} quentes, {contagem[s['id']][0]} no total)", s["id"])
                      for s in sorted(SEGMENTOS, key=lambda s: -contagem.get(s["id"], [0, 0])[1]) if s["id"] in contagem]
            r["segmento"] = pedir(q.select("Segmento:", opcoes, default=r.get("segmento")))
            etapa += 1
        elif etapa == 1:
            linhas = leads_do_segmento(con, r["segmento"])[:40]
            opcoes = [q.Choice(VOLTAR, VOLTAR)] + [q.Choice(
                f"{l['nome'][:38]:<38} {l['nota']}★ {l['avaliacoes']:>4}  {(l['bairro'] or '-')[:16]:<16} "
                f"{'WhatsApp' if whatsapp(l['telefone']) else 'só fone':<8} {'endereço' if l['endereco'] else 'sem endereço'}",
                l["place_id"], checked=l["place_id"] in r.get("leads", [])) for l in linhas]
            marcados = pedir(q.checkbox("Leads (espaço marca, enter confirma):", opcoes,
                                        validate=lambda v: bool(v) or "Marque ao menos um"))
            if VOLTAR in marcados:
                etapa -= 1
                continue
            r["leads"] = marcados
            etapa += 1
        elif etapa == 2:
            seg = por_id[r["segmento"]]
            opcoes = [q.Choice("Automático (o gerador evita repetir os vizinhos)", "auto")] + [
                q.Choice(f"{n} {TEMPLATES[n][0]} — {TEMPLATES[n][1]}", n) for n in seg["templates"] if n in TEMPLATES
            ] + ["Ver a prévia no navegador", VOLTAR]
            escolha = pedir(q.select("Template:", opcoes))
            if escolha == VOLTAR:
                etapa -= 1
            elif escolha == "Ver a prévia no navegador":
                if not (GALERIA / "index.html").exists():
                    gerar_galeria(con, leads_exemplo(con)[0], args)
                webbrowser.open((GALERIA / "index.html").as_uri() + "#segmentos")
            else:
                r["template"] = None if escolha == "auto" else escolha
                lead = carregar_lead(con, r["leads"][0])
                seg_l = segmento_de(lead["categoria"])
                cache = SAIDA / lead["place_id"] / "conteudo.json"
                # Sugestão pelo 1º lead marcado; sem texto escrito ainda, só dá para julgar foto, nota e avaliações.
                cont = json.loads(cache.read_text()) if cache.exists() else {"servicos": [0] * 4, "passos": [0] * 3, "diferenciais": [0]}
                pode = efeitos_possiveis(seg_l, cont, lead["nota"] and lead["avaliacoes"], bruto(lead["place_id"]).get("thumbnail"),
                                         depoimentos(lead["place_id"]))
                nomes = ASSINATURAS[r["template"]] if r["template"] else list(EFEITOS)
                ef = pedir(q.checkbox("Efeitos de movimento (sugeridos para este template e estes dados):",
                                      [q.Choice(VOLTAR, VOLTAR)] + [
                                          q.Choice(EFEITOS[e], e, checked=e in pode,
                                                   disabled=None if e in pode else "sem dado real")
                                          for e in nomes]))
                if VOLTAR in ef:
                    continue
                r["efeitos"] = ef
                etapa += 1
        elif etapa == 3:
            seg = por_id[r["segmento"]]
            cor = pedir(q.select("Cor principal:", [q.Choice("Automática (muda entre vizinhos)", "auto")]
                                 + seg["claro"]["acentos"] + [VOLTAR]))
            if cor == VOLTAR:
                etapa -= 1
                continue
            r["acento"] = None if cor == "auto" else cor
            r["voz"] = pedir(q.select("Tom de voz:", [q.Choice(f"Do segmento: {seg['voz'][:60]}", "segmento")]
                                      + [q.Choice(v, k) for k, v in VOZES.items()]))
            r["voz"] = None if r["voz"] == "segmento" else r["voz"]
            etapa += 1
        elif etapa == 4:
            incluir = pedir(q.checkbox("O que entra na página (só aparece se o dado existir):",
                                       [q.Choice(VOLTAR, VOLTAR)] + [q.Choice(v, k, checked=True, disabled="sempre" if k == "mapa" else None)
                                                                     for k, v in INCLUIR.items()]))
            if VOLTAR in incluir:
                etapa -= 1
                continue
            r["incluir"] = list(dict.fromkeys(["mapa", *incluir]))
            r["escritor"] = pedir(q.select("Quem escreve o texto:", list(ESCRITORES), default=args.escritor))
            r["modelo"] = pedir(q.text("Modelo:", default=args.modelo))
            if pedir(q.confirm("Mostrar o prompt que será usado?", default=False)):
                lead = carregar_lead(con, r["leads"][0])
                tela.print(montar_prompt(lead, tom_sugerido(lead["categoria"]), r["voz"]), markup=False)
            etapa += 1
        elif etapa == 5:
            t = Table(title="Revisão", show_header=False)
            t.add_row("Segmento", por_id[r["segmento"]]["nome"])
            t.add_row("Leads", str(len(r["leads"])))
            t.add_row("Template", r["template"] or "automático")
            t.add_row("Cor", r["acento"] or "automática")
            t.add_row("Voz", r["voz"] or "do segmento")
            t.add_row("Entra", ", ".join(r["incluir"]))
            t.add_row("Efeitos", ", ".join(r.get("efeitos") or []) or "nenhum")
            t.add_row("Escritor", f"{r['escritor']} / {r['modelo']}")
            tela.print(t)
            escolha = pedir(q.select("Tudo certo?", ["Gerar", *(f"Voltar para a etapa {i}" for i in range(1, 6))]))
            etapa = 6 if escolha == "Gerar" else int(escolha[-1]) - 1
        else:
            RECEITAS.mkdir(exist_ok=True)
            arq = RECEITAS / f"{r['segmento']}-{time.strftime('%Y%m%d-%H%M%S')}.yaml"
            arq.write_text(yaml.safe_dump(r, allow_unicode=True, sort_keys=False))
            feitas = aplicar(con, args, r)
            verificar(feitas)
            for f in feitas:
                webbrowser.open(f.resolve().as_uri())
            tela.print(f"Receita salva. Para repetir: uv run gerar.py --receita {arq.relative_to(RAIZ)}")
            etapa = 7


def verificar(paginas: list[Path]) -> None:
    """Roda o verificador nas páginas novas, se o Chrome do Playwright estiver configurado."""
    if not paginas or not os.environ.get("CHROME"):
        print("Verificador pulado: defina CHROME para rodar (ver README).")
        return
    subprocess.run(["uv", "run", str(RAIZ / "verificar" / "verificar.py"), *map(str, paginas)])


def main() -> None:
    p = argparse.ArgumentParser(description="Gera landing pages estáticas para leads do leads.db.")
    p.add_argument("--place-id", action="append", help="lead específico (pode repetir)")
    p.add_argument("--presenca", choices=["sem_nada", "so_rede_social", "site_proprio"])
    p.add_argument("--prioridade", choices=["quente", "morno"], default="quente")
    p.add_argument("--nicho", default="alto", help="alto, um de NICHOS_ALTOS ou texto da categoria")
    p.add_argument("--limite", type=int, default=5)
    p.add_argument("--template", type=lambda s: s.zfill(2), choices=TEMPLATES, help="número do template (padrão: escolhe evitando os vizinhos)")
    p.add_argument("--saida", help="grava o HTML neste caminho (amostra de galeria) sem tocar meta/índice")
    p.add_argument("--reescolher", action="store_true", help="ignora o template salvo e escolhe de novo")
    p.add_argument("--escritor", choices=ESCRITORES, default="omp", help="CLI que escreve o texto")
    p.add_argument("--modelo", default="sonnet", help="modelo passado ao escritor")
    p.add_argument("--refazer-texto", action="store_true", help="ignora conteudo.json já gerado")
    p.add_argument("--listar", action="store_true", help="só lista os candidatos do segmento")
    p.add_argument("--galeria", nargs="?", const="auto", metavar="PLACE_ID",
                   help="gera gerador/galeria/ com todos os templates (padrão: lead mais forte de refrigeração)")
    p.add_argument("--receita", help="repete uma geração salva pelo assistente (gerador/receitas/*.yaml)")
    args = p.parse_args()

    con = conectar()
    if args.receita:
        feitas = aplicar(con, args, yaml.safe_load(Path(args.receita).read_text()))
        verificar(feitas)
        sys.exit(0 if feitas else 1)
    if args.galeria:
        pid = leads_exemplo(con)[0] if args.galeria == "auto" else args.galeria
        print(f"✓ {gerar_galeria(con, pid, args)}")
        return
    if args.place_id:
        ids = args.place_id
    elif args.presenca:
        linhas = listar_candidatos(con, args.presenca, args.prioridade, args.nicho, args.limite)
        if args.listar:
            for r in linhas:
                print(f"{r['place_id']}  {r['nome'][:50]:<50} {r['categoria']} {r['nota']}★ {r['avaliacoes']}")
            return
        ids = [r["place_id"] for r in linhas]
    else:
        modo_interativo(con, args)
        return
    falhas = 0
    for pid in ids:
        try:
            print(f"✓ {gerar(con, pid, args)}")
        except Exception as erro:  # um lead ruim não derruba o lote
            falhas += 1
            print(f"✗ {pid}: {erro}", file=sys.stderr)
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()
