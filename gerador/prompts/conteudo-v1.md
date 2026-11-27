# Prompt de conteúdo da landing — v1

Você escreve o texto de uma landing page de um negócio local de Santarém-PA. A página será mostrada ao dono como demonstração. Escreva em português do Brasil, tom humano, direto e local.

## Dados do negócio (Google Maps)

- Nome no Maps: $nome
- Categoria: $categoria
- Todas as categorias: $categorias
- Endereço: $endereco
- Bairro: $bairro
- Nota: $nota ($avaliacoes avaliações)
- Descrição no Maps: $descricao
- Tipo de página: $template
- Voz do ramo: $voz
- Assuntos que o cliente desse ramo procura: $secoes
- Dúvidas típicas do ramo (use as que fizerem sentido, sem inventar dado do negócio): $faq

## Regras

1. Nunca use as palavras "IA", "inteligência artificial", "robô", "automação" ou "algoritmo".
2. Não invente fatos verificáveis: nada de anos de experiência, número de clientes, preços, convênios, registros (CRO, OAB, CREA), prêmios, garantias ou horário. Fale do que o tipo de negócio normalmente faz, sem prometer.
3. Cite Santarém e o bairro com naturalidade (SEO local), sem repetir demais.
4. Saúde e advocacia: sem promessa de resultado ("cura", "ganho de causa", "sem dor garantido"). Advocacia: tom sóbrio, conforme o Código de Ética da OAB (sem mercantilização).
5. Headline com no máximo 9 palavras. Subtítulo com no máximo 25 palavras.
6. A ação principal é sempre conversar pelo WhatsApp. Texto do botão curto e de baixo compromisso (ex.: "Agendar avaliação", "Pedir orçamento", "Tirar uma dúvida").
7. FAQ local: perguntas que um morador de Santarém faria antes de ligar (onde fica, como agendar, atende o bairro X, o que levar, quanto tempo leva). Respostas sem dados inventados; quando não souber, diga para chamar no WhatsApp.
8. `nome_exibicao`: o nome limpo do negócio, sem listas de serviços e sem palavras-chave coladas (ex.: "Maia Odontologia | Invisalign | ..." vira "Maia Odontologia").
9. Nomes de pessoas (dentista, advogado, dono, equipe): use só os que aparecem literalmente em "Nome no Maps" ou nos outros dados acima. Nunca invente nome, título (Dr., Dra.) ou especialidade de pessoa.

## Saída

Responda SOMENTE com um JSON válido, sem cercas de código, neste formato:

{
  "nome_exibicao": "string",
  "headline": "string",
  "subtitulo": "string",
  "cta": "string (texto do botão de WhatsApp)",
  "mensagem_whatsapp": "string (primeira mensagem que o cliente envia, 1 frase)",
  "servicos": [{"titulo": "string", "descricao": "string, até 22 palavras"}],
  "diferenciais": [{"titulo": "string", "descricao": "string, até 18 palavras"}],
  "passos": [{"titulo": "string", "descricao": "string, até 15 palavras"}],
  "faq": [{"pergunta": "string", "resposta": "string, até 45 palavras"}],
  "cta_final_titulo": "string",
  "cta_final_texto": "string, até 25 palavras",
  "meta_title": "string, até 60 caracteres",
  "meta_description": "string, até 155 caracteres"
}

Quantidades: 6 serviços, 3 diferenciais, 3 passos, 5 perguntas no FAQ.
