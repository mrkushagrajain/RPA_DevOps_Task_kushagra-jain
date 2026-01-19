# scripts/aa_deploy.py
import argparse, json, pathlib, time, yaml, sys, os
from typing import Dict, Any
from xml.etree.ElementTree import Element, SubElement, tostring  # for JUnit

LOGS = pathlib.Path("logs")
LOGS.mkdir(exist_ok=True)
REPORTS = pathlib.Path("reports/junit")
REPORTS.mkdir(parents=True, exist_ok=True)

def log(msg):
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    (LOGS / "deploy.log").open("a", encoding="utf-8").write(line + "\n")

def write_junit(env: str, ok: bool, message: str):
    """
    Write a single-test JUnit XML so Azure DevOps can show deploy pass/fail.
    """
    suite = Element("testsuite", name=f"deploy-{env}", tests="1", failures="0" if ok else "1")
    case = SubElement(suite, "testcase", classname="deploy", name=f"deploy-{env}")
    if not ok:
        fail = SubElement(case, "failure", message=message)
        fail.text = message
    out_path = REPORTS / f"deploy-{env}.xml"
    out_path.write_bytes(tostring(suite, encoding="utf-8"))
    log(f"Wrote JUnit report: {out_path}")

def load_secrets(secrets_file: str) -> Dict[str, str]:
    env = {
        "A360_BASE_URL": os.getenv("A360_BASE_URL"),
        "A360_CLIENT_ID": os.getenv("A360_CLIENT_ID"),
        "A360_CLIENT_SECRET": os.getenv("A360_CLIENT_SECRET"),
        "A360_TENANT": os.getenv("A360_TENANT", "default"),
    }
    if all(v for v in env.values() if v is not None):
        return env
    data = yaml.safe_load(open(secrets_file, "r", encoding="utf-8"))
    return {
        "A360_BASE_URL": data.get("A360_BASE_URL", "https://example-a360.company.com"),
        "A360_CLIENT_ID": data.get("A360_CLIENT_ID", "mock-client-id"),
        "A360_CLIENT_SECRET": data.get("A360_CLIENT_SECRET", "mock-secret"),
        "A360_TENANT": data.get("A360_TENANT", "default"),
    }

# ----- Mocked REST flow -----
def mock_auth(base_url: str, client_id: str, tenant: str) -> str:
    log(f"(MOCK REST) POST {base_url}/oauth2/token  tenant={tenant} client_id={client_id}")
    time.sleep(0.2)
    log("(MOCK REST) 200 OK  access_token=***")
    return "mock-access-token"

def mock_upload(base_url: str, token: str, artifact: str) -> Dict[str, Any]:
    log(f"(MOCK REST) POST {base_url}/repository/packages  Authorization=Bearer ***  file={artifact}")
    time.sleep(0.3)
    pkg = {"id": "pkg-123", "name": pathlib.Path(artifact).name, "version": "1.0.0"}
    log(f"(MOCK REST) 201 Created  package_id={pkg['id']}")
    return pkg

def mock_deploy(base_url: str, token: str, cfg: Dict[str, Any], pkg: Dict[str, Any]):
    payload = {
        "folder": cfg["a360"]["folder"],
        "queue": cfg["a360"]["queue"],
        "packageId": pkg["id"],
        "concurrency": cfg["deploy"].get("concurrency", 1),
    }
    log(f"(MOCK REST) POST {base_url}/deployments  Authorization=Bearer ***  payload={json.dumps(payload)}")
    time.sleep(0.3)
    log("(MOCK REST) 202 Accepted  deployment=started")
    time.sleep(0.3)
    log("(MOCK REST) 200 OK  deployment=success")

def mock_upload_and_deploy(env, artifact, cfg, secrets):
    base = secrets["A360_BASE_URL"].rstrip("/")
    token = mock_auth(base, secrets["A360_CLIENT_ID"], secrets["A360_TENANT"])
    pkg = mock_upload(base, token, artifact)
    mock_deploy(base, token, cfg, pkg)
    log("(MOCK) End-to-end mocked deployment succeeded")
    return True, "success"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--env", required=True, choices=["dev","test","prod"])
    ap.add_argument("--artifact", required=True)
    ap.add_argument("--mock", action="store_true")
    ap.add_argument("--secrets-file", default="configs/secrets.sample.yaml")
    args = ap.parse_args()

    cfg = yaml.safe_load(open(f"configs/envs/{args.env}.yaml", "r", encoding="utf-8"))
    secrets = load_secrets(args.secrets_file)

    if args.mock:
        ok, msg = mock_upload_and_deploy(args.env, args.artifact, cfg, secrets)
    else:
       
        ok, msg = False, "real mode not implemented for demo"

    write_junit(args.env, ok, msg)
    sys.exit(0 if ok else 2)

if __name__ == "__main__":
    main()
