from flask import Flask
from scrapper import run as scrapper_runner
from logger import log_save

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return "hello world"


@app.route("/abc", methods=['GET'])
def abc():
    return "hello abc"


@app.route("/box-office", methods=['POST'])
def box_office_view():
    log_save()
    scrapper_runner()
    return "done"
