
# INTERFACE NO PYTHON SERIA AS CLASSES ABSTRATAS

from abc import ABC ,abstractmethod



class Veiculo(ABC):                  
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('carro de luxo esta buscando o cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('carro popular esta buscando o cliente...')

class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de Luxo esta buscando o cliente...')

class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto popular esta buscando o cliente...')



class VeiculoFactory(ABC):
    def __init__(self,tipo):
        self.carro=self.get_carro(tipo)

    @staticmethod     #nao posso trocar a ordem dessses dois
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: pass


    def buscar_cliente(self):  
        self.carro.buscar_cliente()    
                                    

class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return MotoPopular()
        if tipo == 'moto_luxo':
            return MotoLuxo()
        assert 0 , 'Carro não existe'

class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == 'popular':
            return CarroPopular()
        assert 0 , 'Carro não existe'


if __name__ == "__main__":
    from random import choice

    veiculos_disponiveis_zona_norte = ['luxo','popular','moto','moto_luxo']
    veiculos_disponiveis_zona_sul = ['popular']

    print('ZONA NORTE')

    for i in range(15):
        carro = ZonaNorteVeiculoFactory(choice(veiculos_disponiveis_zona_norte))
        carro.buscar_cliente()

    print('ZONA SUL')

    for i in range(15):
        carro2 = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_zona_sul))
        carro2.buscar_cliente()

















