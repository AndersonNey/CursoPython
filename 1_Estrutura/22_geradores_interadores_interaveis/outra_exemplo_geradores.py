nome = 'aviao no ar carro no chao'
interador= iter(nome)
gerador= (letra for letra in nome)
print(next(gerador)) #a
print(next(gerador)) #v
print(next(gerador)) #i

for t in gerador:  # o for termina o restante
    print(t)
print('----------------------------EXEMPLO1--------------------------------------------------------')
try:                               # lembrando que o TRY executa o que da ,ele so nao executa apartir do
                                   # ponto que ta com problema
    print(next(interador)) # a
    print(next(interador)) # v
    print(next(interador)) # i
    print(next(interador)) # a
    print(next(interador)) # o
    print(next(interador)) #
    print(next(interador)) # n
except:
    print('oii')

print('#'*80)

for x in interador:  #o for nao começou do inicio ele pegou o restante das letras disponiveis
    print(x)

print('--------------------------EXEMPLO2----------------------------------------------------------')
#exemplo abaixo em que o for nao executou nd porque todas as letras foram esgotadas


nome1 = 'aviao no ar carro no chao'
interador1= iter(nome1)

try:                               # lembrando que o TRY executa o que da ,ele so nao executa apartir do
                                   # ponto que ta com problema
    print(next(interador1)) # a
    print(next(interador1)) # v
    print(next(interador1)) # i
    print(next(interador1)) # a
    print(next(interador1)) # o
    print(next(interador1)) #
    print(next(interador1)) # n
    print(next(interador1)) # o
    print(next(interador1)) #
    print(next(interador1)) # a
    print(next(interador1)) # r
    print(next(interador1)) #
    print(next(interador1)) # c
    print(next(interador1)) # a
    print(next(interador1)) # r
    print(next(interador1)) # r
    print(next(interador1)) # o
    print(next(interador1)) #
    print(next(interador1)) # n
    print(next(interador1)) # o
    print(next(interador1)) #
    print(next(interador1)) # c
    print(next(interador1)) # h
    print(next(interador1)) # a
    print(next(interador1)) # o
    print(next(interador1)) #      o TRY encontrou o erro aqui e ja passou pro except
    print(next(interador1)) #
    print(next(interador1)) #
    print(next(interador1)) #
    print(next(interador1)) #

except:
    print('oi')

print('#'*80)

for x1 in interador1:  #o for nao executou nada porque todas as letras foram esgotadas
    print(x1)