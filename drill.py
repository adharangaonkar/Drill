import csv
from pathlib import Path
import json

DATA_DIR = Path("data")
HISTORY_FILE = DATA_DIR / "history.json"

def load_csv(filename: str) -> list[dict]:
    filepath = DATA_DIR / filename
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]
    return rows

def load_history() -> dict:
    if not HISTORY_FILE.exists():
        return {}
    with open(HISTORY_FILE, encoding="utf-8") as f:
        return json.load(f)

def save_history(history: dict) -> None:
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2)


if __name__ == "__main__":
    history = load_history()
    print("History:", history)

    # simulate saving today's entry
    from datetime import date
    history[date.today().isoformat()] = {
        "topics": "Backpropagation",
        "leetcode_python": "Two Sum",
        "leetcode_sql": "Rank Scores"
    }
    save_history(history)
    print("Saved. Check data/history.json")