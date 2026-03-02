import requests

auth_token = "XXXXXXXX"

header = {
    "Authorization": f"Bearer {auth_token}"
}

url = "https://httpbin.org/headers"
response = requests.get(url, headers=header)
print(response.json())