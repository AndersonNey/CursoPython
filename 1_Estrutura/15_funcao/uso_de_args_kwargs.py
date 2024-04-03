


lista_alto_valor = []
lista_baixo_valor = []


def sem_limites(*args) -> None:
    
    for x in args:
        if x >10:
            lista_alto_valor.append(x)
        
        else:
            lista_baixo_valor.append(x)


sem_limites(2,33,34,6,8,4)

print(lista_alto_valor)
print(lista_baixo_valor)


def sem_limites_kwargs(**kwargs):

    x = kwargs.get('nome')
    print(f'como voce está {x}')
    


sem_limites_kwargs(nome ='Lucas')


def world_cup_titles(país, *args):
    print('País: ', país)
    for title in args: 
        print('year: ', title)


world_cup_titles('Brasil','1988','1990','1992','1994','1996')