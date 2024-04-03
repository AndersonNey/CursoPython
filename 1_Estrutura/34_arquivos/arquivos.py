#lembrando que quando ele salva o arquivo cursor fica na posiçao no final e se rodar o comando para ler o arquivo ele executar do cursor em diante , ou seja ,
#nao aparece nada , tem que voltar o cursor para o inicio novamente

#Maneira que normalmente ultilizam para abrir os arquivos

# try:
#     file = open('C:/PYTHON VSCODE/Python (Aulas)/aula 41 (arquivos)/abc.txt','w+')
#     file.write('linha')
#     file.seek(0)
#     print(file.read())
# finally:
#     file.close()


#o modo 'a' coloca o cursor no final do arquivo e por isso da para ficar acrescentando valores

#import os      #seria usado so la no final


file = open('C:/PYTHON VSCODE/Python (Aulas)/aula 41 (arquivos)/abc.txt','w+')  #criando o arquivo  (usando '\' no caminho deu erro precisei trocar por '/')
file.write('linha1\n')
file.write('linha2\n')
file.write('linha3\n')

file.seek(0,0)  # voltando o cursor para o inicio de volta          offset |  whence   ---> 2 parametros necessarios
print('Lendo linhas:')
print(file.read())
file.seek(0,0)
print('1#############')

print(file.readline(), end='')   #lendo uma unica linha     | end =''  serve para nao mandar uma quebra de linha
print(file.readline(), end='')
file.seek(0,0)

print('2#############')

print(file.readlines())       #colocando dentro de uma lista                     
file.seek(0,0)

print('3#############')

for linha in file.readlines():
    print(linha,end ='')

file.seek(0,0)

print('4#############')    #mesma coisa que o de cima , mas de outra maneira

for linha in file:                            #lembrando que file é o nome do arquivo que eu defini la em cima
    print(linha,end ='')

file.seek(0,0)


file.close()    #fechando o arquivo


print('outra Maneira  -----------------------------------------------------------------------------------------')

try:
    file=open('abc.txt','w+')
    file.write('linha')
    file.seek(0)
    print(file.read())
finally:
    file.close()

print('USANDO GERENCIADOR DE CONTEXTO')

#nao precisa mandar fechar o arquivo com o gerenciador de contexto 

with open('abc.txt','w+') as file:
    file.write('linha 1\n')
    file.write('linha 2\n')
    file.write('linha 3\n')

    file.seek(0)
    print(file.read())

with open('abc.txt','r') as file:
    file.seek(0)
    print(file.read())


with open('abc.txt','a+') as file:     #'o A+ colocar o cursor no final do arquivo e acrescenta'
    file.write('outralinha')
    file.seek(0)
    print(file.read())


#os.remove('C:/PYTHON VSCODE/Python (Aulas)/aula 41 (arquivos)/abc.txt')