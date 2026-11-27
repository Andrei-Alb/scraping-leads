# Estudo 02: "How to Build AI Directories on Easy Mode" (Jesse Cunningham)

Fonte: https://www.youtube.com/watch?v=DzphMeAUJuo (12:38, postado em 16/09/2026). A transcrição é uma tradução automática para o pt-BR das legendas, por isso aparecem erros como "Not Google Maps" (= Google Maps), "Freight Choo"/"Frey" (= Frey Chu), "Rank Expand rent" (= rank and rent), "Claude Fable" e "Month Directory" (= provavelmente GeoDirectory, [INFERÊNCIA]).

## 1. Resumo do vídeo

Jesse Cunningham, dono da comunidade paga Rank Expand Academy (rank and rent com IA), apresenta como montar **diretórios locais de nicho feitos com IA**. Ele se baseia no conteúdo do Frey Chu, que constrói diretórios há bastante tempo. A tese tem duas partes:
1. Diretório é uma lista curada otimizada para SEO on-page, montada em 7 passos: nicho → raspar o Google Maps → limpar → enriquecer → páginas → ranquear → monetizar. Hoje a IA (Claude Code) substitui o WordPress e faz em um prompt o que antes dava muito trabalho.
2. O uso que ele propõe é o diretório **reforçar os microsites** de rank and rent: o diretório funciona como uma "espécie de PBN, só que um site real" e vira um argumento de venda para o dono do negócio, com leads exclusivos. Ele chama isso de "1 + 1 = 3".

Boa parte do vídeo é slide comentado e propaganda da academia (teste grátis de 7 dias e reembolso em 90 dias).

## 2. Conhecimento extraído

### Contexto e premissas
- [00:02] Diretórios de IA servem para impulsionar microsites e também para ganhar dinheiro diretamente.
- [00:02–00:33] Referência principal: o canal do Frey Chu. O OCR dos frames mostra títulos como "The 4 Types of Directories Winning in 2026", "How to Deep Research a Directory Niche", "Selling Public Data as a Product", "$2500 Leads", "He Built a $3000/Month Directory in 2 Months".
- [00:33] Os microsites de rank and rent custam **cerca de US$ 11** para criar, considerando que você já tem um construtor de IA (Claude Code ou GPT). Na prática você paga só a hospedagem ([06:14]).
- [01:05] Se você se mantém em um nicho específico, o diretório é uma tática "muito poderosa" para impulsionar um site.
- [01:05] Caso de origem: um site de cerca de 50 páginas, montado com copiar e colar em 2022, que ainda rende todo mês com quase nenhuma manutenção. Os números vêm de uma entrevista do Jared no Niche Pursuits.
- [01:37] Montar um diretório de mil páginas no WordPress seria "muito doloroso". Com IA "o jogo mudou".

### Estrutura do diretório
- [01:37–02:08] Um diretório é uma **lista curada otimizada para SEO on-page**. Hierarquia: página inicial → páginas de estado → páginas de cidade → listagens.
- Frame [02:17]: "A estrutura é chata de propósito. Cada camada mira um padrão de palavra-chave, e cada camada linka para baixo e de volta para cima." Também: "**Páginas de cidade recebem o tráfego. Listagens individuais quase nunca.** Esse único fato decide toda a construção."
- [02:08] Padrões de busca: "parques para cachorro perto de mim", "… na Flórida", "… em Orlando". A intenção de busca de um diretório é a mesma de um microsite, só que em escala maior.
- [00:41–01:08] (frames) Exemplo de microsite: "Custom Pool Builders in Orlando, FL", com telefone em destaque, CTA "Schedule a Free Design Consultation" e uma seção de FAQ ("Why do Orlando homeowners choose a true custom pool builder?").

### Os 7 passos
- [02:08–02:38] 1) achar o nicho, 2) raspar o Google Maps, 3) limpar as linhas, 4) enriquecer com atributos, 5) criar as páginas, 6) ranquear com o tempo, 7) monetizar.

### Passo 1: nicho
- [02:38] Achar o nicho é a parte lenta. Quem já tem microsites em um nicho (por exemplo, piscinas em Orlando) monta o diretório em volta dele.
- [03:09] Método: Ahrefs Keywords Explorer → digitar "near me" → filtrar **KD (dificuldade) < 20** → rolar além da primeira página. "Os termos chatos na página 10 são a oportunidade." Palavras-chave de baixo volume valem a pena.
- Frame [03:11]: exemplo trabalhado com dog parks, com números (27 / 73K / 500 / 41K) e "20K a 50K buscas mensais". Há menção a "red flags / green flags", a concorrentes (TripAdvisor, care.com, sites de prefeitura) e a "depois ele lê o Reddit para achar as perguntas reais". O OCR está parcial.

