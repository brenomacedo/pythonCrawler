from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.climatempo.com.br/').content
soup = BeautifulSoup(site, 'html.parser')

# temperatura = soup.find("span")
# print(temperatura.string())

print(soup.prettify())
