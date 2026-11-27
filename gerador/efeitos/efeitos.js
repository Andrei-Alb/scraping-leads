/* Motor dos efeitos: um único laço rAF passivo escreve --p (0..1) em cada [data-efeito] perto da tela.
   O CSS decide o que fazer com --p. Com prefers-reduced-motion nada liga e a página fica no estado final. */
(() => {
  const raiz = document.documentElement;
  if (matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  raiz.classList.add("ef-vivo");
  const nativo = (t) => CSS.supports(`animation-timeline: ${t}`);
  const todos = [...document.querySelectorAll("[data-efeito]")];
  raiz.dataset.efeitos = [...new Set(todos.map((e) => e.dataset.efeito))].join(" ");
  const limita = (v) => (v < 0 ? 0 : v > 1 ? 1 : v);
  const de = (nome) => todos.filter((e) => e.dataset.efeito === nome);

  // revela: quebra só os nós de texto, mantendo a marcação de dentro (ênfase, links).
  for (const el of de("revela")) {
    let i = 0;
    const nos = [];
    const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    for (let n; (n = w.nextNode());) nos.push(n);
    for (const n of nos) {
      const partes = n.textContent.split(/(\s+)/);
      const frag = document.createDocumentFragment();
      for (const p of partes) {
        if (!p) continue;
        if (/^\s+$/.test(p)) { frag.append(p); continue; }
        const s = document.createElement("span");
        s.className = "ef-pal";
        s.style.setProperty("--i", i++);
        s.textContent = p;
        frag.append(s);
      }
      n.replaceWith(frag);
    }
    el.style.setProperty("--n", i);
  }

  // horizontal: a altura da seção é a distância que o trilho anda + uma tela; medida de novo no resize.
  const trilhos = de("horizontal").map((sec) => ({ sec, t: sec.querySelector(".ef-trilho"), d: 0 }));
  const mede = () => {
    for (const h of trilhos) {
      h.d = Math.max(0, h.t.scrollWidth - innerWidth);
      h.sec.style.height = `${h.d + innerHeight}px`;
    }
  };

  // contagem: sobe do zero até o número real que já está no texto, uma vez, quando entra na tela.
  const conta = new IntersectionObserver((vistos) => {
    for (const v of vistos) {
      if (!v.isIntersecting) continue;
      conta.unobserve(v.target);
      const el = v.target, final = el.textContent.trim();
      const alvo = parseFloat(final.replace(/\./g, "").replace(",", "."));
      const casas = (final.split(",")[1] || "").length;
      if (!isFinite(alvo)) continue;
      const t0 = performance.now(), dur = 1100;
      const passo = (t) => {
        const k = limita((t - t0) / dur), e = 1 - (1 - k) ** 3;
        el.textContent = k < 1 ? (alvo * e).toLocaleString("pt-BR", { minimumFractionDigits: casas, maximumFractionDigits: casas }) : final;
        if (k < 1) requestAnimationFrame(passo);
      };
      requestAnimationFrame(passo);
    }
  }, { threshold: 0.6 });
  de("contagem").forEach((el) => conta.observe(el));

  // magnético: só com ponteiro fino; no toque o botão não pode fugir do dedo.
  if (matchMedia("(hover: hover) and (pointer: fine)").matches) {
    for (const b of de("magnetico")) {
      b.addEventListener("pointermove", (e) => {
        const r = b.getBoundingClientRect();
        b.style.setProperty("--mx", `${((e.clientX - r.left) / r.width - 0.5) * 12}px`);
        b.style.setProperty("--my", `${((e.clientY - r.top) / r.height - 0.5) * 10}px`);
      });
      b.addEventListener("pointerleave", () => { b.style.removeProperty("--mx"); b.style.removeProperty("--my"); });
    }
  }

  const barras = nativo("scroll()") ? [] : de("progresso");
  const vistas = todos.filter((e) => ["parallax", "revela", "marquee", "cor"].includes(e.dataset.efeito)
    || (e.dataset.efeito === "zoom" && !nativo("view()")));
  const pilhas = de("pilha").map((p) => [...p.querySelectorAll(".ef-carta")]);

  const quadro = () => {
    pend = false;
    const vh = innerHeight;
    for (const b of barras) {
      const max = raiz.scrollHeight - vh;
      b.style.setProperty("--p", max > 0 ? (scrollY / max).toFixed(4) : 0);
    }
    for (const el of vistas) {
      const r = el.getBoundingClientRect();
      if (r.bottom < -vh || r.top > 2 * vh) continue;
      const p = limita((vh - r.top) / (vh + r.height));
      el.style.setProperty("--p", p.toFixed(4));
      if (el.dataset.efeito === "cor") el.classList.toggle("ef-virou", p > 0.3 && p < 0.85);
    }
    for (const h of trilhos) {
      const r = h.sec.getBoundingClientRect();
      if (r.bottom < 0 || r.top > vh) continue;
      const p = h.d ? limita(-r.top / h.d) : 0;
      h.t.style.transform = `translate3d(${(-p * h.d).toFixed(1)}px,0,0)`;
    }
    // Cada carta apaga nos 80 px antes de a seguinte alcançar o fim do texto dela: nunca há texto sobre texto.
    for (const cartas of pilhas) {
      cartas.forEach((c, i) => {
        const prox = cartas[i + 1];
        if (!prox) return;
        const fim = c.lastElementChild.getBoundingClientRect().bottom;
        const q = limita((fim + 80 - prox.getBoundingClientRect().top) / 80);
        c.style.setProperty("--q", q.toFixed(3));
      });
    }
  };
  let pend = false;
  const pede = () => { if (!pend) { pend = true; requestAnimationFrame(quadro); } };
  mede();
  quadro();
  addEventListener("scroll", pede, { passive: true });
  addEventListener("resize", () => { mede(); pede(); });
  // As fontes chegam depois e mudam a largura do trilho.
  document.fonts?.ready.then(() => { mede(); pede(); });
})();
