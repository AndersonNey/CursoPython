
from string import Template
from datetime import datetime


import os 
caminho = os.path.dirname(os.path.realpath(__file__))

with open(caminho + r'\template.html','r',encoding="utf-8") as html:
    template = Template(html.read())  #Template ta recebendo uma string de html.read()
    data_atual = datetime.now().strftime('%d/%m/%Y') #formatando a data
#   corpo_msg = template.substitute(nome='Carlos de Souza', data = data_atual)# ----->gera erro se nao tiver a mesma quantidade de parametros na funcao e placeholders no html
    corpo_msg = template.safe_substitute(nome='Carlos de Souza', data = data_atual)#->esse trecho é se por acaso tenha outro placeholder que eu nao tenho infomado o valor dele aqui
#                                                                                      ele simplesmente nao gera excecao e exibi o placeholder sem substituir. 
#                                                                                      ex: o rapaz $valor entrou dentro de casa. 
print(corpo_msg)

#placeholder = marcador de posição























