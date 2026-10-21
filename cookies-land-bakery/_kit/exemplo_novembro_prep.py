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
from PIL import ImageFilter
C = B/'caseiras'
F2 = {
 'x_choco_inteiro': (C/'img-9805_1MMh7T.heic', None),
 'x_choco_papai': (C/'img-9814_1jQ5Mx.heic', None),
 'x_choco_corte': (C/'img-9822_1NAH61.heic', None),
 'x_choco_corte2': (C/'img-9820_1U3JyJ.heic', None),
 'x_choco_dentro': (C/'img-9826_1gBgHx.heic', None),
 'x_guirlanda': (C/'img-0291_1SzCoG.heic', None),
 'x_guirlanda2': (C/'img-0289_1pql1f.heic', None),
 'x_browniettone': (C/'69be38d2-a74d-4e99-ad5d-01c56ae5bcc6_1qWrlP.jpg', None),
 'x_brokiettone': (C/'56f70966-9724-461d-87da-fb39d2c5c2f9_1dSbrH.jpg', (0, 0, 1, .8)),
 'x_choco_dourado': (C/'img-9908_1zQ1kG.jpg', None),
 'x_choco_dourado_corte': (C/'img-9914_1CBWxm.jpg', None),
 'x_pj_embalado': (C/'26d8c497-e1b6-4f8b-bd7d-02645ff68b3c_1fo6kh.jpg', None),
 'x_pj_pilha': (C/'83394f77-57b4-4bac-98ec-7f7ad0eef90c_1O_rXf.jpg', None),
 'n_pj_brownie': (N/'pj-brownie-recheado.jpg', None),
}
for k, (f, cr) in F2.items(): prep(f, k, crop=cr, minimo=1100)
im = Image.open(P/'x_choco_inteiro.jpg'); im.filter(ImageFilter.GaussianBlur(40)).save(P/'x_teaser.jpg', quality=92)
print('ok')

print(sorted(p.name for p in P.glob('*.jpg')))
