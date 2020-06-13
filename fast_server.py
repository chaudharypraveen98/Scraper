from fastapi import FastAPI
from scrapper import run as scrapper_runner
from logger import log_save

app = FastAPI()


@app.get("/")
def hello_world():
    return {"hello": "world"}


@app.get("/abc")
def abc():
    return {"hello": "abc"}


@app.post("/box-office")
def box_office():
    log_save()
    scrapper_runner()
    return {"data": [1, 2, 3]}
