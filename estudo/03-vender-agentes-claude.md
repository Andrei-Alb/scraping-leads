# Estudo 03 — "Build & Sell Claude AI Agents (2+ Hours Course, No code)"

Fonte: https://www.youtube.com/watch?v=kyngnLF27bw — Oliver Rasmussen (canal; se apresenta como "Oliver Alexander"/"Ollie"), publicado 2026-10-21, 2h01.
Legenda automática com ruído; valores em US$.

## 1. Resumo do vídeo

Compilado de vários vídeos do Oliver, dono de uma agência de IA na Dinamarca que diz ter vendido mais de US$ 1 milhão em IA (US$ 700 mil vindos de atendimento e vendas) [00:01][35:40]. Tese central: **ninguém quer comprar "IA", quer o resultado** (mais agendamentos, menos ligação perdida, mais avaliação no Google) [02:37][22:14][1:44:02]. O curso tem duas partes: (1) construir com Claude + skills, sem código, cinco agentes vendáveis — chatbot de WhatsApp para clínica, agente de e-mail "speed to lead", recepcionista de voz, agente de avaliações do Google e reativação de clientes — cada um com demo para a reunião de vendas, preço e jeito de oferecer; (2) conseguir clientes — oferta de entrada (site grátis), cold call, Google Ads Transparency, cold e-mail em escala, Instagram com carrosséis, roteiro da reunião de vendas e a "escada de upsell" que termina numa implantação de ~US$ 7 mil [01:04][1:52:13–2:00:58]. O produto todo é empacotado como skills reaproveitáveis (pesquisa → demo → agente → conversão para o GoHighLevel). Também existe um "Marcus Wright" na abertura [00:01] e trechos de convidados em podcasts.

## 2. Conhecimento extraído

### 2.1 Princípios gerais
- Agentes servem para o que você terceirizaria (call center) ou daria a um estagiário [00:01].
- Tudo é feito com Claude, mas independe do modelo (Codex ou qualquer outro) [00:33].
- Erro clássico: entrar na reunião e falar de tecnologia/chatbot. O dono quer pacientes, não IA [02:37][22:14]. No cold call, **"nunca dizemos IA"**: descreva o resultado, não a ferramenta [1:14:33].
- O "segredo" de fechar 8 de 10 reuniões é **levar uma demo personalizada do negócio** para a reunião [01:35][1:44:02].
- Responder lead na hora é o que todo negócio pode fazer e não faz por ser difícil; agora deixou de ser difícil [21:12].
- Caso contado: uma empresa convertia 55% dos leads (2 a 3 por dia) porque pagava US$ 60 mil/ano a uma tia cuja única função era largar tudo e ligar para o lead no instante em que ele chegava [35:10]. O agente faz isso por centavos [45:33].
- Estudo de Harvard citado: lead tem 21x mais chance de não converter se a resposta demora [1:40:27] (número sem fonte detalhada).

### 2.2 Agente 1 — chatbot de WhatsApp para clínica odontológica [01:35–21:12]
- **Cérebro = prompt em blocos** a partir de um template que já funciona, sem começar do zero [03:08]. Os dois blocos que fazem converter: **(1) fluxo de 3 perguntas** que leva o cliente à decisão e **(2) "sempre acolha o cliente primeiro"** (ex.: dor de dente → acolhe antes de perguntar e agendar) [03:40][04:10].
- Transformar o processo numa **skill** do Claude ("agent prompt builder") apontável para qualquer negócio ou nicho [04:40][05:12].
- **Demo com cara de WhatsApp de iPhone**: o Claude gera o front, a chave da API Anthropic fica no back (chave com validade de 1 dia, US$ 5 de crédito) e o site sobe de graça no Netlify [05:42–06:45]. Uma conversa inteira de teste custou 4 centavos [08:19].
- **Fluxo de agendamento universal**: o agente só coleta os dados e avisa que alguém vai ligar para confirmar. Serve para qualquer clínica ou loja, independentemente da agenda que ela usa [07:48].
- **Pesquisa automática do negócio com Firecrawl** (firecrawl.dev, "setup for agents", plano sem chave e sem conta para buscar/raspar/navegar) [08:51][09:21]. O resultado entrega os dados da empresa para o cérebro, o **CTA principal** do site (ex.: se o site usa formulário, o canal certo é WhatsApp/SMS), as perguntas que o próprio site já responde, um **briefing da reunião de vendas com 2 ou 3 dores** e uma **"pergunta de compromisso"** [09:53–10:57]. Para achar alvo: Google Maps → sua cidade → "dentists" → copiar o site [10:25].
- Vira também uma "research skill"; a demo personalizada não inventa nada e se limita aos dados da empresa [11:27][12:29].
- **Implantação no GoHighLevel (GHL)**: AI Agents → Conversation AI → bot em autopilot; o mesmo agente roda em WhatsApp, SMS, e-mail e redes sociais [15:02][15:33]. Ativar resposta a imagens e áudios, adicionar base de conhecimento e partir o prompt nos campos do GHL (personalidade, objetivo, informações adicionais) com uma skill "conversor de prompt para GHL" [16:03][16:35]. Para ir ao ar, o cliente precisa de WhatsApp Business ligado ao GHL [17:05]. Responde toda mensagem em até ~30 s [18:07].
- **Preço: por agendamento feito**, não retainer [18:37]. Justificativa: sem teto de receita, o cliente fica muito mais tempo e sente que paga pelo resultado, um ROI direto [18:37][19:08]. Todos os clientes que gastaram mais de US$ 2 mil com a agência têm esse modelo [02:06][18:37].
- **Cálculo do preço na reunião**: perguntar quanto pagam por lead e que % dos leads vira conversa ou agendamento (ex.: 30%). Custo por agendamento = custo do lead ÷ taxa (ex.: ÷ 0,3 → ~US$ 166). Confirmar com o cliente e cobrar um pouco menos, ~US$ 100 por agendamento; serviços caros (implante, Invisalign) têm preço próprio [19:08–20:10].
- Meta: 2 ou 3 clientes desses → US$ 12 mil/mês [20:10]. Entrada: mostrar a demo e oferecer implantação **grátis e 100% por desempenho**; depois dos resultados, vender o "sistema operacional de IA" completo por **US$ 7 a 8 mil** [20:10][20:42].

