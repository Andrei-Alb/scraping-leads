# Gerador de landing pages

Gera uma landing estática para um lead do `leads.db`. O texto é escrito pelo Claude a partir de `prompts/conteudo-v1.md`.

## Como rodar
1. Tenha `uv` e o `omp` (ou `claude`) logado. O `leads.db` fica na raiz do repo.
2. Interativo: `uv run gerador/gerar.py` (pergunta segmento, lead e número do template).
3. Abra `gerador/saida/<place_id>/index.html` no navegador.

Lote: `uv run gerador/gerar.py --presenca sem_nada --nicho alto --limite 5`
Só listar: acrescente `--listar`. Um lead: `--place-id <id> [--template 01..08]`. Sem `--template`, o gerador escolhe e evita repetir o template de vizinhos.
Galeria: `uv run gerador/gerar.py --galeria [place_id]` gera `gerador/galeria/index.html` com os 8 templates para o mesmo lead (lado a lado, miniatura + nome + direção). Cada template é um design próprio em `templates/template-NN.html.j2`; os dados comuns (links de rota, mapa, horário, vCard) vêm de `templates/_dados.html.j2`.
Opções: `--escritor omp|claude`, `--modelo sonnet`, `--refazer-texto`.

`saida/` e `galeria/` ficam fora do git (dados de lead, LGPD). Templates e prompts são versionados.

## Verificar

`CHROME=<caminho do Chrome> uv run gerador/verificar/verificar.py gerador/galeria/0*/index.html` abre cada página no celular (320, 375), tablet (768x1024, 1024x768) e desktop (1280, 1920) e falha se houver texto sobreposto, palavra quebrada, rolagem lateral, alvo de toque < 48 px, texto de corpo < 16 px ou endereço sem mapa.
`uv run gerador/verificar/gravar.py <index.html> <saida.mp4> <largura> <altura>` grava um vídeo rolando a página.
