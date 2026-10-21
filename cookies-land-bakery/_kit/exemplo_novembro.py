import sys, json, pathlib, shutil
sys.path.insert(0, '/home/claude/social-midias/cookies-land-bakery/_kit')
from layouts import *

PASTA = '2026-10-21'
OUT = pathlib.Path('/home/claude/social-midias/cookies-land-bakery') / PASTA
TMP = pathlib.Path(__file__).parent / 'out_novembro'

PAG = [("app", "Peça pelo WhatsApp: o link está na bio"),
       ("pix", "Pix: 50% no pedido e 50% na entrega, ou o valor integral"),
       ("cartao", "Cartão parcelado pelo link do Mercado Pago (taxa do cliente)"),
       ("retirada", "Retirada na Vila Regente Feijó"),
       ("entrega", "Entrega com taxa conforme a distância")]

SAB6 = [("Dois Amores", "brigadeiro branco e brigadeiro ao leite"),
        ("NinhoTella", "creme de Leite Ninho e Nutella"),
        ("Amaro", "creme de cacau com avelãs tostadas e brigadeiro meio amargo"),
        ("Kinder Bueno", "creme e crocante de Kinder Bueno com brigadeiro branco"),
        ("Ovomaltine", "creme de Ovomaltine e brigadeiro ao leite"),
        ("Doce de Leite", "recheio de doce de leite")]

P = {}
# 01 · Seg 02/11 (Finados) · foto com frase
P['01'] = [frase('c_nutella_aberto', 'Feriado pede<br>recheio escorrendo.', 'Cookie recheado · 90g', pos='center 60%')]
# 02 · Qua 04/11 · diário de produção
P['02'] = [diario('p_batedor', 'a massa', 'Tudo começa aqui, na tigela.', 0, 3),
           diario('p_forno', 'o forno', 'Fornada por fornada, de olho no ponto.', 1, 3),
           diario('c_aberto2', 'pronto!', 'Recheio por dentro, como tem que ser.', 2, 3, pos='center 55%')]
# 04 · Sex 06/11 · teaser de Natal
P['04'] = [natal_desfoque('n_chocottone', 'Tem novidade de Natal<br>saindo do forno', 'segunda eu conto tudo')]
# 05 · Seg 09/11 · cardápio de Natal (encomendas abertas)
n = 9
P['05'] = [
 natal_card('Cardápio de Natal', 'As encomendas de Natal já estão abertas!', 'n_chocottone', 0, n, sobre='Chegou o Natal Cookies Land', fw=500, fh=500),
 natal_menu('Chocottone Trufado', 'cerca de 900g', 'n_chocottone_corte', [
    ("Dois Amores", "brigadeiro branco e ao leite, cobertura duo"),
    ("NinhoTella", "creme de Leite Ninho e Nutella, cobertura de chocolate branco"),
    ("Amaro", "creme de cacau com avelãs tostadas e brigadeiro meio amargo"),
    ("Pistacchio", "creme de pistache e brigadeiro branco, com pedacinhos de pistache"),
    ("Morango Cravejado", "brigadeiro branco com morangos e crocante de caramelo")],
    [("Chocottone", None)], 1, n, compacto=True),
 natal_menu('Browniettone Trufado', 'cerca de 450g', 'n_browniettone', SAB6, [("Browniettone", None)], 2, n,
    intro='Brownie com gotas de chocolate em formato de panettone, recheado.', compacto=True, pos='center 70%'),
 natal_menu('Brokiettone Trufado', 'cerca de 450g', 'n_brokiettone', SAB6, [("Brokiettone", None)], 3, n,
    intro='Camadas de brownie e cookie em formato de panettone, recheado.', compacto=True,
    nota='Todos levam a moeda de chocolate dourada da marca no topo.'),
 natal_menu('Sobremesas de travessa', 'P e M', None, [
    ("Banoffe", "base crocante, bananas, doce de leite, chantilly e canela"),
    ("Uvoffe", "base crocante, uvas sem sementes, doce de leite, chantilly e raspas de chocolate branco"),
    ("Merengue de Morango", "brigadeiro branco, morangos, suspiros e chantilly")],
    [("Tamanho P", None), ("Tamanho M", None)], 4, n),
 natal_menu('Cone Natalino', '', None, [(a, b) for a, b in [
    ("Dois Amores", "brigadeiro branco e ao leite"), ("NinhoTella", "creme de Leite Ninho e Nutella"),
    ("Kinder Bueno", "creme e crocante de Kinder Bueno com brigadeiro branco"), ("Ovomaltine", "creme de Ovomaltine e brigadeiro ao leite"),
    ("Morango Cravejado", "brigadeiro branco com morangos e crocante de caramelo"), ("Pistacchio", "creme de pistache e brigadeiro branco")]],
    [("Cone", None)], 5, n, intro='Cone de biscoito recheado e decorado como uma arvorezinha de Natal.', compacto=True),
 natal_menu('Guirlanda de Brownie', 'mini e sobremesa', None, [
    ("Dois Amores", ""), ("NinhoTella", ""), ("Amaro", ""), ("Kinder Bueno", ""), ("Ovomaltine", ""), ("Ninho com Morangos", "")],
    [("Mini (lembrancinha)", None), ("Sobremesa (ceia)", None)], 6, n,
    intro='Brownie em formato de guirlanda, recheado, com brigadeiros, confeitos e laço vermelho no topo.', compacto=True),
 natal_menu('Christmas Box', '1, 2 ou 3 unidades', None, [
    ("Brownies", "Dois Amores, Brigadeiro ao Leite, Brigadeiro Branco, Doce de Leite, Leitinho, Nutella, Kinder Bueno, Ovomaltine e Amaro"),
    ("Cookies", "Oreo Cream, Nutella, Kinder Bueno, Ovomaltine, Pistacchio, Churros, Amaro e Creme Branco")],
    [("1 unidade", None), ("2 unidades", None), ("3 unidades", None)], 7, n,
    intro='Cookies e/ou brownies recheados, decorados com tema de Natal, nos sabores que você escolher.'),
 pagamento('Como encomendar', PAG, 8, n, cls='creme', sobre='Encomendas de Natal abertas', fs=38),
]
# 06 · Qua 11/11 · isto ou aquilo
P['06'] = [isto_ou_aquilo('b_pilha', 'c_trio', 'Brownie 110g', 'Cookie 90g', 'Hoje é dia de quê?', p1='70% 60%', p2='center 40%')]
# 08 · Sex 13/11 · Natal para empresas
n = 5
P['08'] = [
 natal_card('Lembrancinhas de Natal para a sua empresa', 'Para colaboradores, clientes, fornecedores e parceiros.', 'n_pj_brownie', 0, n, sobre='Natal para empresas', fw=480, fh=480, pos='center 35%'),
 natal_menu('Brownie recheado', '', 'n_pj_brownie', [("Brigadeiro Branco", ""), ("Brigadeiro ao Leite", ""), ("Casadinho", "brigadeiro branco e brigadeiro ao leite")],
    [("6 x 6 cm · cerca de 100g", False), ("5 x 5 cm · cerca de 70g", False), ("4 x 4 cm · cerca de 45g", False)], 1, n,
    sobre='Natal para empresas', compacto=True, pos='center 30%'),
 natal_menu('Brownie com gotas de chocolate', '', 'n_pj_lacos', [],
    [("6 x 6 cm · cerca de 45g", False), ("5 x 5 cm · cerca de 35g", False)], 2, n, sobre='Natal para empresas',
    intro='Simples, gostoso e com a cara do Natal.'),
 natal_card('Saquinho de mini cookies', 'Cerca de 6 mini cookies com gotas de chocolate: a lembrancinha certa para a confraternização.', None, 3, n, sobre='Natal para empresas'),
 pagamento('Condições para empresas', [("selo", "Todos com tag de Natal e laço de cetim"), ("app", "Pedido mínimo: acima de 10 unidades"),
    ("pix", "Preços promocionais e desconto extra no Pix"), ("cartao", "Boleto com prazo combinado"), ("entrega", "Entrega: consulte a sua região")],
    4, n, cls='creme', sobre='Natal para empresas', fs=38),
]
# 09 · Seg 16/11 · a dupla
P['09'] = [natal_dupla('n_browniettone', 'n_brokiettone', 'Panettone do jeito<br>da Cookies Land', 'Cerca de 450g cada, recheados.',
                       'Browniettone', 'Brokiettone', p1='center 75%', p2='center 40%')]
