#self == instancia


# class Person:
#     def __init__(self,name,lastname):
#         self.name = name
#         self.lastname = lastname


def init_person(self,name,lastname):
    self.name =name
    self.lastname =lastname


Person = type('Person',(),{
    '__init__':init_person
})





person1 = Person('Luiz','Otavio')
person2 = Person('Maria','Oliveira')

print(type(person1))
print(person1.name)
print(person2.name)
print(Person.__dict__) #olhando o que a classe tem 