

# poderia importar assim tambem

# from vendas.calc_preco import aumento
# preco = 49.90
# preco_com_aumento0 = aumento(preco,15) 
# print(preco_com_aumento0)



import vendas.calc_preco

preco = 49.90

preco_com_aumento = vendas.calc_preco.aumento(valor=preco,porcentagem= 15,formata= True)  #valor a ser aumentado e porcentagem a ser aplicada
print(preco_com_aumento)

preco_com_reducao = vendas.calc_preco.reducao(valor=preco,porcentagem= 15,formata= True)  #valor a ser reduzido e porcentagem a ser aplicada
print(preco_com_reducao)