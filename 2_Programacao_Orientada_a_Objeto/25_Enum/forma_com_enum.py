#Forma com o ENUM
from enum import Enum , auto
#esse 'auto' serve para caso eu nao queira ficar dando valor ele se encarrega disso

class Direcoes(Enum):
    direita = 0
    esquerda = 1
    cima = 2
    baixo = 3
    sudoeste = auto()
    noroeste = auto()
    sudeste =auto()
    nordeste =auto()



def mover(direcao):
    if not isinstance(direcao , Direcoes):
        return 'Nao pode se mover nessa direção'
    return f'Movimento para {direcao.name} {direcao.value}'


print(mover(Direcoes.direita))
print(mover(Direcoes.esquerda))
print(mover(Direcoes.cima))
print(mover(Direcoes.baixo))
print(mover(Direcoes.sudoeste))
print(mover(Direcoes.noroeste))
print(mover('cair'))

print('---------------------------------------------------')
for x in Direcoes:
    print(x , x.name , x.value)


