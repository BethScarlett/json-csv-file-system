import csv
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
            print(f"{category_names[0].title()}: {row[0]}, "
                  f"{category_names[1].title()}: {row[1]}, "
                  f"{category_names[2].title()}: {row[2]}, "
                  f"{category_names[3].title()}: {row[3]}, "
                  f"{category_names[4].title()}: {row[4]}, "
                  f"{category_names[5].title()}: {row[5]} ")