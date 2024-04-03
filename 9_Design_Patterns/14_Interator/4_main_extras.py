


from collections.abc import Iterator , Iterable
from typing import List ,Any

class MyInterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = 0

    def next(self):
        try:
            return self.__next__()
        except StopIteration:
            return None

    def __next__(self):   #é necessrio colocar o next porque senao da erro de classe abstrata
        try:
            item = self._collection[self._index]
            self._index +=1
            return item
        except IndexError:
            raise StopIteration   #nao tem problema levantar essa excecao aqui porque o for vai cuidar dela

class ReverseIterator(Iterator):
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = -1

    def next(self):
        try:
            return self.__next__()
        except StopIteration:
            return None

    def __next__(self):   #é necessrio colocar o next porque senao da erro de classe abstrata
        try:
            item = self._collection[self._index]
            self._index -=1
            return item
        except IndexError:
            raise StopIteration   #nao tem problema levantar essa excecao aqui porque o for vai cuidar dela

class MyList(Iterable):
    def __init__(self) -> None:
        self._items : List[Any] = []
        self._my_iterator = MyInterator(self._items)

    def add(self,value:Any)-> None:
        self._items.append(value)

    def __iter__(self):   #é necessrio colocar o iter porque senao da erro de classe abstrata
        return self._my_iterator


    def reverse_iterator(self) -> Iterator:
        return ReverseIterator(self._items)

    def __str__(self) -> str:
        return f'{self.__class__.__name__} --> ({self._items}) '

if __name__ == "__main__":
    mylist = MyList()
    mylist.add('Luiz')
    mylist.add('Maria')
    mylist.add('Joao')

    iterator = mylist.__iter__()

    print('Pegando um item antes', iterator.next() ) #  next(iter(mylist)) = next(mylist.__iter__())


    for value in mylist:
        print(value)

    for value in mylist:
        print(value)
    
    for value in mylist:
        print(value)
    print()
    
    for value in mylist.reverse_iterator():
        print(value)
























