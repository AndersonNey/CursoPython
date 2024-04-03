from zipfile import ZipFile
import os


import os 
caminhobase = os.path.dirname(os.path.realpath(__file__))

caminho = caminhobase + r'\arquivos'

# ESCREVE
with ZipFile(caminhobase + r'\arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):      #somente os arquivos da pasta (nao entra em subpasta)
        caminho_completo = caminhobase + r'\arquivos' +'\\' +arquivo   #caminho completo do arquivo 
        zip.write(caminho_completo,arquivo) #de onde eu to dirando esse arquivo , e nome que eu to salvando
        

# LISTA
with ZipFile(caminhobase + r'\arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# EXTRAIR
with ZipFile(caminhobase + r'\arquivo.zip', 'r') as zip:
    zip.extractall(caminhobase + r'\descompactado')
