from pathlib import Path
from dekorator import timer, required_columns
import csv, json

@required_columns({"name", "age", "city"})
@timer
def read_csv(path: str):
    with Path(path).open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


@timer
def write_json(path: str, data):
    with Path(path).open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


@timer
def write_text(path: str, text: str):
    Path(path).write_text(text, encoding="utf-8")