### Passo 2: dados (Google Maps)
- [03:09–03:41] **Outscraper** é a ferramenta preferida. Ele cogita trocar por vibe coding ou APIs, mas "se é barato e funciona, vamos com ele".
- [03:41] O Google Maps é a matéria-prima. Paga-se **por linha**. Você escolhe a categoria exata do Maps, seleciona os estados e extrai os campos.
- [03:41] Cerca de **US$ 100 por uma raspagem típica**. Frame [03:39–03:45]: valores de "$317" e "$100", "2 hrs", "6.245 dog parks no país inteiro" e "linhas de amostra são tudo de que você precisa para desenhar o schema". Há também uma nota de que o campo de link/localização é "o que toda ferramenta de enriquecimento vê depois". O OCR está parcial.

### Passo 3: limpeza
- [04:12] A maior parte do que se raspa é lixo. De mais de 100 mil linhas brutas: remover linhas com **zero avaliações** e exigir que o **nome contenha o termo do nicho**. Sobram cerca de **5–6%**.

### Passo 4: enriquecimento
- [04:12] "O enriquecimento é o que transforma uma lista em uma ferramenta."
- [04:12–04:43] Fontes de atributos: avaliações do Google Maps, tags, tópicos do Reddit e "modificadores de RH" (transcrição ruim, provavelmente modificadores do Ahrefs [INFERÊNCIA]).
- [04:43] Como se preenche: uma ferramenta lê cada listagem e cada avaliação e devolve **verdadeiro / falso / informação insuficiente** para cada atributo. O Frey tem uma ferramenta própria para isso. Jesse pretende recriar com vibe coding.
- [04:43] Descrições: GPT for Sheets com prompt customizado. Ele prefere Claude.
- Frame [09:23] (pipeline novo): "**Não são mais as avaliações do Google Maps**. É o site do próprio negócio" (via Crawl4AI). E a regra que "salvou" o Frey: "**Um dado por passada de enriquecimento.** Rode duas ou três vezes. Depois revise os casos de borda à mão." [INFERÊNCIA: o OCR está truncado, mas é essa a leitura.]

### Passo 5: stack
- [05:13] Caminho A é WordPress, caminho B é código feito por IA. Ele escolhe o B. Também dá para usar IA no WordPress dando acesso FTP.
- [05:13–05:43] Stack do caminho WordPress: hospedagem paga na **Hostinger**, **GeoDirectory** (lista programática, importação de CSV em lotes), **WP All Import** (listagens e imagens em massa), **Rank Math**, **Elementor Pro**, **JetEngine**, otimizador de imagem e mapas interativos (GeoDirectory Maps).
- Frame [05:29]: "Path B: AI coded. Todo build novo desde o início de 2025. O Claude Code escreve o app, e um banco de dados real guarda os dados."
- [07:46] Stack de diretório feita com IA: **Claude Code dentro do Cursor, Supabase, Vercel, Next.js, Stripe**.
- [07:15] "Páginas pilar estáticas ganham do programático mais vezes do que você imagina." Segundo o YouTube do Frey, são alguns dos melhores sites dele. O cenário ideal de Jesse é HTML estático, com o porém de ser chato de atualizar.
- [07:46] Ele quer evitar plugins prontos e fazer tudo com as ferramentas de IA.
- [07:46–08:16] "**Sete recursos que levaram um prompt cada**", contra a dor de cabeça do WordPress. Exemplos: **páginas pilar de cidade, 4.800 páginas com FAQ local** ("horrível no WordPress, fácil com IA"); **"reivindique sua listagem"** (claim your listing); **destaques (featured) com schema de loja em todo lugar** (LocalBusiness/Store schema, [INFERÊNCIA]).

### Microsites (contexto do curso)
- [06:14] Microsites são rank and rent com IA em escala. Na academia existem o "Microsite Playbook" e o "Microsite Empire". O site de piscinas saiu de um **arquivo zip que você entrega para a IA**. Frame [06:49]: "Microsite Blueprint for Claude Code".
- [06:14–06:45] Ele testou com o "GPT Astra" e falhou. Hoje prefere Claude (Opus).
- [06:45] Prova social da academia: o "Brandon" teve **59 leads desde domingo**. Frame [06:10]: concurso de SEO de microsite com prêmio de US$ 1.000.

### Custo do pipeline
- [08:48–09:19] Um pipeline de dados novo custa **cerca de US$ 250 por diretório de geração de leads**. Frame [09:23]: **Claude Code Max US$ 100 + cerca de US$ 50 em chamadas de API**, e o restante é o Outscraper [INFERÊNCIA sobre a divisão].
- [09:19] Ferramentas: **Outscraper → Claude Code → Crawl4AI → Classify/Enrich → Claude Vision → Supabase** (fonte da verdade).
- [09:19] Comparação: com US$ 250 dá para fazer 20 a 25 microsites. "Vale a pena?" A pergunta fica em aberto.

