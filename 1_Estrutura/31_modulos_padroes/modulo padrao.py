# Modulos padrao do Python:
# Modulos sao arquivos .py (que contem codigo python) e servem para expandir 
# As funcionalidades padrao da linguagem.
# Veja todos os modulos padrao do python em:
# https://docs.python.org/3/py-modindex.html


#A maneira que é importado pode influenciar

#import sys                         Importando o modulo inteiro
#print(sys.platform)



#from sys import platform           Importando do modulo sys a funçao platform
#print(platform)


#from sys import platform  as so       # 'as' serve para tipo dar um apelido
#print(so)


#TER CUIDADO PARA NAO SOBREESCREVER UMA FUNÇAO IMPORTADA
#EX:
#
#
from random import randint

def randint(*args):       # o ideal para nao acontecer isso é so mudar o nome da minha funçao ou dar um apelido para a 
    return 'hahaha'       # funçao padrao do python  usando exemplo: 'from random import randint as rd' ou 
                          # importa o modulo inteiro que evita esse problema exemplo: import random      random.randint()

for i in range(10):
    print(randint(0,10))
    

#from random import *               Importando do modulo random  tudo

#from random import randint , random      Outra maneira de importa funçoes 


#instalar modulo       pip install
#desinstalar modulo    pip uninstall