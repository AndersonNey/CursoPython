#!/usr/bin/env/ python3

# par executar no linux sem precisar falar o python 3.7  -->    ./nome_do_arquivo.py
#importante precisa ter esse cabeçalho superior no inicio do arquivo
#funciona so no linux essa parte de cima.


import sys
import os 
argumentos = sys.argv            #pelo oque eu entendi consigo pegar os comandos em uma lista dos que eu passei no cmd junto com o arquivo
qtd_argumentos = len(argumentos)

#espaços seria o criterio de separacao entre um argumento e outro

if qtd_argumentos <= 1:
    print('faltando argumnetos:')
    print('-a', 'Para listar todos os arquivos nesta pasta', sep='\t')
    print('-d', 'Para listar todos os diretorios nesta pasta',sep='\t')
    sys.exit("to saindo")  #aceita um argumneto de qualquer coisa imprimivel

so_arquivos=False
if '-a' in argumentos:
    so_arquivos = True

so_diretorios= False
if '-d' in argumentos:
    so_diretorios = True



for arquivo in os.listdir('.'):  #ponto significa diretorio atual, onde esta esse script
    if so_arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)

    if so_diretorios:
       if os.path.isdir(arquivo):
            print(arquivo)














