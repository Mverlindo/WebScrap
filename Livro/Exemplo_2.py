from urllib.request import urlopen # Importa o Urllib
from bs4 import BeautifulSoup # Importa O BeatifulSoup
# Busca a pagina a grava ela na variavel html
html = urlopen('http://www.pythonscraping.com/pages/page1.html') 
# 
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.title)
