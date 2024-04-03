

# estado intrinseco estado interno do objeto que nao modifica
# estado extrinseco parte do objeto que geralmente muda , mas tem a possibilidade de remover desse objeto e criar em outro local


from __future__ import annotations
from typing import List , Dict


class Client:
    def __init__(self,name:str) -> None:
        self.name = name
        self._addresses: List =[]

        #extrinsic address data

        self.addresses_number: str
        self.addresses_details: str

    def add_address(self , address: Address) -> None:
        self._addresses.append(address)

    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(self.addresses_number, self.addresses_details)

class Address:
    #Flyweight
    def __init__(self, street:str ,neighbourhood:str , zip_code: str) -> None:
        self._street = street
        self._neighbourhood = neighbourhood
        self._zip_code = zip_code

    def show_address(self,address_number:str, address_details: str) -> None:
        print(
            self._street , address_number , self._neighbourhood , address_details , self._zip_code
        )



class AddressFactory:
    _addresses: Dict = {}

    def _get_key(self, **kwargs) -> str:
        return ''.join(kwargs.values())

    def get_address(self,**kwargs) -> Address:
        key = self._get_key(**kwargs)

        try:
            address_flyweight =self._addresses[key]
            print('Usando objeto já criado')
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('Criando novo objeto')

        return address_flyweight

if __name__ == "__main__":
    address_factory = AddressFactory()

    a1 =address_factory.get_address(street ='Av Brasil' ,neighbourhood='Centro' , zip_code= '000000-00')

    a2 =address_factory.get_address(street ='Av Brasil' ,neighbourhood='Centro' , zip_code= '000000-00')


    luiz = Client('luiz')
    luiz.addresses_number = '50'
    luiz.addresses_details = 'casa'
    luiz.add_address(a1)
    luiz.list_addresses()

    joana = Client('joana')
    joana.addresses_number = '250A'
    joana.addresses_details = 'AP 555'
    joana.add_address(a1)
    joana.list_addresses()


    
