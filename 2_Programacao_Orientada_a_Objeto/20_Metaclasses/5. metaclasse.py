
#no caso nao é que a classe Pearson nao seja mais do tipo TYPE mas na verdade eu estou colocando uma classe no meio do caminho
#original:     type -> Person
#alterado:     type -> NameMyMetaClass -> Person

#o __new__ é executado antes do __init__
# __new__ cria o objeto  e o __init__ inicializa os dados desse objeto



class NameMyMetaClass(type):  #em Metaclasses nao se utiliza 'self' ,mas 'mcs'.
    def __new__(mcs,name,bases,namespace):
        print('__new__ da metaclass')
        cls = super().__new__(mcs,name,bases,namespace)   
        return cls

    #    return type.__new__(mcs,name,bases,namespace)    #esse aqui foi da maneira que eu pensei, mas acho que é a mesma coisa ja que super() seria de type



class Person(metaclass = NameMyMetaClass):     #alterando o tipo da classe 
    def __new__(cls,*args,**kwargs):
        print('__new__ da class')
        return super().__new__(cls)

    def __init__(self,name,lastname):
        print('__init__ da class')
        self.name = name
        self.lastname = lastname


# def init_person(self,name,lastname):
#     self.name =name
#     self.lastname =lastname


# Person = type('Person',(),{
#     '__init__':init_person
# })



person1 = Person('Luiz','Otavio')
person2 = Person('Maria','Oliveira')

print(type(Person))
print(person1.name)
print(person2.name)