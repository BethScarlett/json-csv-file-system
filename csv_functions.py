import csv
import logging
import pandas as pd
from pathlib import Path
from json_functions import read_json

def read_csv(f:Path):
    with open(f, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file, delimiter=",")
        line_num = 0
        for row in csv_reader:
            if line_num == 0:
                print(f"The column names are " + ",".join(row))
                line_num += 1
                category_names = row
            else:
                #Tie catagory names to each value in row for easier printing
                zpd = zip(category_names, row)
                for r in zpd:
                    print(f"{r[0]}: {r[1]}")

def convert_to_json(f:Path) -> bool:
    #Generate new path
    new_path = Path(f'{f.parent.resolve()}/{f.stem}.json')

    #Read file and convert to JSON using new path
    temp = pd.read_csv(f)
    temp.to_json(new_path, orient='records', force_ascii=False, indent=1)

    return validate_json_conversion(new_path, f)

def validate_json_conversion(json_path: Path, csv_path: Path):
    js = read_json(json_path)
    with open(csv_path, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file, delimiter=",")
        jcats = [k for k in js[0].keys()]
        for i, row in enumerate(csv_reader):
            if i == 0:
                if row != jcats:
                    return False
            else:
                jrow = [str(v) for v in js[i-1].values()]
                cleanrow = []
                for v in row:
                    if v == 'false' or v == 'true':
                        v = v.title()
                    cleanrow.append(v)

                if cleanrow != jrow:
                    return False
        return True

#Predefine logger fo use when required
def config_logger():
    logging.basicConfig(level=0,                                            #Level to start logging at
                        filename="log.txt",                                 #Name of file to write log to
                        filemode="w",                                       #Filemode to open file in (Note: 'w' will create file if it doesn't exist)
                        format="{asctime} - {levelname} - {message}",       #Format string to desired look (asctime = current time & date, more can be found in python docs)
                        style="{"                                           #Define style for formatting
                        )