from urllib.request import urlopen

html = urlopen('https://receitas.globo.com/tipos-de-prato/macarrao/macarrao-simples-4dfa24dbd7001a3f8d0021ce.ghtml')
print(html.read())