### 2.3 Agente 2 — e-mail "speed to lead" para clínica [21:12–35:10]
- Mesmo método: o cérebro é montado a partir do site (Firecrawl → preços, horários) com a skill "agent prompt builder" [22:44].
- Chave da API: pedir ao Claude para inserir a chave via terminal **sem vê-la** [23:16]. Ferramenta de ditado do autor: co-type.io (autopromoção) [23:48].
- Demo com cara de Gmail, publicada na Vercel [23:48][24:19]. Testes de "quebrar" o agente: preço da limpeza = US$ 120, igual ao site [24:49]. Testes completos custaram menos de US$ 1 [25:20].
- Formulário do site com **Web3Forms** (grátis até 250 envios/mês; a chave de acesso não é segredo) [26:22]. Promessa do site: "contato em até 5 minutos", inclusive fins de semana e fora do horário [25:52].
- **Roda 24/7 de graça com Google Apps Script** na conta Google do cliente, verificando a cada 1 minuto; chave Anthropic nas Script Properties; o Claude configura pelo Chrome [27:24][27:55].
- **Agendamento numa planilha Google** (data, nome, e-mail, telefone, horário pedido), universal para qualquer sistema; a clínica liga para confirmar [28:25][29:59][30:29]. Telefone virou campo obrigatório no formulário [28:56]. Primeira resposta em ~2 min [29:26].
- **Preço: US$ 500/mês**; instalação = 10 minutos de compartilhamento de tela; revisões nas 2 primeiras semanas [31:00]. Acompanhar de perto por 14 a 21 dias e seguir para o próximo cliente; oferta produtizada [32:35].
- **Porta de entrada: fazer antes um site melhor**, inspirado (via Firecrawl) nas maiores empresas do país, com formulário e promessa de 5 min [31:32]. Site: setup + SEO + hospedagem = **US$ 500/ano** [32:04].
- Conta para US$ 12 mil/mês: 20 clientes com speed to lead + 4 sites por mês, vindos de cross-sell, clientes novos, cold e-mail e anúncios oferecendo site grátis [31:32][32:04].
- **Fazer o dono aparecer na reunião (8 de 10 aparecem)** [13:00–14:31][33:05–34:39]:
  1. Não mandar a demo antes. Criar evento no Google Agenda ("Ollie & [clínica]") [13:00].
  2. 24 h antes (ou horas antes, se foi marcado para o mesmo dia): **ligar com uma "pergunta de pesquisa"** ("estou trabalhando no seu site/demo; qual produto ou serviço vocês mais vendem?") e confirmar "ainda está de pé amanhã?". Isso prova trabalho e ativa a reciprocidade [13:31][14:01][33:37]. Se a pessoa remarcar, a reunião foi salva [34:08].
  3. 2 h antes: SMS/e-mail "aviso rápido, nos vemos em 2 horas" [14:01][34:08].
  4. Na hora, se não entrou: e-mail "consegue entrar?", que gera notificação de que você está esperando [14:31][34:39].

