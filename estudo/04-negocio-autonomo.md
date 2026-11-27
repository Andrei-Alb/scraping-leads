# Estudo 04 — "Grok Bot just built me an autonomous business..." (Alex Finn)

Fonte: https://www.youtube.com/watch?v=lmYLF3keVmw (20:35, publicado 2026-10-13). O OCR dos frames quase não tem texto útil; o estudo se baseia na transcrição.

## 1. Resumo do vídeo

Alex Finn (criador de conteúdo sobre IA, diz ter ~500 mil seguidores no X e uma newsletter com 40 mil inscritos) defende que a métrica que mais vai importar nos próximos 5 anos é a **"agentic income"**: renda gerada por negócios que um agente de IA administra sozinho. Ele mostra o próprio caso, o agentusecases.ai, um diretório de casos de uso de agentes de IA que o bot dele ("Milo", no GrokBot) criou, monetiza com patrocínios e mantém (SEO, otimização para chatbots, newsletter diária). Depois ele refaz o processo ao vivo com um bot novo ("Timothy"). O bot escolhe a ideia (diretório de ferramentas de IA para vibe coders), publica a primeira versão ("Build Stack") em uns 2 minutos, cria rotinas diárias e semanais e liga os conectores Vercel, GitHub, Resend e Stripe. Segundo ele, sobrou só um moat: **distribuição** (audiência no X). O vídeo não é patrocinado, mas é bem promocional e sem números auditáveis.

## 2. Conhecimento extraído

### Tese e números do caso
- [00:00] "Agentic income" é apresentada como a métrica mais importante da vida da pessoa daqui a 5 anos. O negócio seria tocado por um agente de IA.
- [00:33] A página do Stripe mostra **US$ 1.100 no último dia**. Em [04:16] ele diz que os 1.100 vieram de **2 patrocínios**.
- [00:33] O agentusecases.ai é um diretório de use cases de agentes (MetaMuse, GrokBot, Claude Code, Hermes Agent). O bot raspa a internet atrás de casos de uso.
- [01:09] O bot procura casos novos o tempo todo e atualiza o site para **SEO** e para **"chatbot optimization"**, ou seja, para ChatGPT e Claude recomendarem o site.
- [01:09] Tráfego: **56.000 visitantes em "alguns dias", 123.000 views**. As fontes citadas são Google, Facebook, Bing e LinkedIn.
- [01:40] Funciona com qualquer agente (Muse, ChatGPT, Dots, Hermes). Ele usa o GrokBot porque o acha o melhor, sem patrocínio.

### Passo 1: criar o bot "CEO"
- [02:11] O bot "Milo" age como CEO e avisa sobre novos patrocinadores, por exemplo a **Lasso Finance, que pagou US$ 600**. Também manda analytics, melhorias que está construindo e receita.
- [02:41] Crie um perfil/bot dedicado ao negócio, com categoria própria, um nome e o **papel de "CEO do seu negócio agêntico"**. Prompt usado: "Your name is Timothy, and I want you to be the CEO of a new agentic business".

### Passo 2: escolher a ideia
- [03:13] Os melhores negócios resolvem um problema. O agentusecases resolve o "não sei o que fazer com agentes de IA".
- [03:45] Ele se baseou nos próprios vídeos de melhor desempenho (listas "top 5 use cases"). A regra é resolver problemas de jeito simples, com **micro-negócios** que o agente consiga tocar sozinho.
- [03:45–04:16] Prompt: "I want you to design, build, and run an autonomous business for me. Let's first come up with the idea. I want this to be very simple problem my audience might have. I'm into [interesses]. What are some very simple challenges we can solve?"
- [05:17–06:25] Seis ideias propostas pelo bot (as citadas):
  1. app vibe-coded quebrado: a pessoa cola o erro ou o repo e recebe a correção em inglês simples, paga pela correção;
  2. "construí algo e ninguém sabe que existe": um agente escreve posts de lançamento para o X;
  3. "qual ferramenta de IA usar": ranking semanal de ferramentas, que pode começar como newsletter paga;
  4. templates prontos de agente (triagem de e-mail, pesquisa de leads) vendidos como downloads baratos.
- [05:50] Diretórios são "super bons para SEO" e para "AI SEO".
- [06:55] Escolhida: diretório de ferramentas de IA por caso de uso, mais vitrine de lançamentos. Ele libera a ideia para quem quiser copiar.

