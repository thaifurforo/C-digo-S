import requests

# GET
gatinho_408 = requests.get("https://http.cat/408")

with open('408.jpeg', 'wb') as file:
    for chunk in gatinho_408:
        file.write(chunk)

print(gatinho_408.headers)

print(gatinho_408.status_code)

# alterar cabeçalhos no GET

url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)
# Cabeçalhos com X- no começo não são padrão da RFC

# POST

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)
