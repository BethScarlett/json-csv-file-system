import json
from pathlib import Path

BASE_DIR = Path("JSON_Files")
res = BASE_DIR / "test_json.json"

def read_json(p:Path):
    """
    Take in File object (p) and print contents
    :param p:
    :return:
    """
    with open(p, "r", encoding="utf-8") as jsf:
        return json.load(jsf)