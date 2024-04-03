"""

1 - Tem que receber um numero int

2 - Saber se o numero é multiplo de 3 e 5 --> retornar Bacon com Ovos
3 - Se nao for multiplo de nenhum dos dois numeros  --> retornar Passa Fome
4 - Saber se o numero é multiplo somente de 3  --> retornar Bacon
5 - Saber se o numero é multiplo somente de 5  --> retornar Ovos


"""

def bacon_com_ovos(n):
    assert isinstance(n , int), 'n deve ser int'

    if n % 3 == 0 and n % 5 ==0:
        return 'Bacon com ovos'

    if n % 3 == 0:
        return 'Bacon'

    if n % 5 == 0:
        return 'Ovos'

    return 'Passar fome'

























