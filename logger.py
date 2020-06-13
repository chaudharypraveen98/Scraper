import datetime, os

BASE_DIR = os.path.dirname(__file__)
log_path = os.path.join(BASE_DIR, 'log')
os.makedirs(log_path, exist_ok=True)
now = datetime.datetime.now()
year = now.year


def log_save():
    filename = f"{year}.txt"
    filepath = os.path.join(log_path, filename)
    print(log_path)
    print(filepath)
    with open(filepath, 'w+') as f:
        f.write("hello")
