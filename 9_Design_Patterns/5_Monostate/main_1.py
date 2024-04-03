
#Introducao 1


# class A:
#     def __init__(self,nome):
#         self.x = 10
#         self.y = 20
#         self.nome = nome

#     def __str__(self):
#         params = ', '.join([f'{k}={v}' for k ,v in self.__dict__.items()])
#         return f'{self.__class__.__name__} ---> {params}'

#         ### return f'{self.__class__.__name__}{self.__dict__}'     

#     def __repr__(self):
#         return self.__str__()
        
# a = A('joao')
# print(a)


#Introducao 2

# class StringReprMixin:
#     def __str__(self):
#         params = ', '.join([f'{k}={v}' for k ,v in self.__dict__.items()])
#         return f'{self.__class__.__name__} ---> {params}'

#     def __repr__(self):
#         return self.__str__()

# class A(StringReprMixin):
#     def __init__(self,nome):
#         self.x = 10
#         self.y = 20


# a = A('joao')
# print(a)





class StringReprMixin:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k ,v in self.__dict__.items()])
        return f'{self.__class__.__name__} ---> {params}'

    def __repr__(self):
        return self.__str__()

class MonoStateSimple(StringReprMixin):
    _state = {          #isso pertence a classe em si e nao ao objeto
        'x':10,
        'y':20,
    }

    def __init__(self, nome = None , sobrenome = None):
        print(self.__dict__)
        print(self._state)
        self.__dict__ = self._state
        print(self.__dict__)
        print(self._state)

        #isso so vai servir para ver se vai atualizar algum valor
        if nome is not None:
            self.nome = nome
        if sobrenome is not None:
            self.sobrenome = sobrenome


if __name__ == "__main__":

    m1 = MonoStateSimple('luiz','lucas')
    print(f'{MonoStateSimple._state}  <-----')
    print()    
    m2 = MonoStateSimple('joao')
    print(f'{MonoStateSimple._state}  <-----')
    print()    
    m3 = MonoStateSimple('julio')
    print(f'{MonoStateSimple._state}  <-----')
    print()

    print(m1)
    print(m2)
    print(m3)