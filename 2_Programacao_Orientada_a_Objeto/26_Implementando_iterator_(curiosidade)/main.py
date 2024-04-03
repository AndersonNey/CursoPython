

class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index =0

    def add(self, valor):
        self.__items.append(valor)

    def __getitem__(self,index):     #enviar o valor do indexe solicitado
        return self.__items[index]

    def __setitem__(self,index,valor):
        if index >= len(self.__items):   #se nao existir ele cria
            self.__items.append(valor)
        self.__items[index] = valor

    def __delitem__(self,index):
        del self.__items[index]

    def __iter__(self):   #pra next funcionar precisa do __inter__
        return self

    def __next__(self):     #para enviar o valor quando pedido
        try:
            item = self.__items[self.__index]
            self.__index +=1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):             #representacao para usuario
        return f'{self.__class__.__name__}({self.__items})'

    def __repr__(self):            #representacao para desenvolvedores
        return self.__str__()



if __name__ == '__main__':
    lista = MinhaLista()
    lista.add('luiz')
    lista.add('maria')

    lista[2]='carlos'

    print(lista)
    lista[0] = 'joao'
    print(lista)

    del lista[2]

    print(lista[1])

    lista = list(lista)    

   #so conseguir usar dois for seguidos porque eu converti minha lista modificada em uma lista normal
    print('--------------------------------')
    
    for valor in lista:
        print(valor)
    
    print('--------------------------------')

    for valor in lista:
        print(valor)
    



























































