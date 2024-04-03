

def procura_de_valor(dicion,pesquisa):
    for x , y in dicion.items():
        if y == pesquisa:
            print(x)


def mostar_bonito(dic):
    for x , y in dic.items():
        print(f'{x} : {y}')

dicionario1 = {
    'carro1': '2001',
    'carro2': '2000',
    'carro3': '2002',
    'carro4': '2002',
    'carro5': '2001',
    'carro6': '2000',
    'carro7': '2000',
    'carro8': '2001'

}

mostar_bonito(dicionario1) #nao precisava fiz so para deixar bonito

resp1 = input('Qual ano deseja encontrar: ')

procura_de_valor(dicionario1,resp1)