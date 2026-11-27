# Estudo 01 — "Why Are AI Micro Directories Taking Over Google?"

Fonte: Jesse Cunningham, YouTube `Yw5e4QZGM-s` (11:22, publicado 2026-10-07).

## 1. Resumo do vídeo

Jesse Cunningham (dono da comunidade "Rank Expand Academy" no Skool) apresenta o "AI Micro Directory": um site estático pequeno que lista **todas as empresas reais de um nicho numa área** (normalmente um estado, podendo ir até condado), gerado por IA a partir de **uma planilha**. A tese: diretórios em WordPress com plugin são lentos, frágeis e de conteúdo templateado; o micro diretório em HTML puro, com schema em toda página, texto único por empresa e uma página "melhores X em Y" por cidade, rankeia melhor no Google e é citado por ChatGPT/Gemini (GEO). Monetiza com vaga de "destaque" paga (US$ 29/mês, visto nos frames). O vídeo é também propaganda do "directory blueprint" (zip de instruções para LLM/Claude Code) vendido na comunidade.

## 2. Conhecimento extraído

### Definição e formato
- [00:00] Micro diretório = "todo negócio real de um nicho em um estado". Ex.: construtores de piscina (Pool Builders).
- [00:30] Pode descer ao nível de condado. **Uma planilha = um site pequeno.**
- [00:30] O site inteiro tem **4 tipos de página**: home, página do estado, páginas de cidade (as mais importantes) e páginas de cada empresa (listing).
- [01:01] Exemplo ao vivo ("Florida Custom Pool Builders"): feito em 1–2 horas, ainda sem imagens, ~1.500 empresas. Cada listing tem "como chegar", telefone, site. Frames: **1.557 listings em 145 cidades** [09:17]; cards com nota, nº de avaliações no Google, horário, endereço, "Listing claimed on Google", "Services and details" [00:55, 01:19].
- [01:01] Carrega muito rápido vs. diretórios de plugin.
- [01:35] Posicionamento: maior que um micro site (site "rank and rent" de um negócio), muito menor que os diretórios gigantes (Yelp). Frame [01:26]: "pequeno o bastante para cada página ser boa, grande o bastante para dominar um estado inteiro de um ofício". Micro site e micro diretório podem trabalhar juntos.

### Ferramenta / processo
- [01:35–02:05] Na Rank Expand Academy → "Directory Playbook" → "directory blueprint": um **arquivo zip com as instruções** ("o cérebro") que o LLM usa para construir o site no formato exato, para qualquer nicho/área.
- [02:05] Ingredientes de qualquer site de SEO local: **nicho + área específica** (estado ou condado).
- [10:09] Como construir, etapas: **scope (escopo), clean and enrich (limpar e enriquecer dados), plan, build, launch**.
- [10:43] Tempo: 1–2 horas; o primeiro demora mais para montar o sistema.
- [11:15] Caminho mais simples: pegar o zip, dar ao **Claude Code** e dizer "vai".
- [10:43] Comunidade: trial de 7 dias, "700+ pessoas", auto‑declarada nº 1 de AI SEO no Skool (propaganda).

### O que NÃO é
- [02:05–02:35] Não é clone do Yelp; não é diretório em plugin WordPress; não é página spam de IA; não tem empresa falsa; não tem esquema de links. Blogs podem funcionar se incorporados.

### Vantagens declaradas
- [02:35–03:44] Página estática já pronta vs. WordPress que monta a página enquanto o usuário espera (query no banco, tema, plugins de imagem, segurança, cache, diretório, importação). "Diretório de plugin é uma torre; micro diretório é um arquivo de dados." Frame [05:17]: comparação de quantidade de scripts (WordPress ~56% / estáticos "script heavy" vs. "1 script" no blueprint).
- [03:44] Lista de vantagens (frame [04:40]):
  1. **Velocidade de construção** — antes exigia equipe de VAs raspando dados/APIs [04:18].
  2. **Páginas reais**.
  3. **Dados estruturados: schema em toda página** [04:18, 05:20].
  4. **Editar pedindo** — pede ao LLM em vez de mexer no CMS [04:18, 05:51].
  5. **Páginas únicas em escala**.
  6. **Nada para quebrar** — sem banco, sem login, sem update de plugin [04:48].
  + **Vantagem GEO**: toda página de cidade é uma lista "melhores de", formato que ChatGPT adora (listicle) [04:48].
