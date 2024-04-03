
class A:
    def __init__(self):
        print('eu sou o INIT')

    def __call__(self, *args): #funcionar  para poder usar o objeto como funcao
        soma = 0
        for i in args:
            soma += i
        return soma
    
    def __setattr__(self, key,value):
        if key == 'nome':
            self.__dict__[key] = 'voce nao pode fazer isso' 
        else:      
            self.__dict__[key] = value    #esta unica linha é o comportamento padrao


a = A()
a.nome = 'luiz otavio'
a.idade =125
print(a.nome)                     #daria erro se nao configurasse  __setattr__
print(a.idade)