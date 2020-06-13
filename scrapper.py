import requests
from requests_html import HTML
import datetime
import os, sys
import pandas as pd

BASE_DIR = os.path.dirname(__file__)


def url_to_text(url, filename="world.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(filename, 'w') as f:
                f.write(html_text)
        return html_text
    return None


def pharse_and_extract(url, name=2020):
    html_text = url_to_text(url)
    if html_text is None:
        return ""
    r_html = HTML(html=html_text)
    table_class = ".imdb-scroll-table"
    r_table = r_html.find(table_class)
    table_data = []

    if len(r_table) == 1:
        table = r_table[0]
        header_col = table.find("th")
        header_names = [x.text for x in header_col]
        rows = table.find("tr")
        for row in rows[1:]:
            cols = row.find("td")
            row_data = []
            for i, col in enumerate(cols):
                row_data.append(col.text)
            table_data.append(row_data)
    path = os.path.join(BASE_DIR, 'data')
    os.makedirs(path, exist_ok=True)
    filepath = os.path.join('data', f'{name}.csv')
    df = pd.DataFrame(table_data, columns=header_names)
    df.to_csv(filepath, index=False)


def run(start_year=None, year_ago=1):
    if start_year is None:
        now = datetime.datetime.now()
        start_year = now.year
    assert isinstance(start_year, int)
    assert len(str(start_year)) == 4
    for i in range(0, year_ago + 1):
        url = f"https://www.boxofficemojo.com/year/world/{start_year}"
        pharse_and_extract(url, name=start_year)
        print(start_year)
        start_year -= 1


"""if __name__ == '__main__':
    try:
        start = int(sys.argv[1])
    except:
        start = None
    try:
        count = int(sys.argv[2])
    except:
        count = 1
    run(start_year=start, year_ago=count)
"""