- [05:20] Google não rankeia filtros, rankeia páginas: slugs concretos (ex. `/pool-builders/florida/bonita-springs`) [INFERÊNCIA no formato exato; ele só mostra que são "concretos"] vs. slugs com parâmetros de plugin.
- [05:20] Schema = vocabulário acordado entre Google, Bing etc. para os indexadores entenderem o site; já vem embutido.
- [06:00] Frame: com plugin você aprende shortcodes, briga com tema/builder, torce para o update não desfazer, ou paga alguém **US$ 700 a US$ 3.800** para fazer; no micro diretório "muda o site inteiro com uma frase".

### Conteúdo e "information gain"
- [05:51] Plugin preenche template; **IA escreve cada página a partir dos fatos da própria empresa**. Risco de alucinação ("hoje quase não vejo").
- [06:23] O que mais importa: **information gain**. Ex.: "Florida Leak Solutions Inc." — empresa real; o texto descreve a empresa com base no site dela e **tira uma conclusão** a partir disso. Frame [06:19] mostra texto com anos de experiência e nº de licença extraídos do site.
- [06:57] Diretórios antigos perdem porque são texto templateado.

### Palavra‑chave e GEO
- [06:57] A palavra‑chave é **"best X in Y"** (ex. "best pool builders in Austin"); importa para ChatGPT, Gemini e AI Overviews. Frame [07:01]: volume citado **8.200** para uma variação ("who are the best pool builders in…").
- [07:29] Quem busca "melhor X" geralmente é comprador → tráfego premium. Cada página de cidade (geralmente **100+** por diretório) é uma **página de dinheiro**.
- [07:29–08:00] É o velho "roundup post" (pré Helpful Content Update ~2023) refeito a partir de dados. Frame [08:21]: antes = 10 blurbs de uma busca rápida, publicado uma vez, repetido à mão por cidade; agora = todo negócio real do nicho, ranqueado por nota e nº de reviews, cada um enriquecido pelo próprio site, toda cidade coberta. Blogs informacionais "estão de saída".
- [08:30] Dado da **BrightLocal** (800 buscas locais no ChatGPT): sites das empresas = **58%** das fontes; depois menções e diretórios. Entre diretórios, topo: **Three Best Rated, Expertise, TripAdvisor** — os dois primeiros são listas "best of". Ausentes: Yelp, Facebook, Google Maps. Conclusão: o modelo quer uma lista curta e ranqueada por lugar.

### Estrutura on‑page
- [09:07] Toda cidade pode rankear. **H1**: "Pool Builders in Bonita Springs, FL". Frame [09:37]: texto da cidade cita condado (Lee County) e cidades vizinhas. Cidades sem página própria ficam listadas sob a cidade mais próxima [09:17].
- [09:37] **H2**: "Best pool builders in Jensen Beach".
- [09:37–10:09] Página da empresa importa menos que a da cidade (cidade pega mais queries), mas precisa de info suficiente: nº real de reviews do Google, contato real, horário, **redes sociais** (Instagram, YouTube).
- Monetização (só nos frames [04:07, 04:13, 09:40, 09:44, 10:21]): bloco "Featured pool builders in <cidade> — This position is open — Put your business at the top of the <cidade> page — **from US$ 29 a month** — Get featured", na página do estado e de cada cidade.

## 3. Aplicação ao nosso negócio

### (a) Escolher leads na base
- Nossa base (6.781 empresas de Santarém) **já é a "planilha"** do micro diretório. Dá para cortar por nicho (view `segmentos`) e gerar diretórios do tipo "Melhores [nicho] em Santarém" [INFERÊNCIA].
- Os campos que ele usa (nota, nº de reviews, telefone, site, horário, redes) servem como critério: empresas **sem site** ou com poucas reviews são as que mais ganham com landing page; empresas com muitas reviews e sem site são o melhor alvo (já têm prova social, falta a vitrine) [INFERÊNCIA].
- O passo "clean and enrich" [10:09] = o que precisamos fazer antes de abordar: limpar duplicados, conferir telefone, raspar o site existente para avaliar qualidade.

### (b) Montar a landing page
- Copiar o stack: **HTML estático, 1 script, schema `LocalBusiness` em toda página, slug concreto**, gerado por LLM a partir de uma planilha/JSON [02:35–05:20]. Uma landing por cliente = 1 linha da base + enriquecimento.
- Texto com **information gain**: a IA lê o site/Instagram/Google do cliente e escreve conclusões próprias, não template [06:23].
- Bloco com nota e nº de reviews do Google, horário, mapa/"como chegar", WhatsApp, redes [10:09].
- H1 com serviço + cidade ("Dentista em Santarém, PA") [09:07].
- Sem WordPress → hospedagem estática barata (ex. Cloudflare Pages) [INFERÊNCIA].

