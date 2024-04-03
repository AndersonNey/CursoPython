#entrar no site coletar dados 
#
#baixar duas bibliotecas
# pip install requests
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)

html = BeautifulSoup(response.text ,'html.parser')

#Pergando as perguntas
for pergunta in html.select('.s-post-summary'):
    titulo = pergunta.select_one('.s-link')
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.s-post-summary--stats-item-number')
    categorias = pergunta.select_one('.s-post-summary--meta-tags ')
    
    print(f'Data: {data.text}\nVotos: {votos.text}\nTitulo: {titulo.text}\nCategorias: {categorias.text} ')
    print()
    










