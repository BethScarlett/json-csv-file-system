import csv
import pandas as pd
from pathlib import Path
from json_functions import read_json

BASE_DIR = Path("CSV_Files")
res = BASE_DIR / "test_csv.csv"

def read_csv(f:Path):
    with open(res, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file, delimiter=",")
        line_num = 0
        for row in csv_reader:
            if line_num == 0:
                print(f"The column names are " + ",".join(row))
                line_num += 1
                category_names = row
            else:
                zpd = zip(category_names, row)
                for r in zpd:
                    print(f"{r[0]}: {r[1]}")

def convert_to_json(f:Path) -> None:
    #Generate new path
    new_path = f.parent.parent / 'JSON_Files' / f'{f.stem}.json'

    #Read file and convert to JSON using new path
    temp = pd.read_csv(f)
    temp.to_json(new_path, orient='records', force_ascii=False, indent=1)

def validate_json_conversion(p1: Path, p2: Path):
    js = read_json(p1)
    with open(p2, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file, delimiter=",")
        jcats = [k for k in js[0].keys()]
        for i, row in enumerate(csv_reader):
            if i == 0:
                if row == jcats:
                    print("Categories ok")
                else:
                    print("No match")
                    return False
            else:
                jrow = [str(v) for v in js[i-1].values()]
                print(row)
                print(jrow)
                if row == jrow:
                    print("Categories ok")
                else:
                    print("No match")
                    return False
        return True

p = res.parent.parent / 'JSON_Files' / f'{res.stem}.json'
print(f'JSON matches CSV? {validate_json_conversion(p,res)}')