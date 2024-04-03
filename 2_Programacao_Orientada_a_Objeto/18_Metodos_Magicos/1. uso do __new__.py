

class A:
    
    def __new__(cls,*args,**kwargs):   #na verdade quem constroi o objeto é o metodo new 
        return super().__new__(cls)    #concertando o construtor aqui     #toda classe é deriva de object
        #return object.__new__(cls)    #é a mesma coisa que o codigo de cima
    
    def __init__(self):     #ele é executado assim que a classe é instanciada
        print('carro')






a = A()