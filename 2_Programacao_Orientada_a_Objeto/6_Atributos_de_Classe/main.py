
class A:
    vc = 123   #é uma variavel de classe que esta disponivel para todas as instancias dessa classe

a1 = A()
a2 = A()

a1.vc = 321         #primeiro o python vai procurar se existe na instacia, caso exista ele ja exibi, se nao achar vai procurar na classe em si.

print(a1.__dict__)   
print(a2.__dict__)
print(A.__dict__)

print()
print(a1.vc)
print(a2.vc)
print(A.vc)

print('-----------------------------------------------------------------------------------------------------------------------------------------------')

class B:
    vc = 123  

    def __init__(self) -> None:
        self.vc = 321

b1 = B()
b2 = B()

print(b1.vc)
print(b2.vc)
print(B.vc)