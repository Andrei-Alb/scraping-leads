# Estado do projeto

## Objetivo
Achar empresas no Google Maps que não têm site ou têm site ruim. Oferecer a elas uma landing page pronta e, depois, o Agentic (agente que mantém a landing e cuida do atendimento).

## Escopo
- Região: Santarém-PA, área urbana. Alter do Chão fica fora.
- Fonte: só o Google Maps. Empresa fora do Maps não entra.
- Lead: sem site, só com rede social, ou com site que dá pra melhorar.

## Ferramentas escolhidas
- Coleta: [gosom/google-maps-scraper](https://github.com/gosom/google-maps-scraper), sem API.
- Enriquecimento (pendente): [omkarcloud/google-maps-scraper](https://github.com/omkarcloud/google-maps-scraper), só nos leads quentes.
- Banco: SQLite local.

## Coleta
- O binário nativo no macOS derruba o Chrome ao rolar a lista (depth > 1, "target closed"). Rode via Docker (`colima start`).
- Rodada 1: 40 buscas "X em Santarém PA", depth 10, com e-mail → 2.210 empresas.
- Rodada 2: grade, bbox `-2.48,-54.80,-2.39,-54.64`, células de 2 km, 80 buscas (`coleta/queries-grade.txt`), depth 4, sem e-mail, ~3h40 → 4.571 empresas novas.
- Total: 6.781 empresas. 5.095 com telefone, 1.851 com site, 160 com e-mail.
- Atenção: a grade gera muito dado no disco do Colima (~30 GB). Confira o espaço livre antes de rodar.

## Segmentos (view `segmentos`)
`presenca`: sem_nada, so_rede_social (Instagram, Facebook, WhatsApp, Linktree), site_proprio.
`prioridade`: quente (≥ 20 avaliações e nota ≥ 4,3), morno (≥ 20 avaliações), frio.

| presenca | quente | morno | frio |
|---|---|---|---|
| sem_nada | 582 | 172 | 4.172 |
| so_rede_social | 208 | 16 | 542 |
| site_proprio | 379 | 103 | 602 |

## Estudo de referência
`estudo/00-sintese.md` resume 5 vídeos. Conclusões:
- Chegar com a landing pronta fecha mais reuniões.
- Lead certo: tem avaliações, não tem site bom, ticket alto. Excluir quem tem 0 avaliações.
- O Agentic funciona como gerente: avaliações, WhatsApp, reativação, resumo semanal; o dono aprova.
- Cobrança em escada, mensalidade fixa, garantia. Não vender como "IA".
- Não fazer: rank-and-rent com telefone falso, rede de diretórios trocando links.
- Cuidados: LGPD (médicos, MEI) e termos do Google ao republicar dado raspado.

## Gerador
`gerador/` monta uma landing estática por `place_id`, com 8 templates e verificador Playwright. Ver `gerador/README.md`.

## Próximos passos
1. Testar o gerador em leads quentes sem site.
2. Auditar os sites próprios (status, https, viewport, tempo de carga, construtor, WhatsApp, ano do rodapé).
3. Enriquecer os leads quentes com dados públicos do próprio negócio (Instagram, e-mail).
