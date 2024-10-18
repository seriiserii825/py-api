import requests

params = {
    'lat': 47.010452,
    'lng': 28.863810,
    'formatted': 0
}
url = 'https://api.sunrise-sunset.org/json'
response = requests.get(url, params=params)
response.raise_for_status()
if response.status_code != 200:
    print('error')

data = response.json()
print(f"data: {data['results']['sunrise'].split('T')[1].split(':')[0]}")
