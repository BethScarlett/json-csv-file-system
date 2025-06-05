from pathlib import Path
from csv_functions import convert_to_json

def csv_select():
    p = Path(input("Please enter the file path: "))
    if Path.exists(p):
        print(f'JSON matches CSV? {convert_to_json(p)}')
    else:
        print('Invalid path')

if __name__ == '__main__':
    csv_select()