import random

# Gera um número inteiro entra A e B
inteiro = random.randint(10,20)  
print(inteiro)

# Gerar um número aleatório usando a função random.randrange que é muito semelhante a range()
outro_inteiro = random.randrange(900,1000,10)
print(outro_inteiro)

# Gera um número de ponto flutuante entra A e B
flutuante = random.uniform(10,20)  
print(flutuante)

# Gera um número de ponto flutuante entre 0 e 1
outro_flutuante = random.random()
print(outro_flutuante)

#fazer um sorteio com base na lista
lista = ['Luiz', 'Otávio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']
sorteio1 = random.choice(lista) #retorna 1 item da lista
print(sorteio1)
sorteio2 = random.choices(lista, k=2)  #retorna uma lista com k items aleatorios
print(sorteio2)
sorteio3 = random.sample(lista , 2)  #faz a mesma coisa que o decima so que nao retorna valores iguais
print(sorteio3)


#Embaralhando uma lista
lista2 = ['Luiz', 'Otávio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']
random.shuffle(lista2)
print(lista2)


import string

#Gera senha aleatoria
                                # string.ascii_lowercase so minuscula
                                # string.ascii_uppercase so maiuscula
letras = string.ascii_letters  #retorna maiusculas e minusculas
digitos = string.digits
caracteres = '!@#$%&*._-'
geral = letras+digitos+caracteres

senha = "".join(random.choices(geral, k=20))
print(senha)

