### 2.4 Agente 3 — recepcionista de voz "Ashley" [35:40–49:41]
- Voz IA ficou boa o bastante (em 2023 não estava) e destrava negócios que faturam por telefone [36:10].
- Comparação de custo: recepcionista a US$ 3.200/mês por 40 h/semana contra Ashley a US$ 500/mês por 168 h/semana [36:41].
- Cérebro: converter o melhor prompt de chatbot em prompt de voz, mantendo os dois blocos de conversão [37:12]. Prompt de voz abaixo de **2.000 tokens** para responder rápido [37:43].
- Voz: **fish.audio** (8 mil créditos grátis pelo link, MCP e skills próprias para o Claude); o Claude cria o agente, escolhe voz, modo expressivo e velocidade [37:43–39:47]. Dá para clonar a voz do dono [40:50]. Chave de API guardada em variável de ambiente para ficar oculta das ferramentas [38:45].
- Base de conhecimento num `clinic.md` (endereço, preços como Invisalign de US$ 4.200 a 6.800 "o dentista confirma após exame") [42:58][43:28]. Aviso "chamadas podem ser gravadas" na saudação [42:58].
- Agendamento universal: Apps Script → planilha "Ashley Bookings" compartilhada com a clínica, que liga de manhã e de tarde para confirmar [44:00][45:02]. A extensão do Claude para Chrome faz a configuração [44:31].
- **Custo**: US$ 15/mês = 12 h de conversa; número de US$ 1 a 3/mês; ~2 centavos por chamada [45:33]. Número americano não importa: usa-se **desvio de chamada** do número local [46:04].
- Extras possíveis: remarcação, cancelamento, confirmação e lembrete por SMS [48:10].
- **Como vender**: **piloto de 2 semanas** só fora do horário e nas ligações que a recepção já perde; setup de **US$ 700 a 1.500** conforme o porte, **reembolso total em 14 dias**; depois mantém os US$ 700 e cobra **US$ 300 a 700/mês por unidade** conforme o volume de chamadas [48:10–48:41].
- Conta: 20 clínicas × US$ 500 = US$ 10 mil + 2 setups/mês × US$ 1 mil = US$ 12 mil; com upsell (site, avaliações) bastam metade ou um terço dos clientes [48:41][49:11].

### 2.5 Agente 4 — avaliações no Google + reativação (HVAC "PSC Cooling") [49:11–1:08:53]
- Volume de avaliações pesa mais que a nota perfeita; o mais avaliado recebe mais ligações (exemplo: 9 avaliações 5 estrelas contra concorrentes com mil) [49:11–50:11].
- O agente pede avaliação a clientes novos e antigos e depois volta aos satisfeitos oferecendo novos serviços [50:11].
- **Regra anti "review gating"**: o Google proíbe filtrar quem pode avaliar e, segundo o vídeo, removeu **292 milhões** de avaliações "gated" neste ano. Para 1 a 3 estrelas, a página diz "gostaria de te ligar antes de você avaliar", **mas mantém o link para avaliar** [50:43][51:44][53:49][54:49].
- Página de avaliação na Vercel com **link único por cliente** para rastrear quem avaliou; nota baixa → notificação ao dono com os dados do lead [54:19].
- **Workflows no GHL** [55:54–1:00:34]: tag "job complete" → espera 2 h → envia só em horário comercial (9h às 18h aprox., nunca domingo) → tag "review requested" → lembretes em 2 e 3 dias → ramos "rated happy" / "unhappy" / sem avaliação. Custom value com o link de avaliação e contact ID [57:27]; webhook do GHL como variável de ambiente na Vercel [58:29].
- **Reativação**: espera de 90 dias como regra geral; limpeza ~30 dias; controle de pragas ~90 dias; telhados 180 dias para inspeções [59:00]. Lista antiga importada com tag "past customer", enviada em lotes de 10 com intervalo [1:00:01]. Mensagem: "Oi [nome], é o Donald da PSC… vocês nos chamaram um tempo atrás…" [1:00:01].
- Agente conversacional no GHL via SMS, em autopilot, com o conversor de prompt; acolhe a nota baixa e já agenda novo serviço [1:00:34–1:03:09].
- **Achar 500 empresas iguais**: Firecrawl MCP (atualização "Alexandria") raspa o Google Maps e acha e-mails de donos → sheets.new → CSV → limpar nomes ("Air Masters AC" em vez de "LLC") para não parecer automático [1:03:40–1:04:43].
- **Cold e-mail desse nicho**: assunto = nome da empresa (maior taxa de abertura); corpo: "pensei em ligar, mas preferi mandar mensagem antes; vi que vocês têm 5 avaliações com nota 4, o que é bom, mas [concorrente] tem [N]. Aposto que seu trabalho é tão bom quanto… [mais avaliações] sem você precisar pedir. Se importa de dar uma olhada?" [1:05:14][1:05:45].
- **Oferta/preço**: agente de avaliações a **US$ 300/mês com garantia de reembolso de 30 dias sem perguntas** → na mesma reunião, upsell de **speed to lead a US$ 200** (pacote de US$ 500) → site novo de alta conversão por **US$ 500 de entrada** [1:06:17]. Margem de ~95% com o GHL grátis da comunidade; SMS de 1 a 3 centavos; número de poucos dólares por mês [1:06:17][1:06:48].
- **Por que retainer baixo**: retainers de US$ 2 a 5 mil são 10x mais difíceis de fechar e de manter (muitos cancelam no 1º mês ou em 6 meses); melhor produtizar uma oferta de US$ 300 para centenas de negócios do que brigar por 5 retainers de US$ 3 mil [1:07:19]. Cerca de 70% dos que entram por avaliações ou Google Ads sobem para o pacote de US$ 500 com speed to lead [1:07:51]. Meta: 20 clientes × US$ 500 + 4 sites/mês × US$ 500 [1:07:51]. O site é a porta de entrada antes do retainer, e a agência também precisa que o site converta para os serviços funcionarem [1:07:51][1:08:22]. Clientes ficam anos porque o preço é baixo e se paga com 1 ou 2 clientes extras [1:08:22].

