"""Copia as fotos novas do Drive de cada cliente para <slug>/fotos/<categoria>/.

- Lê drive.json ({slug: {pasta_drive, pastas_de_reserva}}).
- Percorre a pasta e as subpastas (seguindo atalhos).
- A categoria é o nome da subpasta de primeiro nível, sem o sufixo de exportação
  do Drive (-20261001T005120Z-1-001), em minúsculas e sem acento.
- Converte para JPEG (inclusive HEIC), maior lado no máximo 2000 px.
- Não copia de novo: guarda o id de cada arquivo em <slug>/fotos/indice.json.
"""
import io, json, os, re, unicodedata, pathlib, sys
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from PIL import Image, ImageOps
import pillow_heif
pillow_heif.register_heif_opener()

ROOT = pathlib.Path(__file__).resolve().parents[1]
FOLDER = "application/vnd.google-apps.folder"
SHORTCUT = "application/vnd.google-apps.shortcut"
MAX = 2000

creds = service_account.Credentials.from_service_account_info(
    json.loads(os.environ["GDRIVE_SA_KEY"]), scopes=["https://www.googleapis.com/auth/drive.readonly"])
drive = build("drive", "v3", credentials=creds, cache_discovery=False)

def slug(txt):
    txt = re.sub(r"-\d{8}T\d{6}Z(-\d+)*$", "", txt.strip())
    txt = unicodedata.normalize("NFKD", txt).encode("ascii", "ignore").decode()
    txt = re.sub(r"^fotos\s*-\s*", "", txt, flags=re.I)
    return re.sub(r"[^a-z0-9]+", "-", txt.lower()).strip("-") or "outros"

def listar(pasta):
    tok = None
    while True:
        r = drive.files().list(q=f"'{pasta}' in parents and trashed=false",
            fields="nextPageToken, files(id,name,mimeType,shortcutDetails,createdTime)",
            pageSize=1000, pageToken=tok, supportsAllDrives=True, includeItemsFromAllDrives=True).execute()
        yield from r.get("files", [])
        tok = r.get("nextPageToken")
        if not tok: break

def resolver(f):
    if f["mimeType"] == SHORTCUT:
        d = f.get("shortcutDetails", {})
        return {"id": d.get("targetId"), "name": f["name"], "mimeType": d.get("targetMimeType", ""), "createdTime": f.get("createdTime")}
    return f

def percorrer(pasta, categoria=None):
    for f in listar(pasta):
        f = resolver(f)
        if not f["id"]: continue
        if f["mimeType"] == FOLDER:
            yield from percorrer(f["id"], categoria or slug(f["name"]))
        elif f["mimeType"].startswith("image/"):
            yield categoria or "outros", f

def baixar(fid):
    buf = io.BytesIO()
    dl = MediaIoBaseDownload(buf, drive.files().get_media(fileId=fid, supportsAllDrives=True))
    done = False
    while not done: _, done = dl.next_chunk()
    buf.seek(0); return buf

total = 0
for cliente, cfg in json.loads((ROOT / "drive.json").read_text()).items():
    base = ROOT / cliente / "fotos"; base.mkdir(parents=True, exist_ok=True)
    idx_path = base / "indice.json"
    indice = json.loads(idx_path.read_text()) if idx_path.exists() else {}
    novos = 0
    for categoria, f in percorrer(cfg["pasta_drive"]):
        if f["id"] in indice: continue
        try:
            im = ImageOps.exif_transpose(Image.open(baixar(f["id"]))).convert("RGB")
        except Exception as e:
            print(f"[{cliente}] pulei {f['name']}: {e}", file=sys.stderr); continue
        im.thumbnail((MAX, MAX))
        nome = f"{slug(pathlib.Path(f['name']).stem)}_{f['id'][:6]}.jpg"
        destino = base / categoria / nome; destino.parent.mkdir(parents=True, exist_ok=True)
        im.save(destino, "JPEG", quality=90)
        indice[f["id"]] = {"arquivo": f"{categoria}/{nome}", "original": f["name"], "criado": f.get("createdTime"),
                           "reserva": categoria in cfg.get("pastas_de_reserva", [])}
        novos += 1
    idx_path.write_text(json.dumps(indice, ensure_ascii=False, indent=1))
    print(f"[{cliente}] {novos} foto(s) nova(s)"); total += novos
print(f"total: {total}")
