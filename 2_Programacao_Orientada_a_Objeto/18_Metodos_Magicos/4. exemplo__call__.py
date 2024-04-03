

class A:
    def __init__(self):
        print('eu sou o INIT')

    def __call__(self, *args, **kwargs): #funcionar  para poder usar o objeto como funcao
        soma = 0
        for i in args:
            soma += i
        return soma


        

a = A()
variavel = a(1,2,3,4,5)
print(variavel)