### 2.6 As 3 ofertas para iniciantes e como achar o primeiro cliente [1:08:53–1:18:12]
- O autor passou um ano falhando (SMMA, grupos de Facebook) até o 1º mês de US$ 10 mil em 2024; diz que IA tem a menor curva de aprendizado [1:08:53][1:09:24].
- **Oferta 1 — site com IA** (Claude, ~20 min, plano grátis ou US$ 20/mês): **grátis para negócio local + US$ 29 a 49/mês de hospedagem**; para clientes maiores, US$ 500 a 2.000/mês com "proof of concept" (paga US$ 500 adiantado, reembolso se não gostar) [1:09:56].
- **Oferta 2 — recepcionista de voz** 24/7: US$ 300 a 700/mês conforme as chamadas; **US$ 500 a 3.500 adiantado**, entregue em 1 a 3 dias, reembolso se não gostar [1:09:56][1:10:28].
- **Oferta 3 — speed to lead** (retorno de ligação perdida por SMS, resposta imediata a lead de site ou anúncio): **US$ 20 a 45 por agendamento, zero adiantado**, "só paga quando ganhamos dinheiro para você" [1:10:28][1:10:58].
- **Recomendação: começar pelo site grátis**: muitos dizem sim, gera valor adiantado e abre upsell de voz e speed to lead [1:10:58].
- **Critério de lead**: nicho "gated" (ex.: remoção de entulho); empresas com **~50 avaliações no Google ou menos**, que costumam ter site ruim ou nenhum (ver ícone de site no Maps) [1:10:58][1:11:29]. Dado citado: EUA têm 33 milhões de pequenas empresas, 28% sem site (~9 milhões) [1:11:29][1:11:59].
- **Site em 8 min**: colar a URL do Google Maps da empresa + prompt (link na descrição) no Claude; pedir fotos melhores do nicho; baixar o HTML; subir no Netlify grátis como demo [1:11:59–1:13:31]. Vender a US$ 97/mês + US$ 500 de entrada [1:13:01].
- **Prospecção 1 — cold call** com lista raspada do Maps (data scraper → CSV) [1:13:31][1:14:02]. **Roteiro em 5 partes**: (1) "estou num projeto com empresas de HVAC em Seattle"; (2) sem pitch, perguntas que criam necessidade (quantas ligações perde por dia? vão para o concorrente?); (3) "não sei se faz sentido, mas se a gente atendesse todas e agendasse, ajudaria?"; (4) "manhã ou tarde é melhor?"; (5) marcar para 1 ou 2 dias depois. Nunca dizer IA. Taxa: ~1 reunião a cada 20 conversas [1:14:02][1:14:33].
- **Prospecção 2 — Google Ads Transparency Center** (adstransparency.google.com): país + nicho → quem está anunciando → clicar no anúncio → ligar dizendo "vi seu anúncio no Google" + mesmo roteiro [1:14:33][1:15:04].
- Antes de toda reunião, fazer uma demo rápida do negócio [1:15:35].
- **Perguntas de necessidade para voz** [1:16:06][1:16:36]: quantas ligações perde por dia (5) → valor médio do serviço (US$ 400) → % de quem atende que vira agendamento (30%) → quem não é atendido liga para o concorrente? → **perda de US$ 600/dia, US$ 18 mil/mês**, com o cliente confirmando cada número. Venda: US$ 3.500 adiantado + US$ 500/mês, que se paga em ~1 semana [1:16:36][1:17:09].
- Custos de ferramenta: Claude grátis para demos ou US$ 20/mês; GoHighLevel US$ 97 a 497/mês (plano de US$ 297 grátis na comunidade paga) [1:17:09][1:17:40].

