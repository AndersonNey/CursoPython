
#por padrao uma funçao retorna none

def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass
        


while True:
    numero = converte_numero(input('Digite um número:'))
    if numero is not None:
        print(numero*5)
    else:
        print('Isso não é um numero')


    # if numero is None:                         #de outra maneira logica (nao invertido)
    #     print('Isso não é um numero')
    # else:
    #     print(numero*5)