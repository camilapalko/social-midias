import pathlib
from PIL import Image, ImageOps, ImageFilter, ImageEnhance
try:
    import pillow_heif; pillow_heif.register_heif_opener()
except Exception:
    pass
B = pathlib.Path('/home/claude/social-midias/cookies-land-bakery/fotos')
N = pathlib.Path('/home/claude/social-midias/cookies-land-bakery/fotos-natal')  # fotos próprias de Natal
P = pathlib.Path('/home/claude/social-midias/cookies-land-bakery/_kit/prep')

def prep(src, nome, crop=None, minimo=0):
    im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    if crop:
        w, h = im.size; im = im.crop((int(crop[0]*w), int(crop[1]*h), int(crop[2]*w), int(crop[3]*h)))
    # tirar o amarelado de leve
    r, g, b = im.split(); b = b.point(lambda v: min(255, int(v*1.04))); r = r.point(lambda v: int(v*.985)); im = Image.merge('RGB', (r, g, b))
    if max(im.size) > 2000: im.thumbnail((2000, 2000), Image.LANCZOS)
    if minimo and min(im.size) < minimo:
        k = minimo / min(im.size); im = im.resize((int(im.width*k), int(im.height*k)), Image.LANCZOS)
        im = im.filter(ImageFilter.UnsharpMask(2, 60, 2))
    im.save(P / f'{nome}.jpg', quality=93)

F = {
 'c_nutella_aberto': B/'cookies/vic04260_1Lawgc.jpg',
 'c_trio': B/'cookies/vic04221_1qyoUB.jpg',
 'c_pistache': B/'cookies/vic04265_1lKZHN.jpg',
 'c_aberto2': B/'cookies/vic04253_1YGpfu.jpg',
 'b_pilha': B/'brownies/vic00570_1NuzhO.jpg',
 'b_pilha2': B/'brownies/vic00575_1TkvxG.jpg',
 'b_vitrine': B/'brownies/vic00569_1ttBV_.jpg',
 'naked_frutas': B/'bolo/vic00370_13qHWj.jpg',
 'p_massa_forma': B/'prdoucao-fotos/photo-2026-10-05-22-55-00_1QbVTe.jpg',
 'p_batedor': B/'prdoucao-fotos/photo-2026-10-05-22-55-01-2_1KrgNp.jpg',
 'p_forno': B/'prdoucao-fotos/photo-2026-10-05-22-55-01_15fnES.jpg',
 'p_tigela': B/'prdoucao-fotos/photo-2026-10-05-22-55-02_1JS-pv.jpg',
}
for k, v in F.items(): prep(v, k)
# Natal: fotos próprias que vieram nos manuais (pequenas: ampliadas para polaroid)
prep(N/'chocottone-inteiro.png', 'n_chocottone', minimo=900)
prep(N/'chocottone-cortado.png', 'n_chocottone_corte', minimo=900)
prep(N/'browniettone-fatia.jpg', 'n_browniettone', minimo=900)
prep(N/'brokiettone-topo.jpg', 'n_brokiettone', crop=(0, 0, 1, .78), minimo=900)
prep(N/'pj-brownie-recheado.jpg', 'n_pj_brownie')
prep(N/'pj-brownie-gotas-laco.png', 'n_pj_lacos', minimo=900)
print(sorted(p.name for p in P.glob('*.jpg')))