### 2.7 Instagram com carrosséis (canal próprio de aquisição) [1:18:12–1:27:00]
- Um post com 122 comentários pedindo um recurso que é enviado automaticamente → funil. Instagram é a principal estratégia de crescimento, de onde vêm os "US$ 19 mil/mês" [1:18:44].
- Fluxo: Claude desktop → conector MCP do **Higgsfield** (gera imagens) + skill de carrossel com base num vídeo do YouTube/TikTok → identidade própria (ex.: verde = crescimento) [1:19:45–1:21:17].
- **Blotato** (US$ 29/mês, MCP) publica no Instagram e monta a automação de DM: comenta a palavra-chave → precisa seguir → recebe o recurso + link do grupo/desafio de 7 dias [1:21:50–1:22:52].
- Rotina diária no Claude às 7h: varre YouTube e Instagram em busca do que está viralizando, gera carrossel e um Google Doc como recurso [1:23:23][1:23:55].
- **Site + pagamento com "WAF"** (nome conforme a legenda): cria site com botão de reunião (iframe do Calendly) e, via MCP, gera **link de pagamento com BNPL** durante a reunião [1:24:26–1:25:58].
- Substitui um social media de US$ 3 a 4 mil/mês. Dá para vender a corretores, coaches etc. por **US$ 2 mil/mês**; 10 clientes = US$ 20 mil/mês [1:25:58][1:26:29][1:27:00].

### 2.8 Máquina de cold e-mail [1:27:31–1:43:00]
- Dois comandos ou skills no Claude Cowork; o autor diz ter feito mais de US$ 300 mil com cold e-mail desde ago/2024 [1:28:02].
- Stack: Claude (cérebro) + Gmail (infra) + **Instantly** (envio) [1:28:33]. **Nunca usar o domínio principal**; criar domínio parecido; contas pré-aquecidas evitam o aquecimento de 20 a 30 dias; 3 a 5 caixas por domínio; DNS e aquecimento automáticos [1:29:03–1:30:05]. Verificar no mxtoolbox.com (MX lookup) [1:30:35].
- Instantly via API key "all scopes" + MCP como conector personalizado; a 1ª skill aplica configurações de envio e aquecimento e checa DNS [1:31:38–1:32:40].
- **Campanha** ("dentistas em Miami – recepcionista de voz"): assunto = nome da empresa limpo → observação → cenário ideal → **reversão de risco** ("já construímos um exemplo, se importa de olhar?") com CTA de alta intenção e baixa pressão [1:33:10][1:33:42]; follow-up 2: cálculo de receita perdida da clínica [1:34:12]; follow-up 3: "conseguiu ver minha mensagem?"; último: "Hail Mary" com outra oferta [1:34:12].
- Envio das 7h às 16h no fuso do lead; sem rastreamento; só texto, sem HTML; limite diário = caixas × 20 [1:34:43][1:35:15].
- **Lista**: **Clay** → empresas até 200 funcionários (acima disso demora demais), cidade → "find people" → filtro com ~80 cargos do setor gerados pelo Claude → enriquecimento de e-mail em cascata (Hunter, Prospeo…) → 41 de 57 encontrados (~80%) [1:35:15–1:37:52]. Variante: importar do Google Maps pelo raio [1:38:22]. Ser local é vantagem [1:37:21].
- **Million Verifier** antes de subir: só "good"; bounce derruba a entregabilidade [1:38:22][1:38:53]. Mapear bem o campo de e-mail no CSV [1:39:23][1:39:55].
- **Agente de resposta do Instantly** em autopilot; o essencial é responder em ~5 min [1:40:27][1:40:58].
- **Escala**: 1 domínio = 5 caixas × 20 a 25/dia (25 depois de 2 a 3 meses); 10 domínios e 50 caixas = 1 mil/dia, 30 mil/mês; custo: US$ 250/mês das caixas + US$ 100 a 130/ano de domínios + US$ 300 a 350/mês de assinaturas [1:41:29][1:41:59][1:42:30].
- "Essa máquina marca reuniões, não fecha. IA não faz dinheiro; vendas fazem" [1:42:30].

