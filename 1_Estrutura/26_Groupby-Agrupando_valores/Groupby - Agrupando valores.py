from itertools import groupby , tee  #essa funçao groupby precisa que o dicionario esteja organizado | é obrigatorio organizar primeiro depois usar a funçâo
                                     # a funçao tee sera usado no exemplo 5, mas basicamente criar copias de interadores
alunos0 = [
    {'nome':'Luiz', 'nota': 'A'},
    {'nome':'Letícia', 'nota': 'B'},
    {'nome':'Fabrício', 'nota': 'A'},
    {'nome':'Rosemary', 'nota': 'C'},
    {'nome':'Joana', 'nota': 'D'},
    {'nome':'João', 'nota': 'A'},
    {'nome':'Eduardo', 'nota': 'B'},
    {'nome':'André', 'nota': 'A'},
    {'nome':'Anderson', 'nota': 'C'},
    {'nome':'José', 'nota': 'B'},

]

alunos0.sort(key=lambda item: item['nota'])   #criando a funçao para ordem a lista com o criterio que eu desejo


for aluno0 in alunos0:   #para ver melhor 
    print(aluno0)


print('----------------------------------------EXEMPLO 1-----------------------------------------------------')


alunos1 = [
    {'nome':'Luiz', 'nota': 'A'},
    {'nome':'Letícia', 'nota': 'B'},
    {'nome':'Fabrício', 'nota': 'A'},
    {'nome':'Rosemary', 'nota': 'C'},
    {'nome':'Joana', 'nota': 'D'},
    {'nome':'João', 'nota': 'A'},
    {'nome':'Eduardo', 'nota': 'B'},
    {'nome':'André', 'nota': 'A'},
    {'nome':'Anderson', 'nota': 'C'},
    {'nome':'José', 'nota': 'B'},

]


alunos1.sort(key=lambda item: item['nota']) 
alunos1_agrupados = groupby(alunos1, lambda item: item['nota'] )    #precisa coloca o iteravel e a chave que a gente quer agrupar,lembrando que é necessario uma funçao 
print(alunos1_agrupados)   # lembrando que sera gerado <itertools._group object at ...>

for x , y in  alunos1_agrupados:   # PRECISEI INTERAR SOBRE ELE PARA PODER VER O QUE TEM DENTRO
    for z in y:
        print(f'{x}----->{z}')


print('----------------------------------------EXEMPLO 2-----------------------------------------------------')



alunos2 = [
    {'nome':'Luiz', 'nota': 'A'},
    {'nome':'Letícia', 'nota': 'B'},
    {'nome':'Fabrício', 'nota': 'A'},
    {'nome':'Rosemary', 'nota': 'C'},
    {'nome':'Joana', 'nota': 'D'},
    {'nome':'João', 'nota': 'A'},
    {'nome':'Eduardo', 'nota': 'B'},
    {'nome':'André', 'nota': 'A'},
    {'nome':'Anderson', 'nota': 'C'},
    {'nome':'José', 'nota': 'B'},

]

ordena2 = lambda item: item['nota']    #foi feito isso para nao repetir codigo
alunos2.sort(key= ordena2) 
alunos_agrupados2 = groupby(alunos2, ordena2 )    #precisa coloca o iteravel e a chave que a gente quer agrupar

for agrupamento2 , valores_agrupados2 in alunos_agrupados2:
    print(f'agrupamento: {agrupamento2}')
    for aluno2 in valores_agrupados2:
        print(aluno2)


print('----------------------------------------EXEMPLO 3-----------------------------------------------------')



alunos3 = [
    {'nome':'Luiz', 'nota': 'A'},
    {'nome':'Letícia', 'nota': 'B'},
    {'nome':'Fabrício', 'nota': 'A'},
    {'nome':'Rosemary', 'nota': 'C'},
    {'nome':'Joana', 'nota': 'D'},
    {'nome':'João', 'nota': 'A'},
    {'nome':'Eduardo', 'nota': 'B'},
    {'nome':'André', 'nota': 'A'},
    {'nome':'Anderson', 'nota': 'C'},
    {'nome':'José', 'nota': 'B'},

]

ordena3 = lambda item: item['nota']    #foi feito isso para nao repetir codigo
alunos3.sort(key= ordena3) 
alunos_agrupados3 = groupby(alunos3, ordena3 )    #precisa coloca o iteravel e a chave que a gente quer agrupar

for agrupamento3 , valores_agrupados3 in alunos_agrupados3:
    print(f'agrupamento: {agrupamento3}')
    quantidade3 = len(list(valores_agrupados3))# é necessario converter para a lista para consegui contar  | para saber quantas pessoas estao nesse grupo
    print(f'{quantidade3} alunos estao nesse grupo')  



print('----------------------------------------EXEMPLO 4-----------------------------------------------------')



alunos4 = [
    {'nome':'Luiz', 'nota': 'A'},
    {'nome':'Letícia', 'nota': 'B'},
    {'nome':'Fabrício', 'nota': 'A'},
    {'nome':'Rosemary', 'nota': 'C'},
    {'nome':'Joana', 'nota': 'D'},
    {'nome':'João', 'nota': 'A'},
    {'nome':'Eduardo', 'nota': 'B'},
    {'nome':'André', 'nota': 'A'},
    {'nome':'Anderson', 'nota': 'C'},
    {'nome':'José', 'nota': 'B'},

]

ordena4 = lambda item: item['nota']    #foi feito isso para nao repetir codigo
alunos4.sort(key= ordena4) 
alunos_agrupados4 = groupby(alunos4, ordena4 )    #precisa coloca o iteravel e a chave que a gente quer agrupar

for agrupamento4 , valores_agrupados4 in alunos_agrupados4:
    print(f'agrupamento: {agrupamento4}')
    quantidade4 = len(list(valores_agrupados4))# é necessario converter para a lista para consegui contar  | para saber quantas pessoas estao nesse grupo
    print(f'{quantidade4} alunos estao nesse grupo')  

    #for aluno4 in valores_agrupados4:   --> se eu tentasse usar o for nao iria dar certo porque a funçao len la emcima ja esgotou os valores 



print('----------------------------------------EXEMPLO 5-----------------------------------------------------')

#resolvendo o problema de cima , que foi ter tido os valores esgotados pelo len()

alunos5 = [
    {'nome':'Luiz', 'nota': 'A'},
    {'nome':'Letícia', 'nota': 'B'},
    {'nome':'Fabrício', 'nota': 'A'},
    {'nome':'Rosemary', 'nota': 'C'},
    {'nome':'Joana', 'nota': 'D'},
    {'nome':'João', 'nota': 'A'},
    {'nome':'Eduardo', 'nota': 'B'},
    {'nome':'André', 'nota': 'A'},
    {'nome':'Anderson', 'nota': 'C'},
    {'nome':'José', 'nota': 'B'},

]

ordena5 = lambda item: item['nota']    
alunos5.sort(key= ordena5) 
alunos_agrupados5 = groupby(alunos5, ordena5 )    

for agrupamento5 , valores_agrupados5 in alunos_agrupados5:
    var1 , var2 = tee(valores_agrupados5)     # a função tee cria varias copias do interador informado

    print(f'agrupamento: {agrupamento5}')

    for aluno5 in var1:
        print(f'\t{aluno5}')
        
    quantidade5 = len(list(var2))
    print(f'\t{quantidade5} alunos estao nesse grupo') 

