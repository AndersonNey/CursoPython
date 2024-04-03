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
lancarquantidade=1000

def jogar_dado():
    resultado = random.randint(1, 6)
    yield resultado


for x in  range(lancarquantidade):
    lancamento=jogar_dado()
    resultado_final=next(lancamento)
    for k ,  l in dicionario_de_verificaçao.items():
        if  k == resultado_final:
            pegar_valor_e_somar=dicionario_de_verificaçao[k]
            cont= pegar_valor_e_somar+1
            dicionario_de_verificaçao[k]=cont


# exibir melhor
for p , q in dicionario_de_verificaçao.items():
    print(f'o numero [{p}] caiu {q} vezes')