# scripts/collect_logs.py
import pathlib, sys

LOGS = pathlib.Path("logs")
REPORTS = pathlib.Path("reports/junit")

def main():
    LOGS.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    print("Collected logs at:", LOGS.resolve())
    print("Collected reports at:", REPORTS.resolve())

if __name__ == "__main__":
    main()
