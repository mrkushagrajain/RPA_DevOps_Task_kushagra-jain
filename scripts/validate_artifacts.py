import json, pathlib, sys

def validate_manifest(path: pathlib.Path):
    if not path.exists():
        raise FileNotFoundError(f"{path} not found")
    data = json.loads(path.read_text(encoding="utf-8"))
    required = ["name", "version", "description"]
    missing = [k for k in required if k not in data]
    if missing:
        raise ValueError(f"manifest.json missing keys: {missing}")
    print(f"Manifest OK: {data['name']}@{data['version']}")

if __name__ == "__main__":
    manifest = pathlib.Path("bots/hello-bot/manifest.json")
    validate_manifest(manifest)
