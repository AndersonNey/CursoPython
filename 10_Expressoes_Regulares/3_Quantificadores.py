
# *     0 ou n        #especifica a esquerda dele
# +     1 ou n        #especifica a esquerda dele
# ?     0 ou 1        #especifica a esquerda dele
# {n}                 #quantas vezes esse caracter vai repetir especificadamente
# {min, max}          #colocandio valor minimo e maximo para qunatas vezes que quero que aparecera obs: {1,} ->significa 1 ou ilimitada vezes
                                                                                                      # {,10} ->significa de zero a 10
                                                                                                      # {5,10} De 5 a 10

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem veem vem"!
Jã
'''

print(re.findall(r'jo+ão+',texto,flags=re.I))
print(re.findall(r'jo*ão*',texto, flags=re.I))
print(re.findall(r'jo+ão+',texto, flags=re.I))
print(re.findall(r'jo?ão?',texto, flags=re.I))
print(re.findall(r'jo{9}ão{7}',texto, flags=re.I))
print(re.findall(r'jo{0,9}ão{0,7}',texto, flags=re.I))


texto2 = 'João ama ser amado'

# o [] é uma letra nao varias por isso que retorna 
print(re.findall(r'ama[do]',texto2, flags=re.I))
#Terminal
#['amad']

                #nesse caso o {2} esta sendo aplicado ao range completo [do] , ou seja ,pode ser somente de 2 letras
print(re.findall(r'ama[do]{2}',texto2, flags=re.I))
#Terminal
# ['amado']

                #nesse caso o * esta sendo aplicado ao range completo [do] , ou seja ,pode ser de 1 ou mais letras 
print(re.findall(r'ama[do]*',texto2, flags=re.I))
#Terminal
# ['ama', 'amado']
