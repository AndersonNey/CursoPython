

class A:
    def falar(self):
        print('Falando... Estou em A')

class B(A):
    def falar(self):
        print('Falando... Estou em B')

class C(A):
    def falar(self):
        print('Falando... Estou em C')

class D(C,B):        #problema do diamante , no caso do python ele da preferencia da esquerda para direita    seria +/- isso    C -> B -> A
    pass

d = D()
d.falar()
