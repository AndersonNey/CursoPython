
class A:
    
    def __new__(cls,*args,**kwargs):   #na verdade quem constroi o objeto é o metodo new 
        

        cls.nome = "eduardo"
        def haha(*args,**kwargs):                #daria erro se eu mandasse sem *args,**kwargs , porque automaticamente ele manda o proprio objeto
            print('fala oi')

        cls.haha = haha

        return object.__new__(cls)    #é a mesma coisa que o codigo de cima
    
    def __init__(self):     #ele é executado assim que a classe é instanciada
        print('carro')



a = A()
print(a.nome)
a.haha()
