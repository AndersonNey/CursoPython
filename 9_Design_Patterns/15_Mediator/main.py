
from __future__ import annotations
from abc import ABC, abstractmethod 
from typing import List

class Colleague(ABC):
    def __init__(self) -> None:
        self.name: str
    
    @abstractmethod
    def broadcast(self, msg:str) -> None: pass

    @abstractmethod
    def direct(self , msg: str) -> None: pass


class Person(Colleague):
    def __init__(self, name:str , mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator

    def broadcast(self, msg:str) -> None:
        self.mediator.broadcast(self, msg)

    def send_direct(self, receiver: str, msg:str) -> None:
        self.mediator.direct(self, receiver , msg)

    def direct(self , msg: str) -> None:
        print(msg)
   
    
class Mediator(ABC):

    @abstractmethod
    def broadcast(self, colleague: Colleague , msg:str ) -> None:
        pass

    @abstractmethod
    def direct(self, sender: Colleague, receiver:str , msg:str ) -> None:
        pass

class Chatroom(Mediator):
    def __init__(self) -> None:
        self.colleagues: List[Colleague] = []

    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self.colleagues

    def add(self,colleague:Colleague) -> None:
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    def remove(self,colleague:Colleague) -> None:
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    def broadcast(self, colleague: Colleague, msg: str) -> None:
        if not self.is_colleague(colleague):
            return
        print(f'{colleague.name} disse {msg}')


    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        if not self.is_colleague(sender):       
            return
        receiver_obj: List[Colleague] = [colleague for colleague in self.colleagues if colleague.name == receiver]

        if not receiver_obj:
            return

        receiver_obj[0].direct(f'{sender.name} para {receiver_obj[0].name} : {msg}')




if __name__ == "__main__":
    chat = Chatroom()

    joao = Person('Joao',chat)
    maria = Person('Maria',chat)
    elis = Person('Elias',chat)
    jose = Person('José',chat)

    chat.add(joao)
    chat.add(maria)
    chat.add(elis)
    chat.add(jose)

    joao.broadcast('Olá pessoas')
    maria.broadcast('Fala, beleza?')
    jose.broadcast('to no chat agora')

    print()

    joao.send_direct('Maria' , 'Oi Maria, tudo bem')
    maria.send_direct('Joao','Bem e vocẽ?')

