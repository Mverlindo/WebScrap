# https://camboriu.sc.gov.br/#
import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.olx.com.br/").content

soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())