### 2.9 Sistema de vendas, auditoria de IA e escada de upsell [1:43:00–2:00:58]
- Fecha 8 de 10 reuniões. Postura de **médico**: perguntar onde dói, o que já tentou, há quanto tempo, antes de receitar [1:44:02].
- **Auditoria de IA, 2 perguntas**: de onde vêm os clientes? o que acontece depois que o lead chega? [1:44:33]. Mapa dor → produto: perde ligação → voz ou "missed call text back"; responde mensagem devagar → agente de WhatsApp/redes/SMS; base grande parada → reativação [1:45:03]. **Corrigir primeiro o maior vazamento** [1:45:03].
- **"Calculadora de consequência"**: custo por lead ÷ taxa de contato. No caso real: US$ 30 por lead no Facebook com 12% de contato = **~US$ 300 por ligação**; proposta: US$ 60 a 70 por agendamento [1:45:34][1:46:04][1:53:45].
- **Arrancar o "não" antes do fechamento**: PME → "de 0 a 10, quanto você dá para isso?" → "o que faria virar 10?" → "se resolvermos, vira 10?" [1:46:04][1:46:35]. Empresa grande → **"o que faria isso ser um não?"**: tira objeções de stakeholders e contratos [1:46:35]. Antecipar oferecendo acordo de privacidade de dados (próprio ou o deles) [1:47:06].
- **Fechamento enterprise**: sem cartão na 1ª reunião; piloto pequeno, até 50% de desconto nos agendamentos, zero adiantado, operação manual primeiro (sem integração pesada) para lançar em dias [1:47:06–1:48:09]. **Nunca sair sem marcar a próxima reunião**, mesmo com pagamento: cria prazo e segura o onboarding [1:48:09][1:57:23].
- **Cartão salvo na reunião**: o Claude gera link de pagamento de US$ 1 para guardar o cartão e cobrar por desempenho; para US$ 1 mil de setup, **link BNPL** (você recebe à vista, o cliente parcela) [1:48:39][1:49:10]. O preço por agendamento vai no contrato, com cobrança semanal no cartão [1:49:10].
- **Reunião real** (empresa de energia solar/financiamento no Reino Unido, mais de 500 mil leads antigos) [1:49:41–1:59:25]: autoridade explicando o caso de outro cliente B2B [1:50:42]; leads vêm de Meta; call center próprio; 80% das vendas acontecem no mesmo dia [1:51:13][1:51:43]; exigir **time de vendas que ligue** para os agendamentos (~75% atendem) [1:52:13][1:52:43]; 10 mil ligações por semana com 12,23% de conversas de 1 minuto [1:53:14]; mensagem que não pareça automática, acolher tudo, "qualificador de interesse" [1:54:47][1:55:18]; caso de reativação de lead de 12 meses [1:55:50]; **teste de baixo volume de 1 a 2 mil leads em modo manual** [1:56:22]; cláusula de não compartilhar/vender leads sem autorização por escrito [1:56:52].
- **Escada de upsell** [1:59:25–2:00:58]: nunca se vende os US$ 7 mil de cara. (1) Auditoria → corrigir um vazamento (voz, reativação ou WhatsApp) → deixar a IA vender sozinha com agendamentos aparecendo → o cliente passa a perguntar "o que mais dá para fazer?" → (2) **implantação completa** (orçamentos, faturas, follow-ups, dashboards, assistente) com proof of concept: paga, você constrói e há **reembolso total em 7 dias** → um cliente de US$ 7 mil + mensalidades por cima.

## 3. Aplicação ao nosso negócio (Santarém)

### (a) Escolher leads na base (6.781 empresas, view `segmentos`)
- **Filtro "sem site ou site ruim + até ~50 avaliações"** [1:10:58][1:11:29]: aplicar direto nas colunas de presença online e número de avaliações. Priorizar quem tem telefone/WhatsApp e pouca avaliação. [INFERÊNCIA] Em Santarém o corte de 50 provavelmente deve ser menor (20 a 30), pelo volume baixo de avaliações local; checar a distribuição real na base.
- **Nichos de agendamento e ligação** (dentista, clínica, estética, oficina, ar-condicionado/refrigeração = HVAC, dedetização, limpeza): é onde o vídeo prova ROI [18:37][36:41][59:00].
- **Sinal de quem tem dinheiro**: quem anuncia no Google (Ads Transparency Center filtrado por Brasil e nicho) [1:14:33]. [INFERÊNCIA] Cruzar com a base e marcar "anuncia" como prioridade alta para o Agentic, porque já paga por lead.
- **Volume de avaliações versus concorrente do mesmo nicho e bairro**: a base já permite calcular, e é o gancho da abordagem [1:05:14].
- Limpar o nome da empresa (sem "LTDA", "ME", "EIRELI") antes de qualquer mensagem automatizada [1:04:43].

### (b) Montar a landing page
- **Pipeline do vídeo serve quase literalmente**: URL do Google Maps + prompt → Claude gera HTML → fotos do nicho → Netlify/Vercel como demo, ~8 min por site [1:11:59–1:13:31]. [INFERÊNCIA] Nossa base já tem os dados do Maps; dá para gerar a demo em lote, uma por lead priorizado.
- Pesquisa automática com Firecrawl para extrair o **CTA principal**, perguntas frequentes e dores, e copiar o padrão das maiores empresas do setor no Brasil [09:53][31:32].
- O site tem que **converter**: formulário + telefone obrigatório + promessa "respondemos em 5 minutos" [25:52][28:56]. [INFERÊNCIA] No Brasil o CTA dominante é botão de WhatsApp, não formulário.
- Formulário grátis com Web3Forms; agendamento simples numa planilha Google que o dono consulta [26:22][28:25].
- **Preço de referência** (adaptar ao real): site grátis + hospedagem mensal baixa (US$ 29 a 49) ou entrada de US$ 500 + US$ 97/mês [1:09:56][1:13:01]; setup + SEO + hospedagem a US$ 500/ano [32:04]. [INFERÊNCIA] Em Santarém, algo como R$ 0 de entrada + R$ 49 a 99/mês, ou R$ 500 a 1.000 de entrada, precisa ser validado em campo; o vídeo não fala de Brasil.

