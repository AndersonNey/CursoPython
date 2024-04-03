#startswith checa se a variavel começa com um caracter/palavra especifica


variavel = ['Joao', 'Maria', 'Tiao']

for valor in variavel:
    if valor.lower().startswith('j'): #Checar se variavel começa com J - startswith("intem a ser encontrado",inicio,fim) -
        print("começa com J : ", valor)
    else:
        print("nao possui essa letra")