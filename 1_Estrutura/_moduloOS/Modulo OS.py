"""
https://levitrares.com/host-https-qastack.com.br/programming/1099300/whats-the-difference-between-getpath-getabsolutepath-and-getcanonicalpath

https://docs.python.org/pt-br/3/library/os.path.html#module-os.path

Considere estes nomes de arquivos:

C:\temp\file.txt - Este é um caminho, um caminho absoluto e um caminho canônico.

.\file.txt- Este é um caminho. Não é um caminho absoluto nem um caminho canônico.

C:\temp\myapp\bin\..\\..\file.txt- Este é um caminho e um caminho absoluto. Não é um caminho canônico.

Um caminho canônico é sempre um caminho absoluto.

A conversão de um caminho para um caminho canônico o torna absoluto (geralmente adere ao diretório de trabalho atual, por 
exemplo, ./file.txttorna-se c:/temp/file.txt). O caminho canônico de um arquivo apenas "purifica" o caminho, removendo e 
resolvendo coisas como ..\e resolvendo links simbólicos (em unixes).

os.path.split(path)
os.path.dirname(path)


"""


import os

print(__file__)  #__file__ é uma variável que contém o caminho para o módulo que está sendo importado no momento.
print(os.path.realpath(__file__))        # especie de tratamento 
print(os.path.dirname(os.path.realpath(__file__)))   #remove o nome do arquivo