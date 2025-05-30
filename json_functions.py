import json
from pathlib import Path

BASE_DIR = Path("JSON_Files")
res = BASE_DIR / "test_json.json"

with open(res, "r", encoding="utf-8") as jsf:
    out = json.load(jsf)
    print(out)
