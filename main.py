import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(f"response: {response.text}")
if response.status_code != 200:
    print('error')

data = response.json()
print(f"data: {data}")
