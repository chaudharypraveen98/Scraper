import requests

url = "http://9d44e5091b7d.ngrok.io"
endpoint = f'{url}/box-office'
r = requests.post(endpoint, json={})
print(r.text)
