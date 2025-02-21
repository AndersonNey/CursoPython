
from abc import ABC, abstractmethod


#ESSA CLASSE E SO PARA FICAR MELHOR PARA VER OS ATRIBUTOS
class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()



class User(StringReprMixin):
    def __init__(self):
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone_numbers = []
        self.addresses = []


class IUserBuilder(ABC):
    
    @property
    @abstractmethod
    def result(self):pass

    @abstractmethod
    def add_firstname(self,firstname):pass

    @abstractmethod
    def add_lastname(self,lastname):pass

    @abstractmethod
    def add_age(self,age):pass

    @abstractmethod
    def add_phone(self,phone):pass

    @abstractmethod
    def add_addresses(self,addresses):pass


class UserBuilder(IUserBuilder):

    def __init__(self):
        self.reset()


    def reset(self):
        self._result = User()
    
    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data


    def add_firstname(self,firstname):
        self._result.firstname = firstname
        return self                       #esse return self serve meramente para permitir encadeamento de metodos

    def add_lastname(self,lastname):
        self._result.lastname = lastname
        return self

    def add_age(self,age):
        self._result.age = age
        return self

    def add_phone(self,phone):
        self._result.phone_numbers.append(phone)
        return self

    def add_addresses(self,addresses):
        self._result.addresses.append(addresses)
        return self

class UserDirector:
    def __init__(self, builder:UserBuilder):
        self._builder = builder

    def with_age(self,firstname, lastname, age):
        self._builder.add_firstname(firstname).add_lastname(lastname).add_age(age)
        return self._builder.result

    def with_address(self,firstname, lastname, age):
        self._builder.add_firstname(firstname).add_lastname(lastname).add_addresses(age)
        return self._builder.result

if __name__ == "__main__" :
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    user1 = user_director.with_age('Luiz', 'Otavio',30)
    user2 = user_director.with_address('Luiz', 'Otavio','Avenida Carlos Souza')   
    print(user1)
    print(user2)