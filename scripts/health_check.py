# scripts/health_check.py
import json, time, random, pathlib

OUT = pathlib.Path("logs")
OUT.mkdir(exist_ok=True)

if __name__ == "__main__":
    # fake health metrics
    status = {
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "control_room_reachable": True,
        "avg_cpu": random.randint(10, 60),
        "queue_depth": random.randint(0, 5),
    }
    print(json.dumps(status))
    (OUT / "health.json").write_text(json.dumps(status, indent=2), encoding="utf-8")