### (c) Abordar e vender
- **Levar a demo pronta com o site e os dados do próprio cliente** é o maior diferencial [01:35][1:15:35]. Mostrar na reunião, não mandar antes [13:00].
- **Roteiro de ligação em 5 partes, sem dizer "IA"** [1:14:02][1:14:33]; traduzir: "estou num projeto com clínicas aqui de Santarém…".
- **Perguntas de necessidade + conta na frente do dono** (ligações perdidas × ticket × conversão → R$ perdidos por mês, com ele confirmando cada número) [1:16:06][1:16:36].
- **Rotina anti-falta**: ligação de pesquisa 24 h antes, mensagem 2 h antes, "consegue entrar?" na hora [13:31–14:31][33:37–34:39]. [INFERÊNCIA] Fazer por WhatsApp, que é o canal real aqui.
- **0 a 10 → "o que faria virar 10?"** com PME; **"o que faria ser um não?"** com empresa maior [1:46:04][1:46:35].
- **Nunca sair sem a próxima reunião marcada** [1:48:09].
- **Oferta de entrada: site grátis ou baratíssimo com garantia**, depois upsell; e **retainer baixo e produtizado** em vez de contrato grande [1:07:19][1:10:58]. Bate com o plano de vender landing page primeiro.
- Cold e-mail: pouco útil para a base local [INFERÊNCIA] (PME de Santarém responde pouco e-mail); o que se aproveita é a estrutura da mensagem (observação concreta → cenário ideal → "já fiz um exemplo, posso mostrar?") para o primeiro contato por WhatsApp ou ligação [1:33:42].

### (d) Vender o Agentic
- **Empacotar como oferta produtizada** com módulos que se somam, como o vídeo faz [1:06:17][1:07:51]:
  1. Atendimento instantâneo no WhatsApp (acolher → 3 perguntas → coletar dados → humano confirma) [03:40][07:48].
  2. Retorno de ligação perdida por mensagem e/ou recepcionista de voz [1:10:28][36:41].
  3. Pedido de avaliação no Google sem gating + reativação de clientes antigos (90 dias de padrão) [54:49][59:00].
  4. "Mexe na landing page" (atualizar preço, horário, promoção a pedido do dono). [INFERÊNCIA] Esse é o diferencial nosso que não aparece no vídeo; vender como "você manda mensagem e o site muda".
- **Precificação aproveitável**:
  - Mensalidade baixa com entrada pequena e **garantia de reembolso** (14 dias no piloto, 30 dias no agente de avaliações, 7 dias na implantação completa) [48:10][1:06:17][2:00:27].
  - **Por resultado** (por agendamento), calculado pela fórmula **custo por lead ÷ taxa de conversão** e cobrando um pouco abaixo [19:08][1:45:34]. Só funciona com cliente que já paga anúncio e sabe o custo por lead. [INFERÊNCIA] Para a maioria das PMEs de Santarém sem anúncio, mensalidade fixa é mais simples.
  - **Piloto restrito** (só fora do horário ou só o que já se perde) reduz o risco percebido [48:10].
- **Escada**: site → 1 agente que estanca o maior vazamento → deixar os resultados aparecerem → "Agentic completo" (orçamento, follow-up, faturas, dashboard) [1:59:25–2:00:27].
- **Infra barata do vídeo** (Apps Script grátis, planilha como agenda universal, mensagens a centavos) sustenta mensalidade baixa com margem alta [27:24][45:33][1:06:48].
- **Fazer skills reaproveitáveis** (pesquisa do negócio → prompt do agente → demo → conversão para a plataforma) para produzir a demo em minutos por lead [20:42].
- **Exigir do cliente quem confirme os agendamentos**; o agente só coleta, o humano confirma [44:00][1:52:13].

