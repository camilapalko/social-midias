"""Dezembro/2026 · Cookies Land. Fotos: rode prep.py antes."""
import sys, pathlib, shutil
sys.path.insert(0, '/home/claude/social-midias/cookies-land-bakery/_kit')
from layouts import *

TMP = pathlib.Path(__file__).parent / 'out_dezembro'

PAG = [("app", "Peça pelo WhatsApp: o link está na bio"),
       ("pix", "Pix: 50% no pedido e 50% na entrega, ou o valor integral"),
       ("cartao", "Cartão parcelado pelo link do Mercado Pago (taxa do cliente)"),
       ("retirada", "Retirada na Vila Regente Feijó, das 9h às 21h"),
       ("entrega", "Entrega com taxa conforme a distância")]

def nome(a, b): return f'{a}<br><span style="font-size:36px;line-height:1.25;color:#857055;font-family:Nunito;font-weight:400;display:block;margin-top:2px">{b}</span>' if b else a

P = {}
# 01 · Qua 02/12 · A mão na massa · carrossel (capa cacau)
n = 4
P['01'] = [
 capa('d_fio', 'Dezembro na cozinha', 'Fornada atrás<br>de fornada', 0, n, pos='center 35%', h=620, cor='cacau'),
 fato('d_espatula', '', 'A massa vai para a forma', 'Massa de brownie com gotas de chocolate, espalhada à mão.', 1, n, pos='center 40%', sobre='Primeiro'),
 fato('d_gotas', '', 'As gotas por cima', 'Mais gotas de chocolate antes de ir para o forno.', 2, n, pos='center 45%', sobre='Depois'),
 cta('Feito à mão, fornada por fornada', 3, n, sub='Cookies Land Bakery'),
]
# 03 · Sex 04/12 · Como pedir · estático (encomendas de Natal)
P['03'] = [dourado(pagamento('Como encomendar o seu Natal', PAG, 0, 1, cls='creme', sobre='Encomendas de Natal abertas', fs=38))]
# 04 · Seg 07/12 · Presente · carrossel (capa rosa)
n = 3
P['04'] = [
 dourado(capa('d_bokeh_rosa', 'Presentes de Natal', 'Um doce para cada<br>pessoa da sua lista', 0, n, pos='center', h=640, cor='rosa')),
 dourado(menu_texto('Presentes de Natal', [
    ('Para o amigo secreto', '', [('Christmas Box com 1, 2 ou 3 unidades', '')], 'Cookies e/ou brownies recheados, decorados com tema de Natal.'),
    ('Para a ceia da família', '', [('Chocottone Trufado', ''), ('Guirlanda de Brownie (sobremesa)', ''), ('Sobremesa de travessa P ou M', '')], ''),
    ('Para a lembrancinha', '', [('Guirlanda de Brownie (mini)', ''), ('Cone Natalino recheado', '')], '')],
    1, n, cls='creme', fs=38)),
 cta('Quem está na sua lista este ano?', 2, n, sub='conta nos comentários'),
]
# 05 · Qua 09/12 · O que vai dentro · estático (Chocottone, sem foto própria)
Z = ''
P['05'] = [dourado(menu_texto('O que vai dentro · cerca de 900g', [
    ('Chocottone Trufado', '5 sabores', [
      (nome('Dois Amores', 'creme de brigadeiro branco e creme de brigadeiro ao leite'), Z),
      (nome('NinhoTella', 'creme de Leite Ninho e Nutella'), Z),
      (nome('Amaro', 'creme de cacau com avelãs tostadas e brigadeiro meio amargo'), Z),
      (nome('Pistacchio', 'creme de pistache e brigadeiro branco, com pedacinhos de pistache'), Z),
      (nome('Morango Cravejado', 'brigadeiro branco com morangos e crocante de caramelo'), Z)],
     'Todos com a moeda de chocolate dourada da marca no topo.')], 0, 1, cls='rosa', fs=48))]
# 07 · Sex 11/12 · Para o seu negócio · estático
P['07'] = [dourado(lista('d_espalha', 'Natal para empresas', 'Lembrancinha de Natal<br>para a sua equipe',
    ['Brownie recheado, em 3 tamanhos', 'Brownie com gotas de chocolate', 'Saquinho com cerca de 6 mini cookies', 'Tag de Natal e laço de cetim em todos'],
    0, 1, pos='center 30%', fh=500, fs=42))]
