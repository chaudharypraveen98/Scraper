from fastapi import FastAPI
from scraper import run as scraper_runner
from logger import log_save
import os
import pandas as pd

app = FastAPI()

current = (os.path.join(os.getcwd(), 'data'))
os.makedirs(current, exist_ok=True)
file = os.path.join(current, "box_office_cleaned.csv")


@app.get("/box-office-collect")
def abc():
    df = pd.read_csv(file)
    return df.to_dict("Rank")


@app.post("/box-office")
def box_office():
    log_save()
    scraper_runner()
    return {"data": [1, 2, 3]}
