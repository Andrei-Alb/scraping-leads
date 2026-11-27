# Estudo de templates — landing de negócio local

## Referências lidas

| Link | O que faz bem |
|---|---|
| https://swipepages.com/blog/7-best-local-business-landing-page-examples-of-2026 | Telefone clicável no topo, uma ação só por página, prova social perto do CTA. |
| https://www.verlua.com/blog/landing-page-design-examples | Comenta LeafFilter, Morgan & Morgan e Sacramento Gutter Guard: oferta clara acima da dobra, formulário curto, selos de confiança. |
| https://www.verlua.com/blog/contractor-website-examples | Construção: fotos de obra, área atendida, orçamento grátis em destaque. |
| https://hookagency.com/blog/home-service-website-examples/ | Home services: telefone gigante, avaliações, garantias, CTA repetido ao longo da página. |
| https://www.forthepeople.com/ | Advocacia (Morgan & Morgan): headline direta, CTA de consulta, autoridade por números. |
| https://www.leaffilter.com/ | Oferta + formulário na dobra, faixa de avaliações logo abaixo. |
| https://sacramentogutterguard.com/ | Local pequeno: nome da cidade na headline, foto real, telefone no topo. |
| https://lokalhq.com/blog/hvac-service-page | Página de serviço HVAC: lista de serviços, área atendida, FAQ. |
| https://rsgonzales.com/blog/hvac-contractor-website-features | Botão de ligar fixo no celular, horário, urgência. |
| https://www.simprogroup.com/blog/hvac-websites | Exemplos HVAC: contraste alto, CTA em toda seção. |
| https://beefoundonline.com/blog/contractor-landing-page-best-practices | Uma meta por página, sem menu que distrai. |
| https://www.nngroup.com/articles/scrolling-and-attention/ | ~57% da atenção fica acima da dobra: o essencial vai no topo. |
| https://unbounce.com/conversion-benchmark-report/ | Texto simples e curto converte mais. |

Templates open source vistos (só referência de estrutura, nada copiado):
- https://github.com/gridtemplate/DiwaDental-HTML5-and-Bootstrap5-Template-For-Dentist-and-Medical-Clinics
- https://github.com/tookit/dental-website-template
- https://github.com/Stephen-Psaradellis/law-firm-website-template
- https://github.com/Stephen-Psaradellis/plumber-website-template
- https://github.com/digitallawyer/freefirmsite

Os gratuitos são genéricos: Bootstrap pesado, carrossel, foto de banco, menu cheio. Os que convertem são o oposto.

## Padrão que se repete
1. Headline com serviço + cidade acima da dobra.
2. Telefone grande e clicável; no celular, barra fixa Ligar / WhatsApp.
3. Prova social (nota e número de avaliações) colada no CTA.
4. Lista curta de serviços, 3 diferenciais, "como funciona" em 3 passos.
5. FAQ local (bairro, horário, como chegar) e schema.org LocalBusiness + FAQPage.
6. Um objetivo só: contato. Sem menu, sem links que tiram o visitante.

## v2: referências premiadas (movimento)
Os 3 templates da v1 ficaram genéricos demais. A v2 parte de sites premiados de negócio local e serviço.

