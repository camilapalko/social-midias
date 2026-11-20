import pathlib, random
import numpy as np
from PIL import Image, ImageOps, ImageFilter, ImageDraw
B = pathlib.Path('/home/claude/social-midias/cookies-land-bakery/fotos')
P = pathlib.Path('/home/claude/social-midias/cookies-land-bakery/_kit/prep')
def prep(src, nome, crop=None, minimo=0, brilho=1.0):
    im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    if crop:
        w, h = im.size; im = im.crop((int(crop[0]*w), int(crop[1]*h), int(crop[2]*w), int(crop[3]*h)))
    r, g, b = im.split(); b = b.point(lambda v: min(255, int(v*1.04))); r = r.point(lambda v: int(v*.985)); im = Image.merge('RGB', (r, g, b))
    if brilho != 1.0:
        from PIL import ImageEnhance; im = ImageEnhance.Brightness(im).enhance(brilho)
    if max(im.size) > 2000: im.thumbnail((2000, 2000), Image.LANCZOS)
    if minimo and min(im.size) < minimo:
        k = minimo / min(im.size); im = im.resize((int(im.width*k), int(im.height*k)), Image.LANCZOS)
        im = im.filter(ImageFilter.UnsharpMask(2, 60, 2))
    im.save(P / f'{nome}.jpg', quality=93)
PR = B/'prdoucao-fotos'
F = {
 'd_fio': (PR/'photo-2026-10-05-22-47-01_11DB_8.jpg', 1.08),
 'd_gotas': (PR/'photo-2026-10-05-22-55-00-3_1R-GIP.jpg', 1.08),
 'd_espalha': (PR/'photo-2026-10-05-22-55-00-2_1tm2UY.jpg', 1.08),
 'd_espatula': (PR/'photo-2026-10-05-22-55-00-1_1n4g9D.jpg', 1.08),
 'd_fouet': (PR/'photo-2026-10-05-22-55-02_1JS-pv.jpg', 1.0),
 'd_c_kb_pist': (B/'cookies/vic04226_1aT0qg.jpg', 1.0),
 'd_c_nut_parte': (B/'cookies/vic04250_1Qex87.jpg', 1.0),
 'd_c_nut_aberto': (B/'cookies/vic04245_1w9M6F.jpg', 1.0),
 'd_c_partido': (B/'cookies/vic04264_1TcBL9.jpg', 1.0),
 'd_c_grade': (B/'cookies/vic04236_1b3KIX.jpg', 1.0),
 'd_c_grade2': (B/'cookies/vic04237_12Wy_1.jpg', 1.0),
 'd_c_grade3': (B/'cookies/dsc02204_1ChgA5.jpg', 1.0),
 'd_c_mix': (B/'cookies/vic04233_1DLAcY.jpg', 1.0),
 'd_bolo_cen': (B/'bolo-cenoura-70g/vic00449_1VukAo.jpg', 1.0),
}
for k, (f, br) in F.items(): prep(f, k, minimo=1100, brilho=br)

def bokeh(nome, top, bot, cores, seed, n=70):
    random.seed(seed); W, H = 1600, 2000
    a = np.linspace(0, 1, H)[:, None, None]
    base = (np.array(top)[None, None, :] * (1 - a) + np.array(bot)[None, None, :] * a) * np.ones((H, W, 3))
    im = Image.fromarray(base.astype('uint8'))
    for blur, cnt, rmin, rmax, alpha in [(40, n//2, 90, 200, 70), (14, n//2, 40, 110, 120), (5, n//3, 14, 40, 170)]:
        lay = Image.new('RGBA', (W, H), (0, 0, 0, 255)); d = ImageDraw.Draw(lay)
        for _ in range(cnt):
            x, y = random.randint(-100, W+100), random.randint(-100, H+100); r = random.randint(rmin, rmax)
            c = random.choice(cores); k = alpha/255; d.ellipse((x-r, y-r, x+r, y+r), fill=tuple(int(v*k) for v in c) + (255,))
        lay = lay.filter(ImageFilter.GaussianBlur(blur)).convert('RGB'); from PIL import ImageChops; im = ImageChops.screen(im, lay)
    im.save(P / f'{nome}.jpg', quality=93)
OURO, ROSA, BR, PES = (238, 200, 120), (250, 190, 215), (255, 245, 235), (242, 176, 140)
bokeh('d_bokeh_rosa', (120, 80, 90), (225, 160, 180), [OURO, ROSA, BR], 3)
bokeh('d_bokeh_ouro', (70, 45, 35), (150, 100, 70), [OURO, PES, BR], 7)
bokeh('d_bokeh_creme', (200, 165, 140), (245, 220, 200), [OURO, BR, ROSA], 11)
bokeh('d_bokeh_noite', (60, 40, 55), (170, 110, 120), [OURO, ROSA, BR], 19)
print('ok')
