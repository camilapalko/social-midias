"""Layouts aprovados da Cookies Land (1080x1350 JPEG).

Uso:
    from layouts import *
    slides = [capa("minha_foto", "Sobretítulo", "Título", 0, 5), ...]
    render({"01": slides}, saida="out")   # gera out/01_01.jpg, out/01_02.jpg...

As fotos são lidas de prep/<nome>.jpg (ou .png para recortes) dentro desta pasta.
Copie as fotos do banco para prep/ antes de renderizar.
"""
import pathlib, json
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).parent

CSS = """
@font-face{font-family:Quicksand;font-weight:600;src:url(quicksand-latin-600-normal.woff2)}
@font-face{font-family:Quicksand;font-weight:700;src:url(quicksand-latin-700-normal.woff2)}
@font-face{font-family:Nunito;font-weight:400;src:url(nunito-latin-400-normal.woff2)}
@font-face{font-family:Nunito;font-weight:700;src:url(nunito-latin-700-normal.woff2)}
@font-face{font-family:Sacramento;src:url(sacramento-latin-400-normal.woff2)}
:root{--rosa:#FFE9F7;--rosaT:255,233,247;--creme:#F5E6D3;--cremeT:245,230,211;--borda:#EBD3DF;
--cacau:#857055;--esc:#5A4636;--manteiga:#F8D080;--pessego:#F2B08C;--pforte:#D9825A}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
body{font-family:Nunito;color:var(--esc);background:var(--rosa);position:relative}
body.creme{background:var(--creme)}
.bg{position:absolute;inset:0;background-size:cover;background-repeat:no-repeat}
.fade{position:absolute;left:0;right:0;bottom:0}
.sobre{font-family:Quicksand;font-weight:700;font-size:28px;letter-spacing:.18em;text-transform:uppercase;color:var(--pforte)}
.tit{font-family:Quicksand;font-weight:700;font-size:74px;line-height:1.02;color:var(--esc);letter-spacing:-.01em}
.tit.m{font-size:62px}
.corpo{font-size:46px;line-height:1.3;color:var(--esc)}
.txt{position:absolute;left:72px;right:72px;bottom:150px}
.num{font-family:Quicksand;font-weight:700;color:var(--pessego)}
.selo{position:absolute;top:48px;right:48px;width:124px;height:124px;border-radius:50%;background:var(--rosa);display:flex;align-items:center;justify-content:center}
.selo img{width:84px}
.dots{position:absolute;bottom:40px;left:72px;display:flex;gap:10px}
.dots i{width:12px;height:12px;border-radius:50%;background:var(--cacau);opacity:.25}
.dots i.on{opacity:.9;width:34px;border-radius:6px}
.spark{position:absolute}
.tag{display:inline-block;font-family:Quicksand;font-weight:700;font-size:30px;padding:6px 22px;border-radius:40px;background:var(--manteiga)}
ul.l{list-style:none}
ul.l{font-size:50px}
ul.l li{font-size:inherit;line-height:1.28;padding:0 0 36px 50px;position:relative}
ul.l li:before{content:"";position:absolute;left:0;top:24px;width:16px;height:16px;border-radius:50%;background:var(--pessego)}
table{border-collapse:collapse;width:100%}
td{font-size:40px;padding:14px 0;border-bottom:2px solid var(--borda)}
td.p{text-align:right;font-family:Quicksand;font-weight:700;white-space:nowrap}
"""

def spark(x, y, s=56, c="#F8D080"):
    return (f'<svg class="spark" style="left:{x}px;top:{y}px" width="{s}" height="{s}" viewBox="0 0 40 40">'
            f'<path d="M20 2 C22 14 26 18 38 20 C26 22 22 26 20 38 C18 26 14 22 2 20 C14 18 18 14 20 2Z" '
            f'fill="{c}" stroke="#857055" stroke-width="1.6" stroke-linejoin="round"/></svg>')

def page(body, cls=""):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{cls}">{body}</body></html>'