| Referência | O que copiamos |
|---|---|
| [South Cliff Dental Group](https://www.awwwards.com/sites/south-cliff-dental-group) (Awwwards) | Clínica com tom calmo e entrada coreografada. Vai para `clinica`: hero em planos com parallax, nada de foto de banco. |
| [Kümmerlein Lawyers & Notaries](https://www.awwwards.com/sites/kummerlein-lawyers-notaries) (Honorable Mention 2025) | Advocacia editorial, tipografia como imagem. Vai para `liberal`: monograma gigante e manifesto que acende com o scroll. |
| [Hafnia Law](https://www.awwwards.com/sites/hafnia-law) (Honorable Mention 2024) | Corporativo sóbrio, muito respiro, áreas de atuação como trilho. Vai para `liberal`: trilho horizontal pinado. |
| [FIRMA](https://www.awwwards.com/sites/firma) (Nominee 2025) | Landing animada de escritório de advocacia. Confirma que movimento cabe em nicho sério, desde que contido. |
| [METRIC.](https://www.awwwards.com/sites/metric) (Honorable Mention 2026) | Serviço de obra com tipo larga e contraste alto. Vai para `tecnico`: palavra gigante vazada em parallax e faixa de serviços que anda com o scroll. |

A análise vem das páginas da galeria e da descrição dos estúdios. Não copiamos código nem imagem.

## O que fizemos igual ou melhor
- Os 3 templates seguem os 6 pontos acima. Sem framework, 1 fonte do Google, ~40 linhas de JS próprio.
- Movimento: um primitivo `--p` (progresso no scroll, 0 a 1) alimenta parallax, seção pinada e barras. Reveal por IntersectionObserver, contador da nota. Só `transform` e `opacity`.
- `prefers-reduced-motion` desliga tudo; sem JS a página mostra o conteúdo final.
- Mensagem do WhatsApp já preenchida com o nome do negócio.
- `clinica`: creme e sálvia, serifa editorial, hero em 3 planos, "como funciona" pinado com passos que acendem.
- `tecnico`: preto e amarelo, palavra gigante em parallax, faixa de serviços ligada ao scroll, passos em cartões que empilham.
- `liberal`: marfim e azul-tinta, monograma em parallax, manifesto palavra a palavra, áreas num trilho horizontal pinado. Texto dentro do Código de Ética da OAB.

Vídeos e capturas ficam fora do git: mostram empresas reais. Para ver, gere a galeria (`uv run gerador/gerar.py --galeria`) e grave com `gerador/verificar/gravar.py`.

## v3: galeria de 8 templates — referências de bibliotecas e galerias

Regra: copiamos ideia e estrutura (ritmo de seções, composição, tipo de movimento). Nenhum código, imagem ou texto é colado, nem dos itens MIT, para manter os templates sem dependência e sem obrigação de atribuição. Licenças conferidas na fonte em 2026-11-18.

| # | Referência | Licença (fonte) | O que tem de bom | Inspira |
|---|---|---|---|---|
| 1 | [Aceternity UI](https://ui.aceternity.com) | Licença própria ([licence](https://ui.aceternity.com/licence)): uso em produtos finais, proibido revender/redistribuir | Spotlight, grid de fundo, cards com brilho que segue o cursor | 04 Noite |
| 2 | [Magic UI](https://magicui.design) | MIT ([GitHub](https://github.com/magicuidesign/magicui)) | Bento grid, marquee de depoimentos, números animados | 06 Mosaico |
| 3 | [shadcn/ui blocks](https://ui.shadcn.com/blocks) | MIT ([GitHub](https://github.com/shadcn-ui/ui)) | Seções neutras, hierarquia limpa, espaçamento consistente | 03 Suíço |
| 4 | [Tailwind Plus (ex-Tailwind UI)](https://tailwindcss.com/plus) | Comercial paga ([license](https://tailwindcss.com/plus/license)); só olhar | Padrões de hero, feature e CTA muito bem resolvidos | 03 Suíço, 06 Mosaico |
| 5 | [HTML5 UP](https://html5up.net) | CC BY 3.0 ([license](https://html5up.net/license)) | Templates de uma página com seções em tela cheia e capítulos | 07 Capítulos |
| 6 | [Astro Themes](https://astro.build/themes/) | Por tema; ex. [AstroWind](https://github.com/onwidget/astrowind) é MIT | Landings estáticas leves, tipografia editorial | 01 Revista |
| 7 | [Cruip](https://cruip.com/free-templates/) | GPL-3.0 nos grátis ([README](https://github.com/cruip/tailwind-landing-page-template)); proíbe republicar/revender | Hero com prova social e passos, CTA repetido | 05 Quintal |
| 8 | [One Page Love](https://onepagelove.com) | Galeria; cada site é do seu dono | Curadoria só de páginas únicas, ótima para narrativa em scroll | 07 Capítulos, 01 Revista |
| 9 | [Awwwards](https://www.awwwards.com) | Galeria; direitos de cada estúdio | Brutalismo, scroll horizontal e tipo gigante premiados | 02 Concreto, 08 Vitrine |
| 10 | [Godly](https://godly.website) | Galeria; direitos de cada site | Vídeos de movimento: tema escuro de luxo, transições finas | 04 Noite |
| 11 | [Land-book](https://land-book.com) | Galeria; direitos de cada site | Filtro por estilo (minimal, ilustrado, colorido) | 05 Quintal, 03 Suíço |
| 12 | [Lapa Ninja](https://www.lapa.ninja) | Galeria; direitos de cada site | Muitos exemplos editoriais e de revista | 01 Revista |
| 13 | [Dribbble](https://dribbble.com/tags/landing_page) | Shots são dos autores ([terms](https://dribbble.com/terms)) | Conceitos de bento, vitrine horizontal e paletas | 06 Mosaico, 08 Vitrine |

Notas:
- Galerias (8 a 13) não dão licença de uso: servem para estudar composição, nunca para recortar asset.
- MIT (Magic UI, shadcn, AstroWind) permitiria copiar com aviso de licença; mesmo assim escrevemos do zero.
- Tailwind Plus, Aceternity e Cruip têm restrição de redistribuição: só ideia.
- Land-book e Lapa Ninja bloqueiam acesso automatizado (HTTP 403); links abertos no navegador.
