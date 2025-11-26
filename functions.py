from fastapi import File, UploadFile
import csv
from classes.soldier.soldiers import Soldiers
from data import soldier_table, houses_table
# from main import soldier_table
# from main import soldier_table


# function that gets the file and return rows and columns
def csv_reader(csv_content: UploadFile):
    text = csv_content.file.read().decode()
    reader = csv.reader(text.splitlines())
    rows = []
    rows = [row for row in reader]
    columns = rows[0]
    # rows = rows[1:]

    soldier_table.add_csv_soldiers(rows)
    res = houses_table.add_full_soldier_to_houses(soldier_table.class_soldiers)

    return {
         "soldiers in houses":res,
         "on the waiting list":len(soldier_table.class_soldiers)-res,
        "all soldiers": soldier_table.class_soldiers,
    }


    # db = sqlite_connector()