### Passo 3: monetização e construção
- [07:26] Proposta do bot: listar ferramentas por caso de uso ("best for X") com um veredito curto e escaneável. A receita vem de **listagens em destaque pagas pelos fabricantes**. Segundo ele, ferramentas de IA pagam caro por patrocínio porque é a única forma de conseguir distribuição.
- [07:57] Público escolhido: vibe coders e builders. O bot oferece as opções pesquisar concorrentes, escolher nome ou construir. A escolha foi **"bias for action"**: construir logo e não perder tempo com o nome.
- [08:27] O build usa **Cursor cloud agents** integrados. A primeira versão ficou no ar em **~2 minutos**.
- [09:02] A primeira versão tinha **33 ferramentas reais** por categoria e já incluía lançamentos do dia. O visual "não é o mais bonito". Ele diz que o bot set up representa "90% do trabalho manual".
- [04:16–04:47] No agentusecases, os patrocinadores clicam em "sponsor us", aparecem num ticker do site e ganham o logo na **newsletter (~2.000 inscritos)**.

### Passo 4: rotinas autônomas (expectativas para o CEO)
- [09:37–10:08] Lista do que o bot dele mantém: monetizar quando fizer sentido, otimizar SEO, otimizar para chatbots, criar e manter a newsletter (o ponto que ele considera mais valioso, porque a lista de e-mails é fácil de monetizar), acompanhar feedback no X e caçar bugs.
- [10:40] Prompt: "You are going to be the autonomous CEO for this micro business. Here is everything I want you to work on and maintain..." e em seguida a lista colada.
- [11:12] Rotinas criadas pelo bot: **todo dia às 7:52 PT** adicionar novos lançamentos, checar bugs, varrer feedback no X e fazer **uma melhoria de SEO**, mensagem só se algo importar. **Toda segunda às 9:17** vai um resumo de progresso. Também foram criados o básico de SEO, uma **página que chatbots conseguem ler e citar** e o cadastro da newsletter.
- [11:44] Salvaguarda do próprio bot: "antes de qualquer coisa sair para pessoas (newsletter, pagamentos de sponsor), checo com você".

### Passo 5: conectores (stack)
- [12:48–13:19] **Vercel** para hospedagem (dá para usar de graça).
- [13:19] **GitHub** para o código. O bot dá push e abre PRs.
- [13:19–14:00] **Resend** é o e-mail programático: coleta inscritos e manda a newsletter diária. Rastreia opens e clicks e já insere o patrocinador da semana.
- [16:05–16:36] **Stripe** para pagamentos. O bot cria o **payment link** e o coloca na área de patrocínio.
- [18:21] O bot pede um nome real, um e-mail de contato e uma conexão ao **Google Search Console**.

### Distribuição
- [14:31–15:02] "Software está morrendo" (cita a facilidade de copiar software e o "Reverse Engineer Everything"). O moat que resta é **distribuição**.
- [15:02–15:33] Ele diz que dá para fazer com uns 50 seguidores. O canal mais fácil seria o **X**: crie a conta, responda pessoas e poste **2x por dia**. Ele começou assim há ~5 anos e diz ter chegado a ~500 mil. A ideia é postar com constância e, de vez em quando, fazer um plug do negócio.

### Visão de vida
- [17:48] Ter **3 a 4 negócios agênticos, cada um com 10–20K** (não diz moeda nem período; o contexto sugere USD/mês [INFERÊNCIA]) para viver disso.
- [18:52–19:23] "Deixe o bot ir": ele faz check-ins com perguntas de múltipla escolha. Entrar cedo seria mais lucrativo.

## 3. Aplicação ao nosso negócio

### (a) Escolher leads na base
- O vídeo não fala de prospecção. O que dá para tirar é o critério de "problema simples e com dor clara" [03:45]. Na view `segmentos`, priorizar quem **não tem site** ou depende só do Instagram/WhatsApp. [INFERÊNCIA]
- A tese do diretório [05:50, 07:26] sugere um ativo próprio: **um diretório local "Santarém"** (ex.: "melhores dentistas/oficinas de Santarém") alimentado pelas 6.781 empresas, otimizado para Google e chatbots, com **destaque pago** para as empresas. A mesma página vira vitrine para a venda da landing page: "seu perfil está aqui, quer um site completo?" [INFERÊNCIA]