### Monetização
- [08:16–08:48] Vender posição no diretório, como os antigos listicles de afiliado ("melhores canecas de café"). Quem está no top 1–3 do Google vende o topo da lista caro. Exemplo: "construtores de piscina na Flórida, alguém vai pagar para ficar no topo do seu diretório".
- Frame [10:43], a escada de monetização (do mais fácil para o mais rentável), com a frase "escolha o degrau antes de escolher o nicho":
  1. **Display ads**: a fatia menor. Entrar na Mediavine ou na Raptive é difícil, e até a Ezoic exige muito tráfego. A transcrição cita **250.000 visitantes/mês** [09:19–09:49]. Ele descarta essa opção.
  2. **Listagem em destaque (featured)**: "mais em alta", **US$ 29 a US$ 500/mês cada** [09:49].
  3. **Venda de leads**: já é rank and rent [09:49].
  4. **Seu próprio serviço**.
- [09:49] "O diretório é o marketplace mais difícil de operar, mas tem teto alto."
- [10:20] O que falta na escada é **influência/audiência**. O primeiro projeto de SEO dele foi um diretório local em 2008/2009, e a lição foi: "em vez de monetizar imediatamente, eu deveria ter acumulado influência".
- [10:20–10:51] Os 4 tipos de diretório que estão ganhando: (1) focados em redes sociais; (2) estilo Yelp/Bark ("Bid, rs"); (3) **geração de leads em nichos de alto valor e chatos**, que é o que ele quer; (4) display ads utilitários e comunidades hipernichadas, que ele não curte.

### A jogada final: diretório + microsites
- [11:21] Diretório vertical = **um nicho + um estado**. Os microsites (por exemplo, piscinas em Orlando, Naples e Miami) ficam no portfólio.
- [11:53] O diretório lista outros negócios também, mas pode dar preferência aos seus microsites.
- Frames [11:11–12:33]: "Uma espécie de PBN, só que é um site real"; "um link do diretório para os microsites é um voto de uma fonte em que esses sistemas já confiam"; "**não é uma jogada de dinheiro, é uma jogada de autoridade**"; "custa um pouco mais que um microsite por causa do trabalho de dados e pode nunca dar receita direta".
- [11:53–12:24] O pitch é ganhar duas vezes: "Ei Bob, sei que você é dono da XYZ de piscinas em Orlando. Eu sou dono deste diretório e de mais cinco sites na sua região que geram leads." Com isso o dono presta atenção, porque são **leads exclusivos, não compartilhados como os do Angie's List**.

## 3. Aplicação ao nosso negócio

### (a) Escolher leads na base
- A regra de limpeza [04:12] vale para a nossa base de 6.781 empresas: **excluir quem tem 0 avaliações** (provável empresa morta ou fantasma) e conferir se a categoria bate com o nicho. A view `segmentos` já faz parte disso. [INFERÊNCIA] Incluir na prioridade um filtro de `avaliações >= 1`, se ainda não existir.
- Para eles, "nichos de alto valor e chatos" [10:51] são os melhores para leads. Na nossa base, priorizar categorias de ticket alto em que um cliente novo paga o ano inteiro (piscinas, clínicas, energia solar, oficinas, construção, advocacia, odontologia) [INFERÊNCIA sobre quais categorias valem em Santarém].
- O enriquecimento verdadeiro/falso/insuficiente [04:43] dá para copiar direto: rodar o Claude sobre avaliações e site de cada empresa para marcar atributos como "tem site?", "site responsivo?", "tem WhatsApp no site?", "reclamações de atendimento nas avaliações?". Seguir a regra de **um atributo por passada** e revisar os casos de borda à mão. Isso melhora a coluna de presença online e prioridade.
- O pipeline Crawl4AI + Claude Vision [09:23] também serve para avaliar a qualidade do site atual do lead (print + nota). Assim dá para separar quem "tem site ruim" automaticamente.

### (b) Montar a landing page
- O microsite de piscinas é um molde simples de landing local: H1 "serviço + cidade", telefone grande, CTA de consulta grátis e FAQ local [00:41–01:08]. Dá para replicar como template: "[Serviço] em Santarém-PA".
- A abordagem de "zip com blueprint entregue ao Claude Code" [06:14] equivale a ter um **template-base + prompt** para gerar cada landing em minutos. Custo baixíssimo, porque só se paga a hospedagem [00:33]. Estático, ou Next.js na Vercel/Cloudflare.
- Para SEO local: página com FAQ local e **schema LocalBusiness** [08:16].
- [INFERÊNCIA] Um diretório "Melhores [nicho] em Santarém", com páginas por categoria, é viável e barato. Os dados já existem, sem os US$ 100 de Outscraper. A estrutura estado → cidade não se aplica porque temos uma cidade só. A camada útil seria categoria → listagens, mais talvez bairros.

