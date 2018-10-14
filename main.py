from urllib.request import urlopen
from bs4 import BeautifulSoup

# Especifica a url de onde será buscado
url = "http://localhost/example.html"

# Carrega o website e retorna o html para a variável 'page'  
page = urlopen(url)

# Faz o parse da html na variável 'soup'
soup = BeautifulSoup(page, "html.parser")

# Print do resultado
print (soup)

