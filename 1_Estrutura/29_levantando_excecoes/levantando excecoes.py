
print('---------------------------------1------------------------------------------------')

def divide(n1,n2):
    return n1/n2

print(divide(2,1))

print('---------------------------------2------------------------------------------------')

def divide1(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError as erro:
        print(erro)

print(divide1(2,0))

print('---------------------------------3------------------------------------------------')

def divide2(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError as erro:
        print(erro)

try:                            #nao adiantaria para nada , pois ja esta sendo tratado o erro dentro da funçao, abaixo ja é outra historia
    print(divide2(2,0))
except:
    print('erro')


print('---------------------------------4------------------------------------------------')

def divide3(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError as erro:
        print(erro)
        raise        #raise relaça a exceçao tratada

try:                            
    print(divide3(2,0))
except ZeroDivisionError as erro1:
    print('erro')


print('---------------------------------5------------------------------------------------')

def divide4(n1,n2):
    if n2==0:
        raise ValueError('n2 nao pode ser 0')
    return n1/n2

print(divide4(10,1))   #para fazer o teste substitua os valores por (10,0)

print('---------------------------------6------------------------------------------------')

def divide5(n1,n2):
    if n2==0:
        raise ValueError('n2 nao pode ser 0')
    return n1/n2

try:
    print(divide5(10,0))
except ValueError as erro:
    print(erro)

