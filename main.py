from fastapi import FastAPI, UploadFile, File
from datetime import datetime
from functions import csv_reader
from data import houses_table,soldier_table
import uvicorn

import csv

app = FastAPI()





# get csv file with post method
@app.post("/assignWithCsv")
def get_file(file: UploadFile = File()):
    if not "csv" in file.content_type:
        return {"msg": f"content_type: `{file.content_type}` not allowed!"}
    result = csv_reader(file)
    return result


@app.get("/space")
def space_geter():
    result = houses_table.get_houses_space()
    return result

@app.get('/waitingList')
def gets_waitingList():
    result = soldier_table.get_thet_wait()
    return result
@app.get('/search/{soldier_id}')
def gets_soldier(soldier_id):
    result = soldier_table.get_soldier_by_id(soldier_id)
    return result