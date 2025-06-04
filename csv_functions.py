import csv
import pandas as pd
from pathlib import Path

BASE_DIR = Path("CSV_Files")
res = BASE_DIR / "test_csv.csv"

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

