import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'

resposta = requests.get(url)

print('Status:', resposta.status_code)
print('Dados:', resposta.json())