# Rotina mensal · Cookies Land Bakery

Roda todo dia 20 e gera o mês seguinte inteiro (do dia 1 ao último dia). Este arquivo
reúne tudo que a rotina precisa; nada aqui depende da conversa em que foi criado.

## 1. A marca em uma linha
Doces artesanais com assinatura, para presentear, celebrar e vender no seu negócio.
Confeiteira: **Ju**. Retirada na Vila Regente Feijó (SP), das 9h às 21h.

## 2. Cardápio e fatos (confira o briefing do mês, que manda sobre isto)
- **Cookies 90g:** Brigadeiro ao leite 10 · Oreo Cream 14 · Nutella 14 · Kinder Bueno 14 · Ovomaltine 14 · Pistache 16 · Churros 14
- **Brownies 110g:** Brigadeiro ao leite 10 · Brigadeiro branco 10 · Casadinho 10 · Doce de leite 12 · NinhoTella 14 · Nutella 14 · Kinder Bueno 14 · Ovomaltine 16
- Bolo de cenoura 70g (brigadeiro ao leite) 6 · Bombom de brownie 18 · Pão de mel (doce de leite) 17
- Docinhos tradicionais 5,60 un · premium 6,60 un · Bombom de morango 14 un
- Naked cake 10-15 fatias 100 / 15-20 145 / 20-25 200 · Premium 145 / 180 / 240 · adicionais: frutas 40, mais recheio 50, brigadeiros 5,57 un
- **Prazos:** brownies e cookies pronta entrega (consultar disponibilidade) · bolos 3 dias · docinhos e bombons 2 dias · lembrancinha com tag 10 dias, sem tag 4 dias · urgência com taxa extra
- **Pagamento:** Pix 50% no pedido e 50% na entrega ou integral · cartão parcelado pelo link do Mercado Pago, taxa do cliente
- **Entrega:** taxa conforme a distância · Uber/99 com horário combinado
- **Empresas (B2B):** validade brownie 20 dias, bolo de cenoura 6 · pedido mínimo 20 unidades · expositor em MDF incluso · troca sem custo · entrega grátis (consulte a região) · se não funcionar no ponto, devolve o dinheiro da primeira compra
- Encomenda personalizada: "Tem uma ideia? Me conta que eu crio e faço."

## 3. Ritmo do feed (todos os posts às 18:00)
| Seg | Qua | Qui | Sex |
|---|---|---|---|
| estático (atrai: O que vai dentro / Presente) | estático (relação: A mão na massa) | **Reels** | estático (venda: Como pedir / Para o seu negócio) |

- A mesma editoria só volta depois de outras duas. Nunca dois posts seguidos no mesmo formato.
- Feriado recebe o post mais leve da semana. Datas comemorativas viram post de Presente na véspera.
- Fixados (Cardápio, Para o seu negócio, Quem faz) não se repetem; o cardápio só volta se mudar preço/sabor.

## 4. Editorias
1. **O que vai dentro de cada um** (25%) · valor do produto: corte, recheio, gramatura exata
2. **A mão na massa** (25%) · bastidor, produção, Ju, o Samurai (cachorro dela)
3. **Doce que vira presente** (20%) · ocasiões, datas, festas
4. **Para o seu negócio** (15%) · revenda em cafés, padarias, mercados, empresas
5. **Como pedir o seu** (15%) · cardápio, prazos, novidades, encomendas abertas

## 5. Modelos aprovados (funções em `_kit/layouts.py`)
| Modelo | Função | Uso |
|---|---|---|
| Carrossel capa + fatos | `capa` (cor rosa/creme/cacau, alternar), `fato`, `lista`, `pagamento`, `cta` | Todo carrossel segue este padrão; muda só a cor da capa |
| Foto anotada | `anotado` | Sabor em destaque, presente: título + setas apontando recheios |
| Foto pura | `foto_pura` | Foto sem texto, logo como marca d'água |
| Cartão de aviso | `vidro` | Novidade, datas, encomendas abertas, vagas para parceiros |
| Exemplos completos | `_kit/exemplo_outubro.py` | Todas as artes aprovadas de outubro, com os parâmetros usados |

Regras visuais: logo sempre como marca d'água pequena na área de cor; produto na parte livre do texto
(espelhe a foto se preciso); texto curto; nada de emoji na arte; conferir cada arte renderizada
antes de entregar (texto sobre o produto, título descentralizado, logo em cima do doce = refazer).
Fotos: ajuste leve de cor (tirar amarelado); recorte de fundo só quando ficar natural; nunca doce gerado.

## 6. Voz das legendas
- Primeira pessoa (Ju), frases curtas, 1 a 3 emojis, exclamação nas chamadas. Sem hashtag.
- Peso exato (110g / 90g), só em post de produto. Dizer se o ingrediente vai dentro ou por cima.
- "Feito à mão, fornada por fornada" (nunca "feito no dia"). "Etiqueta", não "medalha".
- Preço só em Como pedir. Um chamado de venda por semana.
- Chamadas: "Peça o seu pelo WhatsApp, o link está na bio 📲" · "Chame no WhatsApp e peça a tabela para empresas!" · "Encomendas da semana abertas!"
- Nunca inventar fato (receita, história, ingrediente) que não esteja aqui ou no briefing.

## 7. Fotos
- Banco: `fotos/<categoria>/`, índice em `fotos/indice.json` (campo `original` = nome no Drive).
- **Prioridade:** fotos novas (não listadas em `usadas.json`) > fotos já usadas com outro enquadramento/modelo.
- `fotos/caseiras/` é **reserva**: só use se não houver outra opção e o mês estiver repetindo demais. Avise na entrega quando usar.
- `fotos/pascoa-*` e outras sazonais: só na época certa.
- Ao terminar, acrescente em `usadas.json` a chave do mês com os nomes originais usados.

## 8. Reels
- Um por semana, às quintas, editoria alternando 1 e 2 (às vezes 3 ou 4).
- No lote: `tipo: "reel"` com `prompt` = roteiro (tabela de tempos, o que gravar, texto na tela, 3 opções de capa, 9:16, 15-25s).
- Na entrega, liste a **pauta do dia de gravação**: o que deixar pronto, cenas de todos os Reels do mês e fotos a aproveitar.

## 9. Entrega
1. Leia `briefing/<AAAA-MM>.md|.json` do mês a gerar. Se não houver, siga com o que está aqui e avise.
2. Monte o calendário (posts do mês, regras do item 3), gere as artes com o kit, confira cada uma.
3. Pasta nova `cookies-land-bakery/<AAAA-MM-DD do dia da geração>/`, imagens `.jpg` + `lote.json` no formato do dash (máx. 20 posts por lote; mais que isso, 2 pastas).
4. Atualize `usadas.json` e escreva `perguntas-proximo-mes.json` (3 a 5 perguntas específicas para o briefing do mês seguinte: datas, campanhas, lançamentos).
5. Um commit, push para main. Nunca reenviar um lote.json já enviado.
6. Relatório final: pasta, nº de posts, Reels aguardando vídeo, pauta de gravação, fotos de reserva usadas, o que faltou no briefing.
