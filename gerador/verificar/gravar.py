# /// script
# dependencies = ["playwright>=1.58"]
# ///
"""Rola a página devagar, quadro a quadro, e monta um mp4 (30 fps) com o ffmpeg do sistema.
Uso: gravar.py <index.html> <destino.mp4> <largura> <altura>. Caminhos viram absolutos (o file:// exige)."""
import os, sys, json, subprocess, tempfile, pathlib
from playwright.sync_api import sync_playwright
# Sem CHROME, usa o Chromium do Playwright (`uvx playwright install chromium`).
CHROME = os.environ.get("CHROME") or None
arq, destino, w, h = str(pathlib.Path(sys.argv[1]).resolve()), str(pathlib.Path(sys.argv[2]).resolve()), int(sys.argv[3]), int(sys.argv[4])
movel = w < 500
# Tablet não é "mobile" no Chrome, mas é toque: gravar sem toque esconde o comportamento real do dedo.
toque = w <= 1366
tmp = pathlib.Path(tempfile.mkdtemp())
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME)
    pg = b.new_page(viewport={"width": w, "height": h}, is_mobile=movel, has_touch=toque, device_scale_factor=1)
    erros = []; pg.on("pageerror", lambda e: erros.append(str(e)))
    pg.goto("file://" + arq, wait_until="networkidle")
    n = 0
    def quadro():
        global n; pg.screenshot(path=tmp / f"{n:05d}.jpg", type="jpeg", quality=80); n += 1
    for _ in range(36): pg.wait_for_timeout(33); quadro()   # entrada do hero
    total = pg.evaluate("document.documentElement.scrollHeight - innerHeight")
    # Velocidade constante (~420 px/s): o pin horizontal e a pilha alongam a página e precisam de tempo de tela.
    passos = max(240, int(total / 14))
    for i in range(passos + 1):
        k = i / passos; e = 2*k*k if k < .5 else 1 - (-2*k+2)**2/2
        pg.evaluate(f"scrollTo(0,{total*e})"); pg.wait_for_timeout(30); quadro()
    for _ in range(20): pg.wait_for_timeout(33); quadro()
    lateral = pg.evaluate("document.documentElement.scrollWidth > innerWidth")
    b.close()
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "30", "-i", str(tmp / "%05d.jpg"),
                "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "28", destino], check=True)
print(json.dumps({"erros": erros, "lateral": lateral, "quadros": n}))
