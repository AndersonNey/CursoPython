
#Forma sem o ENUM

#limita as opcoes
def mover(direcao):
    if direcao != 'direita' and direcao != 'esquerda' and direcao != 'cima' and direcao != 'baixo':
        raise ValueError('cannot move in this direction')

    return f'Movimento para {direcao}'




print(mover('direita'))
print(mover('esquerda'))
print(mover('cima'))
print(mover('baixo'))
#esse trecho daria erro
#print(mover('diagonal'))




