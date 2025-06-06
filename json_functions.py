import json
from pathlib import Path

def read_json(p:Path):
    """
    Take in File object (p) and print contents
    :param p:
    :return:
    """
    with open(p, "r", encoding="utf-8") as jsf:
        return json.load(jsf)