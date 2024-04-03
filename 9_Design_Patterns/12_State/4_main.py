
from __future__ import annotations
from abc import ABC , abstractmethod



#A variavel de estado (estado do pagamneto) é uma classe

class Order:
    """Context"""
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self)->None:   #aqui ela nao esta se chamando N , self.state tem a funcao pending
        print('Tentando executar pending()')
        self.state.pending()
        print('Estado atual',self.state)
        print()

    def approve(self)->None:
        print('Tentando executar approve()')
        self.state.approve()
        print('Estado atual',self.state)
        print()

    def reject(self)->None:
        print('Tentando executar reject()')
        self.state.reject()
        print('Estado atual',self.state)
        print()

class OrderState(ABC):
    def __init__(self, order) -> None:
        self.order = order
 

    @abstractmethod
    def pending(self)->None:pass
    
    @abstractmethod
    def approve(self)->None:pass
    
    @abstractmethod
    def reject(self) ->None:pass

    def __str__(self):
        return self.__class__.__name__



class PaymentPending(OrderState):
    def pending(self)->None:
        print('Pagamento já pendente, nao posso fazer nada.')
    
    def approve(self)->None:
        self.order.state = PaymentApproved(self.order)
        print('Pagamento aprovado')
    
    def reject(self) ->None:
        self.order.state = PaymentRejected(self.order)
        print('Pagamento recusado')

class PaymentApproved(OrderState):
    def pending(self)->None:
        self.order.state = PaymentPending(self.order)
        print('Pagamento pendente')
    
    def approve(self)->None:
        print('Pagamento já aprovado, nao posso fazer nada')
    
    
    def reject(self) ->None:
        self.order.state = PaymentRejected(self.order)
        print('Pagamento recusado')

class PaymentRejected(OrderState):
 
    def pending(self)->None:
        print('Pagamento recusado. Nao vou mover para pendente.')

    def approve(self)->None:
        print('Pagamento recusado. Nao vou recusar novamente.')    
    
    def reject(self) ->None:
        print('Pagamento recusado. Nao vou recusar novamente.')    



if __name__ == "__main__":
    order = Order()
    order.pending()    #chamando o pedding da ordem
    order.approve()
    order.pending()
    order.reject()
    order.pending()
    order.approve()















