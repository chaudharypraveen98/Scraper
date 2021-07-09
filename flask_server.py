from flask import Flask
from scraper import run as scraper_runner
from logger import log_save

app = Flask(__name__)

@app.route("/box-office", methods=['POST'])
def box_office_view():
    log_save()
    scraper_runner()
    return "done"