### O que NÃO serve ou não se aplica
- **Valores em dólar** (US$ 500/mês, US$ 3.500 de setup, US$ 7 mil de implantação, US$ 12 mil/mês) são do mercado americano/europeu; não converter direto para Santarém. [INFERÊNCIA] O ticket local deve ser uma fração disso.
- **Números americanos e desvio para número dos EUA** [46:04]: aqui o canal é WhatsApp; voz com número estrangeiro tende a não funcionar bem para PME local. [INFERÊNCIA]
- **SMS** como canal principal de reativação e avaliação: no Brasil quase todo mundo responde no WhatsApp; SMS tem baixa resposta. [INFERÊNCIA]
- **Clay + cold e-mail em escala** (1 mil e-mails/dia, 50 caixas): exagero para 6.781 empresas locais, e a base já está raspada. [INFERÊNCIA]
- **GoHighLevel** (US$ 97 a 497/mês): caro para começar; os próprios caminhos baratos do vídeo (Apps Script, planilha) bastam no início [27:24][1:17:40].
- **Venda enterprise com cartão de US$ 1 e cobrança semanal automática por desempenho** [1:48:39][1:49:10]: depende de cartão de crédito salvo e contrato. [INFERÊNCIA] Aqui Pix ou boleto recorrente é mais realista.
- **Instagram com carrosséis** [1:18:12]: serve para a nossa marca, não para o cliente PME local, pelo menos por enquanto.

## 4. Riscos e ressalvas

- **Números de autoridade sem prova**: "US$ 1 milhão vendido", "8 de 10 fechamentos", "80% comparecem", "US$ 19 mil/mês", "70% sobem de plano", "Harvard 21x", "292 milhões de avaliações removidas" [00:01][1:18:44][1:07:51][1:40:27][54:49] são falados, não demonstrados. O vídeo é funil para a comunidade paga "1%", o GoHighLevel por afiliado, links de afiliado (Fish, Blotato com cupom, Firecrawl) e o produto do próprio autor (co-type.io) [15:02][23:48][38:14][1:21:50]. Tratar como hipótese a testar.
- **"Site em 8 minutos" e "agente em 10 minutos"**: demo é diferente de produção; o próprio autor admite de 14 a 21 dias de ajustes por cliente [31:00][32:35].
- **Termos do Google**:
  - Review gating é proibido; o vídeo mostra o jeito "permitido" (oferecer ligação, mas manter o link para todas as notas) [51:44][53:49]. [INFERÊNCIA] Mesmo assim, o pedido de contato antes da avaliação pode ser lido como desestímulo; manter o link visível e igual para qualquer nota. Também não oferecer incentivo em troca de avaliação.
  - Raspar Google Maps (Firecrawl, data scraper) e usar Google Ads Transparency para prospectar [1:03:40][1:14:02][1:14:33]: raspar o Maps viola os termos da plataforma. [INFERÊNCIA] Nossa base já foi raspada; usar os dados para contato comercial pontual, sem republicar conteúdo do Google.
- **LGPD** [INFERÊNCIA salvo o indicado]:
  - Prospecção B2B por telefone ou WhatsApp usando dado público de empresa cabe em **legítimo interesse**, desde que haja identificação, opt-out fácil e nada de spam em massa. Cold e-mail ou WhatsApp em massa pode violar os termos do WhatsApp Business (risco de banimento do número) e incomodar.
  - Os agentes tratam **dados de clientes do nosso cliente**, inclusive **dado de saúde** (dor de dente, procedimento) [04:10][1:01:36], que é dado sensível na LGPD: exige contrato de operador, finalidade definida, segurança e retenção mínima. A planilha compartilhada com "qualquer pessoa com o link pode editar" [45:02] é um vazamento esperando acontecer; restringir aos e-mails do cliente.
  - Reativação de clientes antigos do cliente [1:00:01] exige base legal (relação anterior) e opt-out; enviar em lotes, como o vídeo já faz.
  - Gravação de chamada: avisar no início, como no vídeo [42:58].
  - O vídeo já indica oferecer acordo de privacidade e cláusula de não uso dos leads [1:47:06][1:56:52]; incluir isso no nosso contrato.
- **Agente de saúde**: a IA não pode diagnosticar; o vídeo mantém "não sei dizer daqui, vale ver com o doutor" e "preço confirmado após exame" [24:49][43:28]. Manter essas travas e as regras do conselho profissional (CFO/CFM) sobre publicidade de preço e procedimento. [INFERÊNCIA]
- **Chaves de API**: o vídeo põe a chave Anthropic no front da demo e no Apps Script do cliente [06:13][27:55]. Usar sempre chave com validade curta e limite de gasto na demo; em produção, a chave fica no servidor, nunca no HTML.
- **Cobrança por desempenho**: precisa de definição contratual clara do que é "agendamento" (com ou sem comparecimento), senão vira briga. O vídeo põe o preço no contrato [1:49:10]. BNPL e cartão salvo são figuras do mercado de lá. [INFERÊNCIA]
- **Dependência de plataforma**: GHL, Instantly, Fish e Blotato são SaaS pagos e mudam preço e termos; a "infra grátis" (Apps Script, Netlify, Web3Forms com 250 envios/mês) tem limites de cota [26:22].
