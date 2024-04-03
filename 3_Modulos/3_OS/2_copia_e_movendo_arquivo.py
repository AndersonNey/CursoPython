
import os
import shutil

caminho_original = r'C:\Users\computador\Downloads\testes\pastaA'
caminho_novo = r'C:\Users\computador\Downloads\testes\pastaB'

try:
    os.mkdir(caminho_novo)  #criando um caminho novo

except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe')



for root ,dirs ,files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root,file)
        new_file_path = os.path.join(caminho_novo,file)

        if '.txt' in file:
            
            #Copiando

            shutil.copy(old_file_path, new_file_path)
            print(f'Arquivo {file} copiado com sucesso')

            #Movendo

            #shutil.move(old_file_path,new_file_path)                #tambem tem como renomear o arquivo comm esse comando
            #print(f'Arquivo {file} movido com sucesso')