def dots(i, n):
    return '<div class="dots">' + "".join(f'<i class="{"on" if k == i else ""}"></i>' for k in range(n)) + '</div>' if n > 1 else ""

def fade(h, rgb="var(--rosaT)"):
    return (f'<div class="fade" style="height:{h}px;background:linear-gradient(to top, rgba({rgb},1) 0%, '
            f'rgba({rgb},1) 38%, rgba({rgb},.75) 58%, rgba({rgb},0) 100%)"></div>')

LOGO_COR = '<img src="prep/logo-t.png" style="position:absolute;right:60px;bottom:30px;width:130px;opacity:.75">'
LOGO_COR_TOPO = '<img src="prep/logo-t.png" style="position:absolute;right:60px;top:60px;width:150px;opacity:.75">'
SELO = '<img src="prep/logo-t.png" style="position:absolute;right:56px;top:48px;width:230px;opacity:.72;filter:drop-shadow(0 0 16px rgba(255,255,255,.85))">'

# ---------- layouts ----------
CORES = {"rosa": ("255,233,247", "#5A4636", "#D9825A"), "creme": ("245,230,211", "#5A4636", "#D9825A"),
         "cacau": ("90,70,54", "#FFF6EC", "#F8D080")}

def capa(foto, sobre, titulo, i=0, n=1, pos="center 30%", h=640, cor="rosa"):
    """Foto sangrada, degradê na cor escolhida embaixo, título grande."""
    rgb, txt, sob = CORES[cor]
    return page(f'''<div class="bg" style="background-image:url(prep/{foto}.jpg);background-position:{pos}"></div>
      {fade(h, rgb)}{LOGO_COR}
      <div class="txt"><div class="sobre" style="color:{sob}">{sobre}</div><div class="tit" style="margin-top:14px;color:{txt}">{titulo}</div></div>
      <style>.dots i{{background:{txt}}}</style>{dots(i,n)}''')

def fato(foto, numeral, titulo, texto, i, n, pos="center 30%", h=620, topo=False, sobre=None):
    """Foto sangrada com fato numerado sobre o degradê (embaixo ou em cima)."""
    sob = sobre if sobre else f'<span class="num">{numeral}</span> &nbsp;de 3'
    if topo:
        fd = (f'<div class="fade" style="top:0;bottom:auto;height:{h}px;background:linear-gradient(to bottom, rgba(245,230,211,1) 0%, '
              f'rgba(245,230,211,1) 38%, rgba(245,230,211,.75) 58%, rgba(245,230,211,0) 100%)"></div>')
        txt = f'<div style="position:absolute;left:72px;right:240px;top:90px">'
        fd += LOGO_COR_TOPO
    else:
        fd = fade(h, "var(--cremeT)") + LOGO_COR; txt = '<div class="txt">'
    return page(f'''<div class="bg" style="background-image:url(prep/{foto}.jpg);background-position:{pos}"></div>
      {fd}{txt}<div class="sobre">{sob}</div>
        <div class="tit m" style="margin-top:12px">{titulo}</div>
        <div class="corpo" style="margin-top:16px">{texto}</div></div>
      {dots(i,n)}''')

def cta(frase, i, n, sub="link na bio"):
    """Fechamento: logo, com carinho e uma frase curta."""
    return page(f'''{spark(150,250,64)}{spark(860,300,48,"#F2B08C")}
      <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:0 110px">
        <img src="prep/logo-t.png" style="width:540px;opacity:.72">
        <div style="font-family:Sacramento;font-size:92px;color:var(--cacau);line-height:1;margin-top:18px">com carinho</div>
        <div style="font-family:Quicksand;font-weight:700;font-size:50px;margin-top:70px;text-align:center">{frase}</div>
        <div class="sobre" style="margin-top:14px">{sub}</div>
      </div>{dots(i,n)}''')

