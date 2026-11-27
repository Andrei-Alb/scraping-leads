#!/usr/bin/env bash
# Coleta em grade de uma cidade com o gosom/google-maps-scraper e carrega no leads.db.
# Docker e não o binário nativo: no macOS o binário derruba o Chrome ao rolar a lista (depth > 1).
# Uso: coleta/coletar.sh "<minLat,minLon,maxLat,maxLon>" [arquivo-de-buscas]
# Santarém-PA (área urbana): coleta/coletar.sh "-2.48,-54.80,-2.39,-54.64"
set -euo pipefail

raiz="$(cd "$(dirname "$0")/.." && pwd)"
bbox="${1:?informe a bbox minLat,minLon,maxLat,maxLon}"
buscas="${2:-$raiz/coleta/queries-grade.txt}"
saida="$raiz/data/grade-$(date +%Y%m%d-%H%M).json"

mkdir -p "$raiz/data"
cp "$buscas" "$raiz/data/buscas.txt"
touch "$saida"

# A grade de Santarém (54 células x 80 buscas) levou 3h40 e o disco do Colima cresce bastante: confira o espaço livre antes.
docker run --rm -v "$raiz/data:/data" gosom/google-maps-scraper:latest \
  -input /data/buscas.txt -results "/data/$(basename "$saida")" -json -lang pt-BR \
  -grid-bbox "$bbox" -grid-cell 2 -zoom 15 -depth 4 -c 4 -exit-on-inactivity 5m \
  > "${saida%.json}.log" 2>&1

python3 "$raiz/coleta/carregar.py" "$saida" "$raiz/leads.db"
