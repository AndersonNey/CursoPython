
import os
import shutil

caminho = r'C:\Users\computador\Downloads\testes\pastaB'


for root ,dirs ,files in os.walk(caminho):
    for file in files:
        new_file_path = os.path.join(caminho,file)
        if '.txt' in file:
            os.remove(new_file_path)