def vidro(foto, titulo, sub, i=0, n=1, pos="center"):
    """Foto inteira com cartão rosa translúcido no centro."""
    return page(f'''<div class="bg" style="background-image:url(prep/{foto}.jpg);background-position:{pos}"></div>
      <div style="position:absolute;left:100px;right:100px;top:50%;transform:translateY(-50%);background:rgba(255,233,247,.86);backdrop-filter:blur(10px);border-radius:40px;padding:64px 60px;text-align:center">
        <div class="tit" style="font-size:70px">{titulo}</div>
        <div style="width:90px;height:2px;background:var(--cacau);margin:30px auto 24px;opacity:.5"></div>
        <div class="corpo" style="font-size:44px">{sub}</div>
      </div><img src="prep/logo-t.png" style="position:absolute;right:50px;top:46px;width:180px;opacity:.72;filter:drop-shadow(0 0 14px rgba(255,255,255,.85))">{dots(i,n)}''')

def moldura(cut, titulo, sub, i=0, n=1):
    """Fundo com ondas da marca, moldura recortada e produto sem fundo."""
    ondas = '''<svg style="position:absolute;inset:0" width="1080" height="1350" viewBox="0 0 1080 1350">
      <path d="M0 180 C 200 80 360 300 560 200 S 900 60 1080 160 L1080 0 L0 0Z" fill="#FBDDEE"/>
      <path d="M0 1350 L0 1080 C 220 980 380 1200 600 1100 S 920 980 1080 1060 L1080 1350Z" fill="#FBDDEE"/>
      <path d="M-20 300 C 160 220 300 420 520 330" fill="none" stroke="#F8D080" stroke-width="16" stroke-linecap="round"/>
      <path d="M600 1010 C 780 930 920 1060 1100 990" fill="none" stroke="#F2B08C" stroke-width="16" stroke-linecap="round"/></svg>'''
    fest = '<div style="position:absolute;left:150px;right:150px;top:150px;height:980px;background:#F5E6D3;border:3px solid #857055;border-radius:390px 390px 48px 48px"></div>'
    return page(f'''{ondas}{fest}
      <img src="prep/symbol.png" style="position:absolute;left:50%;transform:translateX(-50%);top:210px;width:120px">
      <div style="position:absolute;left:210px;right:210px;top:370px;text-align:center">
        <div class="tit m">{titulo}</div>
        <div class="corpo" style="font-size:42px;margin-top:18px">{sub}</div></div>
      <img src="prep/{cut}.png" style="position:absolute;left:50%;transform:translateX(-50%);bottom:-60px;width:760px;filter:drop-shadow(0 24px 30px rgba(90,70,54,.28))">
      {dots(i,n)}''')

def cheio(foto, sobre, titulo, pos="center"):
    """Foto já com fundo rosa (produto recortado no enquadramento original), título no topo."""
    return page(f'''<div class="bg" style="background-image:url(prep/{foto}.jpg);background-position:{pos}"></div>
      {spark(900,110,64)}
      <div style="position:absolute;left:72px;right:220px;top:90px"><div class="sobre">{sobre}</div>
        <div class="tit" style="margin-top:12px">{titulo}</div></div>''')

def recorte(img, sobre, titulo, i=0, n=1, largura=820, fundo=150):
    """Produto sem fundo sobre o rosa, título no topo, marca d'água no canto."""
    return page(f'''<img src="prep/logo-t.png" style="position:absolute;right:56px;top:56px;width:200px;opacity:.6">
      <div style="position:absolute;left:72px;right:280px;top:90px"><div class="sobre">{sobre}</div>
        <div class="tit" style="margin-top:12px">{titulo}</div></div>
      <div style="position:absolute;left:50%;transform:translateX(-50%);bottom:{fundo-30}px;width:{int(largura*0.8)}px;height:70px;border-radius:50%;background:rgba(90,70,54,.22);filter:blur(22px)"></div>
      <img src="prep/{img}.png" style="position:absolute;left:50%;transform:translateX(-50%);bottom:{fundo}px;width:{largura}px">
      {dots(i,n)}''')

