import requests
from bs4 import BeautifulSoup

url = 'https://example.com'

pagina = requests.get(url)

soup = BeautifulSoup(pagina.text, 'html.parser')

print('Título da página:')
print(soup.title.text)