# 08 · Seg 14/12 · Presente · carrossel (capa creme)
n = 4
P['08'] = [
 dourado(capa('d_bokeh_creme', 'Presente de Natal', 'Monte a sua<br>Christmas Box', 0, n, pos='center', h=640, cor='creme')),
 dourado(menu_texto('Christmas Box', [
    ('Passo 1 · o tamanho', '', [('Caixa com 1 unidade', ''), ('Caixa com 2 unidades', ''), ('Caixa com 3 unidades', '')], ''),
    ('Passo 2 · o recheio', '', [('Cookies recheados', ''), ('Brownies recheados', ''), ('Ou os dois na mesma caixa', '')], '')],
    1, n, cls='rosa', fs=50)),
 dourado(menu_texto('Passo 2 · os sabores', [
    ('Brownies', '', [], 'Dois Amores, Brigadeiro ao Leite, Brigadeiro Branco, Doce de Leite, Leitinho, Nutella, Kinder Bueno, Ovomaltine e Amaro.'),
    ('Cookies', '', [], 'Oreo Cream, Nutella, Kinder Bueno, Ovomaltine, Pistacchio, Churros, Amaro e Creme Branco.'),
    ('Passo 3', '', [], 'Cada um vem decorado com tema de Natal.')],
    2, n, cls='creme', fs=54)),
 cta('Salva para montar a sua', 3, n, sub='Christmas Box'),
]
# 09 · Qua 16/12 · A mão na massa · estático (frase)
P['09'] = [foto_pura('d_fouet', pos='center 40%', logo_pos='left:60px;top:56px')]
# 11 · Sex 18/12 · Como pedir · estático (vidro)
P['11'] = [dourado(vidro('d_bokeh_noite', 'Ainda dá tempo de encomendar o seu Natal', 'Me chama no WhatsApp e confere as datas de retirada.', pos='center'))]
# 12 · Seg 21/12 · A mão na massa · carrossel (capa cacau + diário)
n = 4
P['12'] = [
 capa('d_c_grade3', 'Semana de Natal', 'A cozinha<br>não para', 0, n, pos='center 0%', h=700, cor='cacau'),
 diario('d_c_grade', 'na grade', 'Cookie saindo do forno vai direto para a grade.', 1, n, pos='center 100%').replace('left:64px;bottom:110px;max-width:760px', 'right:64px;bottom:96px;max-width:560px'),
 diario('d_c_grade2', 'quase lá', 'Esfriando, um do lado do outro, antes de embalar.', 2, n, pos='center 35%'),
 cta('Obrigada por cada pedido deste Natal', 3, n, sub='com carinho, Ju'),
]
# 13 · Qua 23/12 · Para o seu negócio · estático (bolo de cenoura)
P['13'] = [fato('d_bolo_cen', '', 'Janeiro começa<br>no seu balcão', 'Bolo de cenoura de 70g, embalado um a um, com validade de 6 dias.', 0, 1, pos='center 60%', h=600, topo=True, sobre='Para o seu negócio')]
# 15 · Sex 25/12 · Natal · estático (vidro)
P['15'] = [dourado(vidro('d_bokeh_ouro', 'Feliz Natal!', 'Obrigada por deixar a sua mesa mais doce com a gente.', pos='center'))]
# 16 · Seg 28/12 · O que vai dentro · carrossel (capa rosa)
n = 5
P['16'] = [
 capa('d_c_nut_aberto', 'De perto', 'Um cookie<br>de 90g', 0, n, pos='center 20%', h=560, cor='rosa'),
 fato('d_c_nut_parte', '1', 'Por dentro', 'No de Nutella, o recheio vai por dentro e as gotas ao leite, por fora.', 1, n, pos='center 30%', topo=True),
 fato('d_c_kb_pist', '2', 'Por cima', 'No de pistache, os pedacinhos de pistache vão por cima.', 2, n, pos='center 55%', topo=True),
 fato('d_c_mix', '3', '90g cada', 'Todos do mesmo tamanho, feitos à mão, fornada por fornada.', 3, n, pos='center 50%', topo=True),
 cta('Qual você parte primeiro?', 4, n, sub='conta nos comentários'),
]
# 17 · Qua 30/12 · Como pedir · estático (prazos)
P['17'] = [prazos('d_c_partido', 'Anota os prazos para 2027', [
    ('Brownies e cookies', 'pronta entrega'), ('Bolos', '3 dias'), ('Docinhos e bombons', '2 dias'),
    ('Lembrancinha com tag', '10 dias'), ('Lembrancinha sem tag', '4 dias')],
    'Brownies e cookies: consulte a disponibilidade. Urgência tem taxa extra.', 0, 1, pos='center 45%', fh=470)]

so = sys.argv[1:]
if so: P = {k: v for k, v in P.items() if k in so}
elif TMP.exists(): shutil.rmtree(TMP)
feitos = render(P, saida=str(TMP))
print({k: len(v) for k, v in feitos.items()})