def colagem(f1, f2, titulo, texto, i, n, p1="center", p2="center"):
    """Duas fotos lado a lado, texto embaixo."""
    return page(f'''<div class="bg" style="right:50%;bottom:440px;margin-right:6px;background-image:url(prep/{f1}.jpg);background-position:{p1}"></div>
      <div class="bg" style="left:50%;bottom:440px;margin-left:6px;background-image:url(prep/{f2}.jpg);background-position:{p2}"></div>
      <div style="position:absolute;left:72px;right:72px;top:975px"><div class="tit m">{titulo}</div>
        <div class="corpo" style="margin-top:16px">{texto}</div></div>
      {dots(i,n)}''', "creme")

def prazos(foto, titulo, linhas, nota, i, n, pos="center", fh=420):
    rows = "".join(f'<tr><td style="font-size:44px;padding:20px 0">{a}</td><td class="p" style="font-size:44px;padding:20px 0">{b}</td></tr>' for a, b in linhas)
    if foto:
        topo = f'''<div class="bg" style="height:{fh+120}px;background-image:url(prep/{foto}.jpg);background-position:{pos}"></div>
      <div class="fade" style="bottom:auto;top:{fh-180}px;height:300px;background:linear-gradient(to bottom, rgba(245,230,211,0), rgba(245,230,211,1) 70%)"></div>'''
    else:
        topo = f'{spark(880,120,72)}{spark(980,240,46,"#F2B08C")}' + '<img src="prep/logo-t.png" style="position:absolute;right:56px;bottom:56px;width:170px;opacity:.6">'
        fh = 170
    return page(f'''{topo}
      <div style="position:absolute;left:72px;right:72px;top:{fh}px"><div class="sobre">Como pedir</div>
        <div class="tit" style="font-size:68px;margin:12px 0 30px">{titulo}</div><table>{rows}</table>
        <div class="corpo" style="font-size:36px;margin-top:30px;color:var(--cacau)">{nota}</div></div>
      {dots(i,n)}''', "creme")

def lista(foto, sobre, titulo, itens, i, n, pos="center", fh=520, fs=None, cls="creme"):
    lis = "".join(f"<li>{t}</li>" for t in itens)
    rgb = "245,230,211" if cls == "creme" else "255,233,247"
    return page(f'''<div class="bg" style="height:{fh+120}px;background-image:url(prep/{foto}.jpg);background-position:{pos}"></div>
      <div class="fade" style="bottom:auto;top:{fh-200}px;height:320px;background:linear-gradient(to bottom, rgba({rgb},0), rgba({rgb},1) 70%)"></div>
      <div style="position:absolute;left:72px;right:72px;top:{fh}px"><div class="sobre">{sobre}</div>
        <div class="tit m" style="margin:10px 0 36px">{titulo}</div><ul class="l" style="{f'font-size:{fs}px' if fs else ''}">{lis}</ul></div>
      {LOGO_COR}{dots(i,n)}''', cls)

