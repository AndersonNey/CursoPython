import json

# cuidado para nao confudir dump , dumps ,load , loads

#links realmente uteis
# https://www.geeksforgeeks.org/python-difference-between-json-dump-and-json-dumps/#:~:text=dump()%20method%20used%20to,object%20into%20JSON%20formatted%20String.
# https://www.geeksforgeeks.org/working-with-json-data-in-python/
# https://www.geeksforgeeks.org/python-difference-between-json-load-and-json-loads/

#gravando  usando dumps  "converte o dicionario para um objeto json"(organiza)

cliente1 = {'ID':'1','Nome': 'alice', 'CNPJ': '12344', 'Nome Fantasia': 'alice_eer'}

json_objeto = json.dumps(cliente1, indent=4 )
with open('C:/PYTHON VSCODE/Python (Aulas)/_arquivo JSON/dados.json', 'a+') as arquivo:
        arquivo.write(json_objeto)
    
        


#gravando  usando dump  (Nao organiza)



# cliente2 = {'ID':'1','Nome': 'alice', 'CNPJ': '12344', 'Nome Fantasia': 'alice_eer'}

# with open('C:/PYTHON VSCODE/Python (Aulas)/_arquivo JSON/dados.json', 'a+') as arquivo:
#     json.dump(cliente2, arquivo )



        
#lembrando que se a estrutura dos dados no JSON estiver errada essa funcao nao funciona , as duas funçoes LOAD e LOADS tiram o dicionario da string exemplo: "{}"
#lendo o arquivo com LOAD


with open('C:/PYTHON VSCODE/Python (Aulas)/_arquivo JSON/dados.json', 'r') as arquivo:
    json_object = json.load(arquivo) 
  
print(json_object) 
print(type(json_object)) 



#lendo o arquivo com LOADS    maneira diferente que deu certo

with open('C:/PYTHON VSCODE/Python (Aulas)/_arquivo JSON/dados.json', 'r') as arquivo:
    json_dados = arquivo.read()
    json_dados  =json.loads(json_dados)

print(json_dados)
print(type(json_dados))   
