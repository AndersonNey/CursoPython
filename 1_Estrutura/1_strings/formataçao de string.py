#fatiamento de string 
car = 'caminhao'
print(car[2:5:2])   # car[onde comeca : onde termina : saltos]


nome = 'VARIAVEL'
idade = 32
altura = 1.80
emaior = idade>18
peso = 80

imc = peso / (altura ** 2)

#outra maneira de deixar bonito sem precisar ficar usando aspas e virgulas
print(f'{nome} texto aleatorio {idade} texto aleatorio {imc}')

#formatando numero
print(f'{nome} texto aleatorio {idade} texto aleatorio {imc:.2f}')

#outra maneira
print('{} texto aleatorio {} texto aleatorio {:.2f}'.format(nome,idade,imc))
print('-')
#outra maneira
print('{1} texto {0} texto {0} aleatorio {1} texto aleatorio {2:.2f} texto {2}'.format(nome,idade,imc))

#outra maneira
print('{e} texto aleatorio {a} texto aleatorio {u:.2f}'.format(e=nome,a=idade,u=imc))

#teste
#print(imc:.2f)   Desse modo nao funciona

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)



#converter binario em inteiro

teste = '101010'
teste = int(teste,2)
print(f'aqui-> {teste}')


#observar esses operadores 
"+="    #--> x+=1          x = x + 1        soma
"-="    #--> x-+1          x = x - 1        subtrai
"*="    #--> x*=2          x = x * 2        multiplica
"@="    #-->multiplicação de matrizes
"/="    #--> x/=4          x = x / 4        dividi sem arredonda
"//="   #--> x //= 5	   x = x // 5       dividi arredondando para baixo         
"%="    #--> x%=3          x = x % 3        resto da divisao
"**="   #--> x**=2         x = x ** 2       exponencial  
">>="   #--> x >>= 5	   x = x >> 5
"<<="   #--> x <<= 5	   x = x << 5
"&="    #--> x &= 5	       x = x & 5
"^="    #--> x ^= 5        x = x ^ 5
"|="    #--> x |= 5	       x = x | 5


#invertendo uma string 

x= 'carro' 
x[::-1]

#https://stackoverflow.com/questions/1746613/bitwise-operation-and-usage



# https://realpython.com/python-strings/