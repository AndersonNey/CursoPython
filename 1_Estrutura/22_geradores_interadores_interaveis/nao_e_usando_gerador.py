import random

lista1 = []
dicionario_de_verificaçao = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}
cont = 0
total_de_lancamentos = 10000


for x in range(total_de_lancamentos):
    resultado = random.randint(1, 6)
    lista1.append(resultado)

for y, z in dicionario_de_verificaçao.items():
    for t in lista1:
        if t == y:
            cont += 1
            dicionario_de_verificaçao[y] = cont
    cont = 0

# exibir melhor
for k, l in dicionario_de_verificaçao.items():
    # regra de 3
    regra_de_3 = (100 * l) / total_de_lancamentos
    print(f'o numero [{k}] caiu {l} vezes,ou seja, {regra_de_3:.2f}%')