### (c) Abordar e vender
- Montar um **diretório público "Melhores X em Santarém"** por nicho vira isca: o cliente se vê listado e já sente o valor; vender destaque (o modelo US$ 29/mês, em reais) e, a partir dele, a landing própria [INFERÊNCIA; o vídeo só mostra o bloco "Get featured"].
- Argumento de venda: "quando alguém pergunta ao ChatGPT 'melhor X em Santarém', ele olha sites de empresas (58%) e listas best‑of" (dado BrightLocal [08:30]). Empresa sem site fica fora.
- Argumento contra o concorrente WordPress: lento, quebra, manutenção custa US$ 700–3.800 [06:00].
- Prova rápida: gerar a landing do lead **antes** da conversa (1–2 h pelo método, provavelmente minutos para 1 página) e mostrar pronta [INFERÊNCIA].

### (d) Vender o Agentic
- "Edit by asking / change the whole site with a sentence" [04:18, 05:51] é exatamente a proposta do Agentic: o cliente pede pelo WhatsApp "muda o horário", "põe a promoção" e o agente edita o HTML. Site estático sem banco/login reduz o que pode quebrar quando um agente mexe [04:48].
- O agente também pode manter o diretório (atualizar reviews, horários) e vender/renovar destaques [INFERÊNCIA].

### O que NÃO serve / não se aplica
- **Escopo "um nicho em um estado"**: no Pará/Santarém o volume de busca é baixo; um diretório estadual de um nicho dá poucas cidades rentáveis. Melhor: um diretório **multinicho de Santarém** ou nicho × cidades do oeste do Pará (Santarém, Itaituba, Oriximiná, Alenquer, Monte Alegre) [INFERÊNCIA].
- **Volumes e "100+ páginas de cidade como money pages"** são de mercado americano (8.200 buscas) — não esperar isso em Santarém.
- **Dado BrightLocal e fontes citadas (Three Best Rated, TripAdvisor)** é dos EUA; no Brasil o comportamento pode diferir (Google Maps e Instagram pesam muito) [INFERÊNCIA].
- O blueprint zip é pago e não está aqui; não dependemos dele — o Claude Code e um template próprio cobrem.
- "Destaque por US$ 29/mês" é monetização de diretório (renda passiva tipo rank and rent), não a venda direta de landing page que queremos — serve como complemento, não como produto principal.

## 4. Riscos e ressalvas

- **Promessas exageradas**: "pronto em 1–2 horas", "rankeia melhor", "ChatGPT adora" — sem nenhum dado de ranking/tráfego/receita do site mostrado; o exemplo nem tem imagens. Vídeo é funil de venda da comunidade Skool.
- **Alucinação**: ele mesmo admite [05:51]. Texto gerado sobre empresa real com informação errada (licença, anos de mercado, serviço) é risco jurídico e de reputação; precisa revisão humana.
- **"Best of" sem critério**: chamar de "melhores" e ranquear por nota pode gerar reclamação; vender "destaque" no topo de uma lista de "melhores" mistura publicidade e ranking — no Brasil, o CDC exige identificar publicidade claramente (art. 36) [INFERÊNCIA].
- **LGPD**: dados de empresas (CNPJ, telefone comercial) têm base mais tranquila, mas MEI/autônomo com telefone pessoal é dado pessoal; publicar e usar para prospecção exige base legal (legítimo interesse), opção de remoção e cuidado com WhatsApp em massa [INFERÊNCIA].
- **Termos do Google**: reproduzir nota/reviews/horários raspados do Google Maps num site viola os termos da Google Maps Platform/raspagem; o vídeo não aborda isso. Usar a API oficial (com atribuição e limites de cache) ou mostrar só dados próprios/fornecidos pelo cliente [INFERÊNCIA].
- **Uso de nome/marca de terceiros**: listar empresa sem consentimento e cobrar para "subir" pode ser visto como extorsivo; oferecer remoção fácil [INFERÊNCIA].
- **Spam do Google**: muitas páginas de cidade geradas por IA com pouca diferença podem cair como "scaled content abuse"; o próprio vídeo depende do information gain para escapar disso.
