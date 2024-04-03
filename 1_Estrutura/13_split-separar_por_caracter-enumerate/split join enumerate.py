"""
split- divide uma string em uma lista de strings depois de quebrar a string fornecida pelo separador especificado.
join -   é um método de string e retorna uma string na qual os elementos da sequência foram unidos pelo
separador str.
enumerate -
"""

X = "O Brasil é penta campeao, mas nao é hexa"
Y = X.split(",")
print(Y)


Z= ["aviao","carro","metro","moto","navio","trem"]
T = "-".join(Z)
print(T)

for cont , valor in enumerate(Z):
    print(cont,valor)