# 10 · Qua 18/11 · antes e depois
P['10'] = [antes_depois('p_massa_forma', 'Antes', 'A massa vai para a forma, espalhada à mão.', 0, 2),
           antes_depois('b_pilha2', 'Depois', 'Brownie de 110g, recheado por dentro.', 1, 2, pos='70% 60%')]
# 12 · Sex 20/11 (feriado) · isto ou aquilo de Natal
P['12'] = [natal_dupla('n_chocottone', 'n_browniettone', 'Qual vai para a sua ceia?', 'Responde aqui embaixo.', 'Chocottone', 'Browniettone',
                       p1='center', p2='center 75%', pergunta=True)]
# 13 · Seg 23/11 · presentes de Natal
n = 5
P['13'] = [
 natal_card('Presente de Natal que se come', 'Para o amigo secreto, a família e quem você quiser agradecer.', None, 0, n, sobre='Presentes de Natal'),
 natal_card('Christmas Box', 'Com 1, 2 ou 3 cookies e/ou brownies recheados, decorados com tema de Natal. Você escolhe os sabores.', None, 1, n, sobre='Presentes de Natal'),
 natal_card('Guirlanda de Brownie', 'Na versão mini, para lembrancinha.<br>Na versão sobremesa, para a ceia.', None, 2, n, sobre='Presentes de Natal'),
 natal_card('Cone Natalino', 'Um cone recheado e decorado como uma arvorezinha de Natal.', None, 3, n, sobre='Presentes de Natal'),
 cta('Escolha o seu presente pelo WhatsApp', 4, n),
]
# 14 · Qua 25/11 · para o seu negócio
P['14'] = [frase('b_vitrine', 'Dezembro chegando:<br>seu balcão tem brownie?', 'Para o seu negócio', pos='center 40%')]
# 16 · Sex 27/11 · encomendas de Natal abertas (reforço)
P['16'] = [natal_card('Encomendas de Natal abertas!', 'Chocottone, Browniettone, Brokiettone, sobremesas, guirlanda e Christmas Box.', 'n_chocottone_corte', 0, 2, fw=480, fh=520),
           pagamento('Como encomendar', PAG, 1, 2, cls='creme', sobre='Encomendas de Natal abertas', fs=38)]
# 17 · Seg 30/11 · naked cake
P['17'] = [frase('naked_frutas', 'Dezembro tem festa.<br>O bolo fica comigo.', 'Naked cake', pos='center 55%', lado='topo')]

so = sys.argv[1:]
if so: P = {k: v for k, v in P.items() if k in so}
if TMP.exists() and not so: shutil.rmtree(TMP)
feitos = render(P, saida=str(TMP))
print({k: len(v) for k, v in feitos.items()})