ICON = {
 "pix": '<path d="M24 6 L42 24 L24 42 L6 24 Z M16 24 L24 16 L32 24 L24 32 Z"/>',
 "cartao": '<rect x="5" y="11" width="38" height="26" rx="5"/><path d="M5 19 H43 M11 30 H20"/>',
 "retirada": '<path d="M8 20 L24 8 L40 20 V40 H8 Z"/><path d="M19 40 V28 H29 V40"/>',
 "entrega": '<path d="M4 14 H28 V33 H4 Z M28 20 H37 L44 27 V33 H28"/><circle cx="13" cy="36" r="4"/><circle cx="36" cy="36" r="4"/>',
 "troca": '<path d="M8 20 A16 16 0 0 1 38 14"/><path d="M38 6 V14 H30"/><path d="M40 28 A16 16 0 0 1 10 34"/><path d="M10 42 V34 H18"/>',
 "selo": '<circle cx="24" cy="20" r="13"/><path d="M18 20 L22 24 L30 16"/><path d="M16 31 L12 44 L18 41 L22 46 L24 33 M32 31 L36 44 L30 41 L26 46 L24 33"/>',
 "app": '<rect x="13" y="4" width="22" height="40" rx="5"/><path d="M21 38 H27"/><path d="M24 14 C19 14 18 18 18 20 C18 25 24 30 24 30 C24 30 30 25 30 20 C30 18 29 14 24 14 Z"/>',
}
def pagamento(titulo, itens, i, n, cls="rosa", sobre="Pagamento e retirada", selo=False, fs=40, nota=""):
    """Card só de texto com ícones de traço fino da marca."""
    rows = ""
    for ic, txt in itens:
        rows += (f'<div style="display:flex;gap:30px;align-items:center;margin-bottom:28px">'
                 f'<div style="flex:none;width:104px;height:104px;border-radius:50%;background:#FBDDEE;display:flex;align-items:center;justify-content:center">'
                 f'<svg width="56" height="56" viewBox="0 0 48 48" fill="none" stroke="#857055" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">{ICON[ic]}</svg></div>'
                 f'<div style="font-size:{fs}px;line-height:1.28">{txt}</div></div>')
    deco = ('<svg style="position:absolute;left:50%;transform:translateX(-50%);bottom:110px" width="250" height="250" viewBox="0 0 48 48" fill="#FBDDEE" stroke="#857055" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round">'
            '<path d="M24 3 L28 7 L33.5 6 L35 11.5 L40.5 13 L39.5 18.5 L43.5 22.5 L39.5 26.5 L40.5 32 L35 33.5 L33.5 39 L28 38 L24 42 L20 38 L14.5 39 L13 33.5 L7.5 32 L8.5 26.5 L4.5 22.5 L8.5 18.5 L7.5 13 L13 11.5 L14.5 6 L20 7 Z"/>'
            '<path d="M17 22.5 L22 27.5 L31.5 18" fill="none" stroke-width="2.4"/></svg>') if selo else f'{spark(880,120,72)}{spark(980,240,46,"#F2B08C")}'
    return page(f'''{deco}
      <div style="position:absolute;left:72px;right:72px;top:{110 if nota else 150}px"><div class="sobre">{sobre}</div>
        <div class="tit" style="font-size:68px;margin:12px 0 {34 if nota else 50}px">{titulo}</div>{rows}
        {f'<div style="margin-top:20px;background:#FBDDEE;border-radius:32px;padding:30px 36px;font-size:40px;line-height:1.3"><span style="font-family:Sacramento;font-size:74px;color:#857055;line-height:.8">Tem uma ideia?</span><br>Me conta o que você imaginou que eu crio e faço para você!</div>' if nota else ''}</div>
      {LOGO_COR}
      {dots(i,n)}''', cls)

def cardapio(foto, titulo, peso, linhas, i, n, pos="center", fh=430):
    rows = "".join(f'<tr><td>{a}</td><td class="p">R$ {b}</td></tr>' for a, b in linhas)
    return page(f'''<div class="bg" style="height:{fh+120}px;background-image:url(prep/{foto}.jpg);background-position:{pos}"></div>
      <div class="fade" style="bottom:auto;top:{fh-180}px;height:300px;background:linear-gradient(to bottom, rgba(245,230,211,0), rgba(245,230,211,1) 70%)"></div>
      <div style="position:absolute;left:72px;right:72px;top:{fh}px">
        <div style="display:flex;align-items:center;gap:22px;margin-bottom:14px"><div class="tit m">{titulo}</div><span class="tag">{peso}</span></div>
        <table>{rows}</table></div>
      {LOGO_COR}{dots(i,n)}''', "creme")

