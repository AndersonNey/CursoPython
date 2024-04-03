


from abc import ABC ,abstractmethod



class Veiculo(ABC):                   #o veiculo é o produto que a gente quer
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

class VeiculoFactory:
    def __init__(self,tipo):
        self.carro=self.get_carro(tipo)

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

    def buscar_cliente(self):  #esse metodo tem esse nome por escolha mesmo,como essa classe nao tem nenhuma heranca nao sobrescreveu nada
        self.carro.buscar_cliente()    #self.carro pode usar buscar_cliente()  porque ele é um objeto do tipo (CarroLuxo | CarroPopular | MotoPopular | MotoLuxo)
                                    

if __name__ == "__main__":
    from random import choice

    carros_disponiveis = ['luxo','popular','moto','moto_luxo']

    for i in range(15):
        carro = VeiculoFactory(choice(carros_disponiveis))
        carro.buscar_cliente()







