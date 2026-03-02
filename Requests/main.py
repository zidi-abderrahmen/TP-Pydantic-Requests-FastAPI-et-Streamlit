import requests

url = requests.get("https://httpbin.org/delay/10")

try:
    response = requests.get(url.text, timeout=5)
except requests.exceptions.Timeout as err:
    print(err)