def menu(foto, secoes, i, n, pos="center", fh=380, cls="creme", fs=36):
    """Cardápio com várias seções: (titulo, tag, linhas[(nome, preço)], nota)."""
    rgb = "245,230,211" if cls == "creme" else "255,233,247"
    blocos = ""
    for tit, tag, linhas, nota in secoes:
        rows = "".join(f'<tr><td style="font-size:{fs}px;padding:9px 0">{a}</td><td class="p" style="font-size:{fs}px;padding:9px 0">{("R$ " + b) if b else ""}</td></tr>' for a, b in linhas)
        tg = f'<span class="tag">{tag}</span>' if tag else ""
        nt = f'<div style="font-size:{fs-4}px;color:var(--cacau);margin-top:8px">{nota}</div>' if nota else ""
        blocos += f'<div style="margin-bottom:34px"><div style="display:flex;align-items:center;gap:20px;margin-bottom:6px"><div class="tit" style="font-size:54px">{tit}</div>{tg}</div><table>{rows}</table>{nt}</div>'
    return page(f'''<div class="bg" style="height:{fh+120}px;background-image:url(prep/{foto}.jpg);background-position:{pos}"></div>
      <div class="fade" style="bottom:auto;top:{fh-180}px;height:300px;background:linear-gradient(to bottom, rgba({rgb},0), rgba({rgb},1) 70%)"></div>
      {LOGO_COR}<div style="position:absolute;left:72px;right:72px;top:{fh}px">{blocos}</div>
      {dots(i,n)}''', cls)

def menu2(img, secoes, i, n, cls="creme", fs=40, largura=440, topo=40, inicio=500):
    """Cardápio com foto do produto (recortada ou em círculo) no canto e lista embaixo."""
    blocos = ""
    for tit, tag, linhas, nota in secoes:
        rows = "".join(f'<tr><td style="font-size:{fs}px;padding:10px 0">{a}</td><td class="p" style="font-size:{fs}px;padding:10px 0">{("R$ " + b) if b else ""}</td></tr>' for a, b in linhas)
        tg = f'<span class="tag">{tag}</span>' if tag else ""
        blocos += f'<div style="margin-bottom:34px"><div style="display:flex;align-items:center;gap:20px;margin-bottom:6px"><div class="tit" style="font-size:54px">{tit}</div>{tg}</div><table>{rows}</table></div>'
    t0 = secoes[0]
    return page(f'''<img src="prep/{img}.png" style="position:absolute;right:50px;top:{topo}px;width:{largura}px;filter:drop-shadow(0 18px 24px rgba(90,70,54,.22))">
      <div style="position:absolute;left:72px;top:110px;width:480px"><div class="sobre">Cardápio</div>
        <img src="prep/logo-t.png" style="width:170px;opacity:.6;margin-top:24px"></div>
      <div style="position:absolute;left:72px;right:72px;top:{inicio}px">{blocos}</div>
      {dots(i,n)}''', cls)

def menu_bolo(foto, titulo, tamanhos, massas, recheios, adicionais, i, n, cls="rosa", pos="center", fh=420):
    """Bolos no mesmo formato dos outros cards: foto no topo com degradê, informação em duas colunas."""
    rgb = "245,230,211" if cls == "creme" else "255,233,247"
    t = "".join(f'<tr><td style="font-size:35px;padding:7px 0">{a}</td><td class="p" style="font-size:35px;padding:7px 0">R$ {b}</td></tr>' for a, b in tamanhos)
    ad = "".join(f'<tr><td style="font-size:32px;padding:6px 0">{a}</td><td class="p" style="font-size:32px;padding:6px 0">R$ {b}</td></tr>' for a, b in adicionais)
    def lst(xs): return "".join(f'<div style="font-size:32px;line-height:1.42">{x}</div>' for x in xs)
    h = lambda x: f'<div class="sobre" style="font-size:24px;margin:0 0 6px">{x}</div>'
    return page(f'''<div class="bg" style="height:{fh+120}px;background-image:url(prep/{foto}.jpg);background-position:{pos}"></div>
      <div class="fade" style="bottom:auto;top:{fh-180}px;height:300px;background:linear-gradient(to bottom, rgba({rgb},0), rgba({rgb},1) 70%)"></div>
      {LOGO_COR}<div style="position:absolute;left:72px;right:72px;top:{fh}px">
        <div class="tit" style="font-size:54px;margin-bottom:18px">{titulo}</div>
        <div style="display:grid;grid-template-columns:1.15fr 1fr;gap:20px 56px">
          <div>{h("Tamanho")}<table>{t}</table><div style="height:26px"></div>{h("Adicionais")}<table>{ad}</table></div>
          <div>{h("Massas")}{lst(massas)}<div style="height:20px"></div>{h("Recheios")}{lst(recheios)}</div>
        </div></div>
      {dots(i,n)}''', cls)