### (c) Abordar e vender
- O pitch do "Bob" [11:53] adaptado: "Sou dono do guia X de Santarém, onde sua empresa já aparece. Posso destacar você no topo e montar sua página." A empresa já está listada, o que serve como gancho [INFERÊNCIA].
- **Listagem em destaque** a US$ 29–500/mês [09:49] vira referência de produto recorrente barato. Em Santarém o preço precisa ser bem menor, em R$ [INFERÊNCIA].
- O "reivindique sua listagem" [08:16] é um funil de entrada: o dono reivindica a página no diretório e ali recebe a oferta da landing.
- Leads exclusivos, não compartilhados [12:24], são um argumento forte se em algum momento vendermos leads.

### (d) Vender o Agentic
- O vídeo não fala de agente operando o site do cliente. O mais perto disso: "sete recursos, um prompt cada" [07:46] e 4.800 páginas de FAQ com IA [08:16] mostram que a manutenção por IA é barata. [INFERÊNCIA] Esse é o argumento do Agentic: "o agente atualiza sua página, FAQ, horários e promoções quando você pede".
- Supabase como fonte da verdade e Next.js/Vercel como front [07:46, 09:23] também cabem como arquitetura do Agentic: os dados do cliente ficam no banco e o agente edita o banco [INFERÊNCIA].

### O que NÃO serve ou não se aplica
- **Ahrefs e pesquisa de volume "near me"** [03:09]: em Santarém o volume de busca por nicho é minúsculo e o Ahrefs custa caro. Nosso nicho vem da base, não da pesquisa de palavra-chave.
- **Outscraper** [03:41]: já temos a raspagem.
- **Display ads** (Mediavine/Raptive/Ezoic) [09:19]: inviável com o tráfego de uma cidade de cerca de 300 mil habitantes [INFERÊNCIA].
- **Escala estado/cidade e 4.800 páginas**: é pensada para os EUA e não se aplica.
- **Rank and rent / PBN** como modelo central: nosso modelo é vender o site para o cliente, não alugar site próprio. O "diretório como PBN" serve no máximo como ativo de autoridade local.
- **Stack WordPress** [05:43]: o próprio autor descarta.
- **Preços em US$**: as referências (US$ 11, US$ 100, US$ 250, US$ 29–500) não se convertem direto para o poder de compra local.

## 4. Riscos e ressalvas
- **Viés comercial**: o vídeo funciona como funil da Rank Expand Academy (teste de 7 dias, reembolso em 90 dias, "59 leads do Brandon"). As vitórias citadas são anedotas sem verificação.
- **Os números são de terceiros**: o site de 50 páginas que "rende todo mês" vem de uma entrevista sem valor declarado. O próprio autor admite que o diretório "pode nunca dar receita direta" (frame [12:33]) e que é "o marketplace mais difícil de operar" [09:49].
- **PBN**: usar diretório para passar autoridade aos próprios sites é esquema de links e viola as diretrizes de spam do Google. Há risco de penalização, e "site real" não elimina esse risco.
- **Termos do Google**: raspar o Google Maps (Outscraper ou a nossa própria raspagem) viola os Termos de Serviço do Google Maps/Places. Republicar avaliações e fotos em um diretório piora o problema (direito autoral dos autores das avaliações). Melhor usar dados factuais (nome, endereço, telefone, categoria) e conteúdo próprio.
- **LGPD**: dados de empresas são em geral de pessoa jurídica, mas MEIs e profissionais liberais costumam ter dados de pessoa física (nome, celular). Publicar isso num diretório e usar para prospecção exige base legal (legítimo interesse, com teste de balanceamento), opção de remoção/opt-out fácil e cuidado com mensagens em massa no WhatsApp. O WhatsApp também bane envio em massa não solicitado.
- **Enriquecimento por LLM**: atributos inferidos de avaliações podem estar errados ("tem estacionamento" quando não tem). Por isso o próprio método roda várias passadas e prevê revisão manual. Publicar atributo falso sobre uma empresa gera risco de reclamação.
- **Venda do "topo da lista"**: em diretório pago, o destaque precisa estar sinalizado como patrocinado (CDC, publicidade enganosa).
- **Transcrição de baixa qualidade**: alguns nomes e números ("modificadores de RH", "Claude Fable", "Month Directory", divisão dos US$ 250) estão incertos e foram marcados acima.
