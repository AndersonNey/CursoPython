


class NameMyMetaClass(type):  
    def __new__(mcs,name,bases,namespace):
        print('__new__ da metaclass')

        if name == 'Person':                           #impedindo de criar uma classe com nome de Person
            raise Exception('Cannot use name Person')

        cls = super().__new__(mcs,name,bases,namespace)   
        return cls

 


class Person(metaclass = NameMyMetaClass):    
    def __new__(cls,*args,**kwargs):
        print('__new__ da class')
        return super().__new__(cls)

    def __init__(self,name,lastname):
        print('__init__ da class')
        self.name = name
        self.lastname = lastname



person1 = Person('Luiz','Otavio')
person2 = Person('Maria','Oliveira')

print(type(Person))
print(person1.name)
print(person2.name)