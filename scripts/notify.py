# scripts/notify.py
import argparse, time, pathlib

ALERTS = pathlib.Path("logs/alerts")
ALERTS.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--subject", required=True)
    p.add_argument("--message", required=True)
    p.add_argument("--to", default="ops@example.com")
    args = p.parse_args()

    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] ALERT to {args.to}: {args.subject} -> {args.message}"
    print(line)

    # write a stub "email"
    out = ALERTS / f"{int(time.time())}-{args.subject.replace(' ','_')}.txt"
    out.write_text(line + "\n", encoding="utf-8")
