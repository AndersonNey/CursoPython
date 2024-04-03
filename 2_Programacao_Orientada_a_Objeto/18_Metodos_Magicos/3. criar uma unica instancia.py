class A:
    
    def __new__(cls,*args,**kwargs):   #na verdade quem constroi o objeto é o metodo new 
        
        if not hasattr(cls,'_jaexiste'):              # isso é para instanciar apenas um objeto, se eu tentar instacia outro ele retorna sempre o 'primeiro' objeto instanciado 
            cls._jaexiste = object.__new__(cls)

        return cls._jaexiste

    
    def __init__(self):     #ele é executado assim que a classe é instanciada
        print('carro')



a = A()
b = A()
c = A()

print(a==b)   # o padrao isso era para dar false
print(b==c)   # o padrao isso era para dar false
print(a==c)   # o padrao isso era para dar false

print(id(a),id(b),id(c))   #percebam que todas tem o mesmo id