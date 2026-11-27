# Catálogo de efeitos de rolagem

`efeitos.css` + `efeitos.js` entram inline em cada página por `_blocos.html.j2` (`ef.estilo()` no `<head>`, `ef.motor()` antes do `</body>`).
Sem CDN e sem GSAP: um laço `requestAnimationFrame` passivo escreve `--p` (0..1) em cada `[data-efeito]` perto da tela e o CSS decide o resto.
Com `prefers-reduced-motion: reduce` o motor não liga (`html.ef-vivo` nunca entra) e tudo fica no estado final, legível.

Cada efeito marca o elemento com `data-efeito="<nome>"`; o verificador conta por esse atributo.

| Efeito | O que faz | Só entra quando |
|---|---|---|
| `horizontal` | Seção fixada (pin); os cards de serviço correm para o lado com a rolagem vertical | 4+ serviços |
| `parallax` | Foto do negócio e formas em camadas, cada uma numa velocidade | há foto real (thumbnail do Google) |
| `zoom` | Foto abre do recorte (`clip-path`) e desfaz o zoom ao rolar | há foto real |
| `revela` | Texto acende palavra a palavra conforme atravessa a tela | sempre |
| `pilha` | Passos em cartas que grudam (sticky) e se empilham | 3+ passos |
| `progresso` | Barra de progresso de leitura no topo | sempre |
| `contagem` | Nota e nº de avaliações sobem do zero até o valor real | há nota do Google |
| `marquee` | Faixa de avaliações escritas do Google | 3+ avaliações com texto; nunca em advocacia (OAB, Provimento 205/2021) |
| `cor` | Faixa que troca de cor enquanto passa | há diferenciais |
| `magnetico` | Botão principal segue o mouse com profundidade (não conta como efeito de rolagem) | sempre (só com mouse) |

## Assinatura de cada template

Fonte: `ASSINATURAS` em `gerar.py`. O que a página recebe = assinatura ∩ o que os dados sustentam ∩ escolha da receita (`efeitos:` no YAML; lista vazia = nenhum).

| Template | Efeitos de rolagem | Extra |
|---|---|---|
| 01 Revista | revela, zoom, progresso, contagem | magnetico |
| 02 | horizontal, marquee, cor, contagem | magnetico |
| 03 | pilha, cor, progresso, contagem | |
| 04 Noite | parallax, revela, contagem, marquee | |
| 05 | parallax, pilha, marquee | magnetico |
| 06 | horizontal, zoom, contagem, progresso | |
| 07 Capítulos | revela, pilha, cor, progresso | |
| 08 | horizontal, parallax, marquee, zoom | magnetico |

O horizontal fica no 02, 06 e 08; o parallax no 04, 05 e 08. Nenhuma combinação se repete.
O tema do segmento só troca cor, fonte e texto (variáveis `--ef-*`); nunca liga, desliga ou move efeito.
