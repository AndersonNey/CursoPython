class Meta(type):
    def __new__(mcs,name,bases,namespace):
        if name== 'A':
            return type.__new__(mcs, name , bases , namespace)
        
        if 'attr_classe' in namespace:   #nao deixando a classe filha sobrescrever o atributo da classe pai
            print(f'{name} tentou sobrescrever o atributo')
            del namespace['attr_classe']

        return type.__new__(mcs, name , bases , namespace)


class A(metaclass=Meta):
    attr_classe = 'Valor A'


class B(A):
    attr_classe = 'Valor B'     #taria sobrescrevendo

class C(B):
    attr_classe = 'Valor C'


c = C()
print(c.attr_classe)