### (b) Montar a landing page
- Stack citada e barata: **Vercel (free) + GitHub + Resend + Stripe**, com o agente dando push e PR [13:19–16:36]. Serve como template por cliente.
- "Bias for action": primeira versão em minutos, polimento depois [07:57–09:02]. Dá para gerar a landing do lead **antes** da abordagem e mostrar pronta. [INFERÊNCIA]
- Itens que valem para toda landing: SEO básico, **página legível/citável por chatbots** (dados estruturados, FAQ, horário, endereço), Search Console [11:12, 18:21]. Num mercado local, "ChatGPT recomendar a loja" é argumento novo. [INFERÊNCIA]

### (c) Abordar e vender
- A distribuição é o moat [15:02]. Para nós, o canal não é o X: é **WhatsApp e Instagram local**, e o "X" do vídeo não se aplica a Santarém. [INFERÊNCIA]
- Modelo de receita recorrente por patrocínio/destaque [07:26]. Aqui ele vira **mensalidade** (hospedagem + manutenção + destaque no diretório), com cobrança por link de pagamento. No Brasil o natural seria **Pix** (Stripe/Mercado Pago/Asaas) em vez de cartão. [INFERÊNCIA]

### (d) Vender o Agentic
- O vídeo é praticamente o roteiro do produto: um **agente "gerente" por cliente** com rotinas fixas [11:12]. Por exemplo: todo dia ver avaliações e mensagens e fazer uma melhoria de SEO; toda segunda mandar ao dono um resumo curto pelo WhatsApp; só incomodar quando algo importa.
- A salvaguarda de **aprovar antes de publicar ou cobrar** [11:44] deve ser regra de produto, porque o dono local não aceita "o robô postou sozinho". [INFERÊNCIA]
- O check-in por múltipla escolha [04:47, 18:52] é a UX certa para dono sem tempo: responder "A/B" no WhatsApp. [INFERÊNCIA]
- A newsletter vira **lista de clientes/WhatsApp da empresa** com promoções semanais geradas pelo agente, respeitando opt-in. [INFERÊNCIA]

### O que NÃO serve
- **Patrocínio de empresas de IA**: o mercado dele é global, de tech, com gente pagando US$ 600 por logo. O comércio de Santarém não paga isso. O preço local tem de ser outro. [INFERÊNCIA]
- **X como canal**: pouca relevância para o público local. [INFERÊNCIA]
- **"Zero trabalho"**: o caso dele depende de uma audiência de 500 mil, que não temos. O tráfego de 56 mil visitas não se reproduz sem isso.
- Tudo em inglês, com horários PT e público de vibe coders: só aproveita o método.

## 4. Riscos e ressalvas

- **Números não verificáveis**: os US$ 1.100 vêm de 2 patrocínios pontuais, não de receita recorrente. O tráfego provavelmente veio da audiência dele [INFERÊNCIA]. O "zero trabalho" contradiz os passos manuais (conectores, aprovações, tweets).
- **Promessa exagerada**: "software is dead" e "3–4 negócios de 10–20K" são opinião sem prova. Não repetir isso para cliente.
- **LGPD**: newsletter ou lista de contatos exige consentimento (opt-in), finalidade e descadastro. Montar diretório com dados de empresas (Google Maps) envolve dados de PJ, mas telefone/nome de MEI/autônomo pode ser dado pessoal. Usar só o necessário e honrar pedidos de remoção. [INFERÊNCIA]
- **Termos do Google**: o raspador e a republicação de conteúdo do Maps (avaliações, fotos) num diretório podem violar os Termos do Google Maps Platform. Usar só dados factuais e conteúdo próprio. SEO automatizado em massa ou páginas pouco úteis correm risco de "scaled content abuse" nas políticas de spam do Google. [INFERÊNCIA]
- **"Destaque pago"** em diretório precisa estar sinalizado como patrocinado (CDC, transparência publicitária). [INFERÊNCIA]
- **Agente autônomo publicando ou cobrando** pode errar preço, horário ou promessa em nome do cliente. É preciso aprovação humana e log. O próprio bot do vídeo pede aprovação [11:44].
- **Cobrança automática**: links de pagamento gerados por agente exigem controle de quem pode criar e alterar cobranças. Nunca deixar chaves expostas.
- **Dependência de fornecedor**: GrokBot, Cursor, Vercel e Resend podem mudar preço ou termos. Plano gratuito da Vercel tem restrição de uso comercial no Hobby [INFERÊNCIA: verificar os termos atuais].
