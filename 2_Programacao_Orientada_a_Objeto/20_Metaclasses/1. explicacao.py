"""
EM PYTHON TUDO É UM OBJETO:incluindo classes
Metaclasses sao as "classes" que criam classes.
type é uma metaclasse (!!!???)
"""

#no exemplo abaixo to checando caso a classe nao tenha o metodo b_fala ela precisa criar obrigatoriamente.

class Meta(type):
    def __new__(mcs,name,bases,namespace):
        if name== 'A':
            return type.__new__(mcs, name , bases , namespace)
        
        if 'b_fala' not in namespace:
            print(f'oi, voce precisa criar o metodo b_fala em {name}')

        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um metodo, nao atributo em {name}.')
            
        return type.__new__(mcs, name , bases , namespace)


class A(metaclass=Meta):
    def fala(self):
        self.b_fala()


class B(A):
    teste = 'Valor'

    def b_fala(self):   #caso nao tivesse esse metodo a metaclasse gerariar uma mensagem falando que precisaria do metodo
        print('oi')