def _cv(W, H, fx, fy):
    sc = 1080 / W; h = H * sc
    return fx * 1080, fy * h - (h - 1350) / 2

def seta(sx, sy, tx, ty, laco=True):
    """Seta desenhada à mão: pequeno laço na saída e curva até o alvo."""
    import math
    dx, dy = tx - sx, ty - sy; L = math.hypot(dx, dy) or 1
    nx, ny = -dy / L, dx / L
    c1 = (sx + dx * .25 + nx * L * .35, sy + dy * .25 + ny * L * .35)
    c2 = (sx + dx * .75 - nx * L * .25, sy + dy * .75 - ny * L * .25)
    d = f"M{sx:.0f},{sy:.0f} "
    if laco:
        ux, uy = dx / L, dy / L
        p1 = (sx + ux * 34 + nx * 30, sy + uy * 34 + ny * 30)
        p2 = (sx + ux * 10 - nx * 12, sy + uy * 10 - ny * 12)
        d += f"C{sx+ux*40:.0f},{sy+uy*40:.0f} {p1[0]+ux*10:.0f},{p1[1]+uy*10:.0f} {p1[0]:.0f},{p1[1]:.0f} "
        d += f"C{p1[0]-ux*30:.0f},{p1[1]-uy*30:.0f} {p2[0]:.0f},{p2[1]:.0f} {sx+ux*22:.0f},{sy+uy*22:.0f} "
    d += f"C{c1[0]:.0f},{c1[1]:.0f} {c2[0]:.0f},{c2[1]:.0f} {tx:.0f},{ty:.0f}"
    ang = math.atan2(ty - c2[1], tx - c2[0])
    a1 = (tx - 30 * math.cos(ang - .5), ty - 30 * math.sin(ang - .5))
    a2 = (tx - 30 * math.cos(ang + .5), ty - 30 * math.sin(ang + .5))
    d += f" M{a1[0]:.0f},{a1[1]:.0f} L{tx:.0f},{ty:.0f} L{a2[0]:.0f},{a2[1]:.0f}"
    return f'<path d="{d}" fill="none" stroke="#FFF6EC" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'

TITULO_ESTILO = "color:#FFF6EC;text-shadow:0 2px 12px rgba(60,40,30,.55);background:rgba(70,50,38,.22)"
import os
if os.environ.get("VAR") == "rosa":
    TITULO_ESTILO = "color:#5A4636;background:rgba(255,233,247,.72)"
elif os.environ.get("VAR") == "texto":
    TITULO_ESTILO = "color:#FBD3E9;text-shadow:0 2px 12px rgba(60,40,30,.55);background:rgba(70,50,38,.22)"

def anotado(foto, WH, titulo, notas, tpos=(.5, .09), pos="center"):
    """Foto real com o nome do produto e setas apontando os recheios.
    notas: (texto, (lx,ly) posição do rótulo, (sx,sy) início da seta, (tx,ty) alvo) em frações da foto original."""
    W, H = WH
    svg = ""; labels = ""
    for txt, lp, sp, tp in notas:
        lx, ly = _cv(W, H, *lp); sx, sy = _cv(W, H, *sp); tx, ty = _cv(W, H, *tp)
        svg += seta(sx, sy, tx, ty)
        labels += f'<div class="rot" style="left:{lx:.0f}px;top:{ly:.0f}px">{txt}</div>'
    tt = ""
    if titulo:
        tx, ty = _cv(W, H, *tpos)
        tt = f'<div class="scr" style="left:{tx:.0f}px;top:{ty:.0f}px">{titulo}</div>'
    return page(f'''<style>
      .rot{{position:absolute;transform:translate(-50%,-50%);font-family:Quicksand;font-weight:700;font-size:48px;line-height:1.12;text-align:center;color:#FFF6EC;text-shadow:0 1px 8px rgba(60,40,30,.55);white-space:nowrap;
            padding:12px 26px;border-radius:40px;background:rgba(70,50,38,.22);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}}
      .scr{{position:absolute;transform:translate(-50%,-50%);font-family:Quicksand;font-weight:700;font-size:92px;line-height:1.08;white-space:nowrap;text-align:center;
            padding:18px 44px;border-radius:60px;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);{TITULO_ESTILO}}}
      </style>
      <div class="bg" style="background-image:url(prep/{foto}.jpg);background-position:{pos}"></div>
      <svg style="position:absolute;inset:0;filter:drop-shadow(0 2px 6px rgba(60,40,30,.55))" width="1080" height="1350">{svg}</svg>
      {labels}{tt}
      <img src="prep/logo-t.png" style="position:absolute;right:44px;bottom:40px;width:170px;opacity:.72;filter:drop-shadow(0 0 14px rgba(255,255,255,.8))">''')

