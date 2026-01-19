import json, os, zipfile, pathlib

MANIFEST = pathlib.Path("bots/hello-bot/manifest.json")
SRC_DIR  = pathlib.Path("bots/hello-bot/src")
DIST_DIR = pathlib.Path("dist")

def main():
    DIST_DIR.mkdir(exist_ok=True)
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    name, version = data["name"], data["version"]
    out = DIST_DIR / f"{name}-{version}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(MANIFEST, arcname="manifest.json")
        for p in SRC_DIR.rglob("*"):
            if p.is_file():
                z.write(p, arcname=f"src/{p.name}")
    print(out)

if __name__ == "__main__":
    main()
