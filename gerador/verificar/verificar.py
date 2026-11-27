#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["playwright>=1.58"]
# ///
"""Verifica as landings geradas no celular (320, 375), tablet (768x1024, 1024x768) e desktop (1280, 1920),
rolando a página inteira. Celular e tablet vêm primeiro e rodam com toque ligado.

Falha (saída 1) se encontrar:
- texto sobreposto: caixas de linha de elementos de texto diferentes se cruzando;
- palavra quebrada: uma palavra que ocupa mais de uma linha (quebra no meio ou no hífen);
- rolagem lateral: a página rola para o lado, ou texto visível sai da tela fora do trilho horizontal;
- alvo de toque menor que 48 px (celular e tablet);
- botão ou link coberto por elemento fixo/sticky com a página parada no topo, no fim, ou com contato/mapa/rodapé na tela;
- texto de corpo (p, li, dd, td, summary, blockquote) menor que 16 px;
- página com endereço (schema.org `address`) e sem mapa do Google embutido;
- tarefa longa (> 50 ms, PerformanceObserver 'longtask') durante a rolagem: efeito travando o scroll;
- efeito que não desliga com prefers-reduced-motion (o motor não pode marcar html.ef-vivo);
- na galeria: template com menos de 3 efeitos de rolagem ([data-efeito]) ou duas assinaturas iguais.

Texto dentro de [aria-hidden="true"] é decoração e fica de fora. A barra fixa do celular também.
Na regra dos 16 px ficam de fora `.rotulo` (sobretítulo em caixa alta) e `small` (legenda dentro de botão).

Uso: `uv run gerador/verificar/verificar.py [pasta/index.html ...]` (padrão: todas em gerador/saida/).
Navegador: Chromium do Playwright (`uvx playwright install chromium`) ou CHROME=<executável>.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

# (largura, altura, toque)
TELAS = [(375, 812, True), (320, 640, True), (768, 1024, True), (1024, 768, True), (1280, 900, False), (1920, 1080, False)]
SAIDA = Path(__file__).resolve().parent.parent / "saida"
# Magnético reage ao mouse, não à rolagem: não conta para o mínimo de 3.
SO_MOUSE = {"magnetico"}

# Registra tarefas longas desde o carregamento; a regra só olha as que começam depois do início da rolagem.
LONGAS = """window.__longas = [];
try { new PerformanceObserver((l) => { for (const e of l.getEntries()) window.__longas.push([e.startTime, e.duration]); })
  .observe({ type: "longtask", buffered: true }); } catch (e) {}"""
ASSINATURA = """() => [...new Set([...document.querySelectorAll("[data-efeito]")].map((e) => e.dataset.efeito))].sort()"""

# Roda uma vez por tela, no documento inteiro: regras que não dependem da posição de rolagem.
ESTATICO = r"""
(toque) => {
  const problemas = [];
  const fora = (el) => el.closest('[aria-hidden="true"],script,style,noscript,details:not([open])>p');
  const mostra = (el) => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0 && getComputedStyle(el).visibility !== "hidden"; };
  const nome = (el) => el.tagName.toLowerCase() + (typeof el.className === "string" && el.className.trim() ? "." + el.className.trim().split(/\s+/).join(".") : "");
  const txt = (el) => el.textContent.trim().replace(/\s+/g, " ").slice(0, 30);
  if (toque) for (const el of document.querySelectorAll('a[href],button,summary,input,select,textarea,[role="button"]')) {
    if (fora(el) || !mostra(el)) continue;
    const r = el.getBoundingClientRect();
    if (r.width < 47.5 || r.height < 47.5) problemas.push(`alvo de toque ${Math.round(r.width)}x${Math.round(r.height)}: "${txt(el)}" em ${nome(el)}`);
  }
  for (const el of document.querySelectorAll("p,li,dd,td,summary,blockquote")) {
    if (fora(el) || el.closest(".rotulo") || !mostra(el)) continue;
    const proprio = [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim());
    const fs = parseFloat(getComputedStyle(el).fontSize);
    if (proprio && fs < 15.5) problemas.push(`fonte de corpo ${fs}px: "${txt(el)}" em ${nome(el)}`);
  }
  const ld = [...document.querySelectorAll('script[type="application/ld+json"]')].map((s) => s.textContent).join(" ");
  if (/"address"/.test(ld) && !document.querySelector('iframe[src*="google.com/maps"]')) problemas.push("tem endereço e não tem mapa");
  return problemas;
}
"""

# Roda dentro da página. Devolve os problemas vistos na posição de rolagem atual.
COLETAR = r"""
(checarPalavras) => {
  const vw = innerWidth, vh = innerHeight, problemas = [];
  const pulado = (el) => el.closest('[aria-hidden="true"],script,style,noscript,.barra-fixa,details:not([open])>p');
  function visivel(el) {
    let op = 1;
    for (let e = el; e && e.nodeType === 1; e = e.parentElement) {
      const cs = getComputedStyle(e);
      if (cs.visibility === "hidden" || cs.display === "none") return 0;
      op *= +cs.opacity;
    }
    return op;
  }
  // Recorta a caixa pelos ancestrais com overflow != visible (o que fica escondido não pode sobrepor nada).
  function recorte(el, r) {
    let [l, t, rr, b] = [r.left, r.top, r.right, r.bottom];
    for (let e = el.parentElement; e && e !== document.body; e = e.parentElement) {
      const cs = getComputedStyle(e);
      if (cs.overflowX !== "visible" || cs.overflowY !== "visible") {
        const c = e.getBoundingClientRect();
        if (cs.overflowX !== "visible") { l = Math.max(l, c.left); rr = Math.min(rr, c.right); }
        if (cs.overflowY !== "visible") { t = Math.max(t, c.top); b = Math.min(b, c.bottom); }
      }
    }
    return { l, t, r: rr, b };
  }
  const nome = (el) => (el.tagName.toLowerCase() + (el.className && typeof el.className === "string" ? "." + el.className.trim().split(/\s+/).join(".") : ""));
  const caixas = [];
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  for (let n; (n = w.nextNode());) {
    const txt = n.textContent;
    if (!txt.trim()) continue;
    const el = n.parentElement;
    if (!el || pulado(el)) continue;
    const op = visivel(el);
    if (op < 0.15) continue;
    const rg = document.createRange();
    rg.selectNodeContents(n);
    for (const r of rg.getClientRects()) {
      if (r.width < 2 || r.height < 2) continue;
      const c = recorte(el, r);
      if (c.r - c.l < 2 || c.b - c.t < 2) continue;  // escondido pelo recorte
      if (c.b < 0 || c.t > vh) continue;              // fora da tela na vertical
      // Texto visível saindo da tela pelo lado (o trilho horizontal é recortado pelo palco, então não cai aqui).
      if (c.l < -1 || c.r > vw + 1) problemas.push(`fora da tela: "${txt.trim().slice(0, 40)}" em ${nome(el)} (${Math.round(c.l)}..${Math.round(c.r)} de ${vw})`);
      caixas.push({ el, txt: txt.trim().slice(0, 40), ...c, h: r.height });
    }
    if (checarPalavras) {
      // Palavra que ocupa duas linhas = quebrou no meio ou no hífen.
      const re = /\S{2,}/g;
      for (let m; (m = re.exec(txt));) {
        rg.setStart(n, m.index); rg.setEnd(n, m.index + m[0].length);
        const tops = new Set([...rg.getClientRects()].filter((r) => r.width > 0.5).map((r) => Math.round(r.top)));
        if (tops.size > 1) problemas.push(`palavra quebrada: "${m[0]}" em ${nome(el)}`);
      }
    }
  }
  for (let i = 0; i < caixas.length; i++) for (let j = i + 1; j < caixas.length; j++) {
    const a = caixas[i], b = caixas[j];
    if (a.el === b.el || a.el.contains(b.el) || b.el.contains(a.el)) continue;
    const ix = Math.min(a.r, b.r) - Math.max(a.l, b.l), iy = Math.min(a.b, b.b) - Math.max(a.t, b.t);
    // Caixa de linha é mais alta que as letras; só conta cruzamento real (>25% da linha menor).
    if (ix > 3 && iy > 0.25 * Math.min(a.h, b.h)) problemas.push(`sobreposto: "${a.txt}" (${nome(a.el)}) x "${b.txt}" (${nome(b.el)})`);
  }
  if (document.documentElement.scrollWidth > vw + 1 || scrollX > 0) problemas.push(`rolagem lateral: scrollWidth ${document.documentElement.scrollWidth} > ${vw}`);
  return problemas;
}
"""

# Fixo (ou sticky) cobrindo botão/link. O que só passa por baixo durante a rolagem é normal; o defeito é o alvo
# coberto onde a pessoa para para tocar: página no topo (metade de cima), no fim, e com contato/mapa/rodapé
# na tela (metade de baixo, onde fica o contato fixo do polegar).
COBERTO = r"""
(metade) => {
  const vh = innerHeight, problemas = [];
  const preso = (el) => { for (let a = el; a && a !== document.body; a = a.parentElement) { const p = getComputedStyle(a).position; if (p === "fixed" || p === "sticky") return a; } return null; };
  const nome = (el) => (el.tagName.toLowerCase() + (el.className && typeof el.className === "string" ? "." + el.className.trim().split(/\s+/).join(".") : ""));
  for (const el of document.querySelectorAll('a[href],button,summary,input,select,textarea,[role="button"]')) {
    if (preso(el)) continue;
    const r = el.getBoundingClientRect();
    if (r.width < 2 || r.height < 2 || r.bottom <= 0 || r.top >= vh) continue;
    const cy = Math.min(Math.max((r.top + r.bottom) / 2, 1), vh - 1);
    if (metade === "alto" ? cy > vh / 2 : cy < vh / 2) continue;
    for (const [x, y] of [[(r.left + r.right) / 2, cy], [r.left + 4, cy], [r.right - 4, cy]]) {
      const hit = document.elementFromPoint(x, y);
      const fixo = hit && !el.contains(hit) && preso(hit);
      if (fixo && !fixo.contains(el)) { problemas.push(`coberto por fixo: "${(el.textContent || el.getAttribute("aria-label") || "").trim().slice(0, 40)}" (${nome(el)}) sob ${nome(fixo)}`); break; }
    }
  }
  return problemas;
}
"""
ZONA = """() => [...document.querySelectorAll('#contato, #chegar, [aria-labelledby="contato-t"], footer')]
  .some((z) => { const r = z.getBoundingClientRect(); return r.bottom > 0 && r.top < innerHeight; })"""


def verificar(pg, arquivo: Path, largura: int, altura_tela: int, toque: bool) -> list[str]:
    pg.set_viewport_size({"width": largura, "height": altura_tela})
    pg.goto(arquivo.as_uri(), wait_until="networkidle")
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(1400)  # entrada do hero e contadores terminam
    vistos: dict[str, None] = dict.fromkeys(pg.evaluate(ESTATICO, toque) + pg.evaluate(COBERTO, "alto"))
    inicio = pg.evaluate("performance.now()")
    altura = pg.evaluate("document.documentElement.scrollHeight")
    passo = int(pg.viewport_size["height"] * 0.6)
    y, primeiro = 0, True
    while y <= altura:
        pg.evaluate(f"scrollTo(0, {y})")
        pg.wait_for_timeout(350)  # rAF do movimento + transições curtas (a etiqueta do 08 recolhe em .3s)
        cobertos = pg.evaluate(COBERTO, "baixo") if pg.evaluate(ZONA) else []
        for p in pg.evaluate(COLETAR, primeiro) + cobertos:
            vistos.setdefault(f"y={y}: {p}" if not p.startswith("palavra") else p)
        primeiro = False
        y += passo
        altura = pg.evaluate("document.documentElement.scrollHeight")
    pg.evaluate("scrollTo(0, document.documentElement.scrollHeight)")
    pg.wait_for_timeout(400)  # etiquetas/barras que reagem ao fim da página terminam a transição
    vistos.update(dict.fromkeys(f"fim: {p}" for p in pg.evaluate(COBERTO, "baixo")))
    for t, dur in pg.evaluate("window.__longas"):
        if t >= inicio:
            vistos.setdefault(f"rolagem travou: tarefa longa de {round(dur)} ms")
    return list(vistos)


def sem_movimento(nav, arquivo: Path) -> list[str]:
    """Com prefers-reduced-motion o motor não pode ligar (a página fica no estado final, parada)."""
    ctx = nav.new_context(reduced_motion="reduce")
    pg = ctx.new_page()
    pg.goto(arquivo.as_uri(), wait_until="networkidle")
    vivo = pg.evaluate("document.documentElement.classList.contains('ef-vivo')")
    ctx.close()
    return ["prefers-reduced-motion: efeitos continuam ligados"] if vivo else []


def main() -> None:
    arquivos = [Path(a).resolve() for a in sys.argv[1:]] or sorted(SAIDA.glob("*/index.html"))
    if not arquivos:
        sys.exit("Nenhuma página em gerador/saida/. Rode o gerador antes.")
    falhas = 0
    assinaturas: dict[tuple[str, ...], Path] = {}
    with sync_playwright() as p:
        nav = p.chromium.launch(executable_path=os.environ.get("CHROME") or None)
        for arq in arquivos:
            for larg, alt, toque in TELAS:
                ctx = nav.new_context(is_mobile=toque and larg < 700, has_touch=toque)
                ctx.add_init_script(LONGAS)
                pg = ctx.new_page()
                erros: list[str] = []
                pg.on("pageerror", lambda e: erros.append(f"erro de JS: {e}"))
                problemas = erros + verificar(pg, arq, larg, alt, toque)
                if larg == TELAS[0][0]:
                    problemas += sem_movimento(nav, arq)
                    efeitos = pg.evaluate(ASSINATURA)
                    rolagem = tuple(e for e in efeitos if e not in SO_MOUSE)
                    print(f"       {arq.parent.name[:14]} efeitos: {', '.join(efeitos) or 'nenhum'}")
                    if arq.parent.parent.name == "galeria":
                        if len(rolagem) < 3:
                            problemas.append(f"só {len(rolagem)} efeitos de rolagem (mínimo 3)")
                        if rolagem in assinaturas:
                            problemas.append(f"assinatura igual à de {assinaturas[rolagem].parent.name}")
                        assinaturas.setdefault(rolagem, arq)
                ctx.close()
                rotulo = f"{arq.parent.name[:14]} {larg:>4}x{alt}"
                if problemas:
                    falhas += 1
                    print(f"FALHOU {rotulo}")
                    for linha in problemas[:12]:
                        print(f"   - {linha}")
                    if len(problemas) > 12:
                        print(f"   … mais {len(problemas) - 12}")
                else:
                    print(f"ok     {rotulo}")
        nav.close()
    print(f"\n{len(arquivos) * len(TELAS) - falhas}/{len(arquivos) * len(TELAS)} combinações sem problema")
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()
