# scraping-leads

Base de empresas do Google Maps para prospecção: quem não tem site ou tem site ruim recebe uma landing page pronta e, depois, a oferta do Agentic (agente que mantém a landing e cuida do atendimento).

Uso educacional. O repositório não traz dados coletados. Quem roda a coleta responde pelos termos do Google e pela LGPD.

## Requisitos

Docker (no macOS, `colima`), `python3`, `sqlite3` e [`uv`](https://docs.astral.sh/uv/). O gerador também usa o Chromium do Playwright (`uvx playwright install chromium`) e o `ffmpeg` para gravar vídeo.

## Fluxo

1. **Coleta:** `coleta/coletar.sh "<minLat,minLon,maxLat,maxLon>"` roda o [gosom/google-maps-scraper](https://github.com/gosom/google-maps-scraper) em grade (Docker, via `colima start`) e carrega o resultado no `leads.db` local. Sem duplicar: a chave é o `place_id` do Google.
2. **Banco:** `sqlite3 leads.db < banco/segmentos.sql` cria a view de segmentação.
3. **Estudo:** `estudo/00-sintese.md` reúne o que aprendemos nos vídeos de referência sobre landing page, diretórios e venda de agentes.
4. **Gerador:** `gerador/` monta uma landing estática por empresa. Ver `gerador/README.md`.

## Banco

| Tabela | Conteúdo |
|---|---|
| `empresas` | nome, categoria, telefone, site, nota, avaliações, link do Maps, coordenadas |
| `enderecos` | rua, bairro, cidade, CEP |
| `categorias`, `empresa_categorias` | todas as categorias de cada empresa |
| `contatos` | telefone, site e e-mail, com a origem |
| `segmentos` (view) | `presenca` (sem_nada, so_rede_social, site_proprio) e `prioridade` (quente, morno, frio) |

Ver localmente: `uvx datasette leads.db`.

## Dados

`leads.db` e `data/` ficam fora do git: são dados de empresas e de pessoas (LGPD).