def quem_faz(foto, nome, texto, pos="center 25%", topo=False, rgb="255,233,247"):
    """Fixado Quem faz: foto dela no topo, degradê rosa, apresentação embaixo."""
    if foto:
        img = f'<div class="bg" style="background-image:url(prep/{foto}.jpg);background-position:{pos}"></div>'
    else:
        img = ('<div style="position:absolute;left:0;right:0;top:0;height:900px;background:repeating-linear-gradient(45deg,#F5E6D3 0 40px,#FBDDEE 40px 80px);'
               'display:flex;align-items:center;justify-content:center;font-family:Quicksand;font-weight:700;font-size:44px;color:#857055">'
               'foto dela aqui</div>')
    if topo:
        fd = (f'<div class="fade" style="top:0;bottom:auto;height:640px;background:linear-gradient(to bottom, rgba({rgb},1) 0%, '
              f'rgba({rgb},1) 42%, rgba({rgb},.75) 62%, rgba({rgb},0) 100%)"></div>')
        return page(f'''{img}{fd}<img src="prep/logo-t.png" style="position:absolute;right:60px;top:60px;width:130px;opacity:.75">
      <div style="position:absolute;left:72px;right:230px;top:80px"><div class="sobre">Quem faz</div>
        <div class="tit" style="margin-top:14px">Prazer, eu sou a {nome}!</div>
        <div class="corpo" style="margin-top:18px">{texto}</div></div>''')
    return page(f'''{img}{fade(620)}{LOGO_COR}
      <div class="txt"><div class="sobre">Quem faz</div>
        <div class="tit" style="margin-top:14px">Prazer, eu sou a {nome}!</div>
        <div class="corpo" style="margin-top:18px">{texto}</div></div>''')

def foto_pura(foto, pos="center", logo_pos="right:60px;top:56px"):
    """Foto real com o logo como marca d'água."""
    return page(f'''<div class="bg" style="background-image:url(prep/{foto}.jpg);background-position:{pos}"></div>
      <div style="position:absolute;right:0;top:0;width:460px;height:320px;background:radial-gradient(ellipse at 70% 36%, rgba(255,255,255,.6), rgba(255,255,255,0) 62%)"></div>
      <img src="prep/logo-t.png" style="position:absolute;width:200px;opacity:.72;{logo_pos}">''')



def render(posts, saida="out", qualidade=90):
    """posts: {"nome": [html_slide, ...]} -> lista de arquivos JPEG por post."""
    from playwright.sync_api import sync_playwright
    out = pathlib.Path(saida); out.mkdir(parents=True, exist_ok=True)
    feitos = {}
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for nome, slides in posts.items():
            arqs = []
            for k, html in enumerate(slides, 1):
                h = ROOT / "_tmp.html"; h.write_text(html)
                pg.goto(h.as_uri()); pg.wait_for_timeout(300)
                f = out / f"{nome}_{k:02d}.jpg"
                pg.screenshot(path=str(f), type="jpeg", quality=qualidade)
                arqs.append(f)
            feitos[nome] = arqs
        b.close()
    return feitos
