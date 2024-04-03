
#entrada de dados
#nome = input("qual o seu nome ? ")   #indepedente se for texto ou numero sempre vai ser string
#print(f'foi respondido "{nome}" que é:{type(nome)}')    #da maneira que esta escrito agora

#outra maneira
#nome = input("qual o seu nome ? ")
#idade = int(input("qual a sua idade ?"))# ja pode modificar o tipo da variavel logo de cara ou depois
#print(f'foi respondido "{nome}" e "{idade}" que é: {type(nome)} que é: {type(idade)}')

#outra maneira
nome = input("qual o seu nome ? ")
idade = input("qual a sua idade ?")#pode modificar o tipo da variavel depois de ja ter recebido
idade = int(idade)
print(f'foi respondido "{nome}" e "{idade}" que é: {type(nome)} que é: {type(idade)}')



"""
>>> int('5')
5
>>> float('5.0')
5.0
>>> float('5')
5.0
>>> int(5.0)
5
>>> float(5)
5.0
>>> int('5.0')   OBSERVE QUE É UMA STRING FLOAT
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '5.0'
>>> int(float('5.0'))
5

"""