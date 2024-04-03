"""

formatando valores

:s -texto (strings )
:d - inteiro (int)
:f - numeros de ponto flutuante (float)
:. - (NUMEROS) f- quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO -s, d ou f)
> - esquerda
< - direita
^ - centro
"""
num_1 = 1
print(f'{num_1:0>10}')

num_2 = 150
print(f'{num_2:0>10}')  #serao colocados caracteres 0 a esquerda sao 10 no total
                        #funciona tanto com numero quanto com letra
                        #{num_2:e>10}