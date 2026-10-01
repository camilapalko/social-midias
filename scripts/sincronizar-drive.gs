/**
 * Copia as fotos novas do Drive para o GitHub (camilapalko/social-midias).
 * Roda no Google Apps Script, com a sua própria conta (não precisa de chave de serviço).
 *
 * Configuração (uma vez):
 *  1. Projeto > Configurações do projeto > Propriedades do script:
 *       GITHUB_TOKEN = seu token fine-grained (Contents: read and write)
 *  2. Rode a função "instalarGatilho" uma vez (cria o agendamento do dia 19, 23h).
 *  3. Rode "sincronizar" uma vez agora para copiar as fotos atuais.
 *     Se não der tempo, ele se reagenda sozinho a cada 1 minuto até terminar (veja em Execuções).
 */
const CFG = {
  owner: 'camilapalko',
  repo: 'social-midias',
  branch: 'main',
  clientes: {
    'cookies-land-bakery': '1DktMxLa7DHjkyNvx0Y4bHXRJ3pmxbg_S',
  },
  limiteMs: 5 * 60 * 1000,   // o Apps Script para em 6 min; paramos antes e continuamos depois
};

function sincronizar() {
  const inicio = Date.now();
  const props = PropertiesService.getScriptProperties();
  let faltou = false;
  const token = props.getProperty('GITHUB_TOKEN');
  if (!token) throw new Error('Falta a propriedade GITHUB_TOKEN');

  for (const [slug, pastaId] of Object.entries(CFG.clientes)) {
    let novos = 0, acabou = true;
    const fotos = [];
    coletar_(DriveApp.getFolderById(pastaId), null, fotos);
    for (const { arquivo, categoria } of fotos) {
      const chave = slug + ':' + arquivo.getId();
      if (props.getProperty(chave)) continue;
      if (Date.now() - inicio > CFG.limiteMs) { acabou = false; break; }
      const nome = nomeLimpo_(arquivo.getName(), arquivo.getId());
      const caminho = `${slug}/fotos/${categoria}/${nome}`;
      const r = enviar_(token, caminho, arquivo.getBlob().getBytes(), 'foto do Drive: ' + arquivo.getName());
      if (r === 201 || r === 422) {           // 422 = já existe no GitHub
        props.setProperty(chave, JSON.stringify({ arquivo: `${categoria}/${nome}`, original: arquivo.getName(),
          reserva: categoria === 'caseiras', criado: arquivo.getDateCreated().toISOString() }));
        if (r === 201) novos++;
      } else {
        Logger.log(`Falhou ${arquivo.getName()} (HTTP ${r})`);
      }
    }
    atualizarIndice_(token, slug, props);
    Logger.log(`[${slug}] ${novos} foto(s) nova(s)` + (acabou ? '' : ' · continua sozinho em 1 minuto'));
    if (!acabou) faltou = true;
  }
  // Não terminou? agenda a continuação para daqui 1 minuto, até acabar.
  if (faltou) ScriptApp.newTrigger('continuar').timeBased().after(60 * 1000).create();
}

function continuar() {
  ScriptApp.getProjectTriggers().forEach(t => { if (t.getHandlerFunction() === 'continuar') ScriptApp.deleteTrigger(t); });
  sincronizar();
}

function coletar_(pasta, categoria, lista) {
  const arquivos = pasta.getFiles();
  while (arquivos.hasNext()) {
    let f = arquivos.next();
    if (f.getMimeType() === 'application/vnd.google-apps.shortcut') {
      try {
        const alvo = f.getTargetId();
        try { coletar_(DriveApp.getFolderById(alvo), categoria || slug_(f.getName()), lista); continue; } catch (e) {}
        f = DriveApp.getFileById(alvo);
      } catch (e) { continue; }
    }
    if (f.getMimeType().indexOf('image/') === 0) lista.push({ arquivo: f, categoria: categoria || 'outros' });
  }
  const subpastas = pasta.getFolders();
  while (subpastas.hasNext()) {
    const p = subpastas.next();
    coletar_(p, categoria || slug_(p.getName()), lista);
  }
}

function slug_(txt) {
  txt = txt.trim().replace(/-\d{8}T\d{6}Z(-\d+)*$/, '').replace(/^fotos\s*-\s*/i, '');
  txt = txt.normalize('NFD').replace(/[̀-ͯ]/g, '');
  return txt.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'outros';
}

function nomeLimpo_(nome, id) {
  const ponto = nome.lastIndexOf('.');
  const base = ponto > 0 ? nome.slice(0, ponto) : nome;
  const ext = ponto > 0 ? nome.slice(ponto + 1).toLowerCase() : 'jpg';
  return `${slug_(base)}_${id.slice(0, 6)}.${ext}`;
}

function enviar_(token, caminho, bytes, mensagem, sha) {
  const corpo = { message: mensagem, content: Utilities.base64Encode(bytes), branch: CFG.branch };
  if (sha) corpo.sha = sha;
  const r = UrlFetchApp.fetch(`https://api.github.com/repos/${CFG.owner}/${CFG.repo}/contents/${encodeURI(caminho)}`, {
    method: 'put', contentType: 'application/json', muteHttpExceptions: true,
    headers: { Authorization: 'Bearer ' + token, Accept: 'application/vnd.github+json' },
    payload: JSON.stringify(corpo),
  });
  return r.getResponseCode();
}

function atualizarIndice_(token, slug, props) {
  const todas = props.getProperties(), indice = {};
  for (const [k, v] of Object.entries(todas)) if (k.indexOf(slug + ':') === 0) indice[k.slice(slug.length + 1)] = JSON.parse(v);
  const caminho = `${slug}/fotos/indice.json`;
  const atual = UrlFetchApp.fetch(`https://api.github.com/repos/${CFG.owner}/${CFG.repo}/contents/${caminho}?ref=${CFG.branch}`, {
    muteHttpExceptions: true, headers: { Authorization: 'Bearer ' + token, Accept: 'application/vnd.github+json' } });
  const sha = atual.getResponseCode() === 200 ? JSON.parse(atual.getContentText()).sha : undefined;
  enviar_(token, caminho, Utilities.newBlob(JSON.stringify(indice, null, 1)).getBytes(), 'índice de fotos', sha);
}

function instalarGatilho() {
  ScriptApp.getProjectTriggers().forEach(t => { if (t.getHandlerFunction() === 'sincronizar') ScriptApp.deleteTrigger(t); });
  ScriptApp.newTrigger('sincronizar').timeBased().onMonthDay(19).atHour(23).inTimezone('America/Sao_Paulo').create();
  // segunda chance, caso a primeira não termine em 6 minutos
  ScriptApp.newTrigger('sincronizar').timeBased().onMonthDay(20).atHour(1).inTimezone('America/Sao_Paulo').create();
}
