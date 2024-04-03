"""Documentaçao deste modulo

ele nao faz nada, mas é so um exemplo pra voce.
typing - https://docs.python.org/3/library/typing.html

"""


x: int = 10
y: float = 8.5
z: bool = False
variavel:str = 'Variavel1'


def funcao(p1:float ,p2:str ,p3:dict) -> float :   #é bom para indicar qual tipo de dado é para entrar aqui  e o tipo de dado que vai sair 
    return 'oi'

var = funcao(10.5,'joaozinho',{})
print(var)
def funcao1() -> list |dict:  # posso indicar assim apertir do python 3.10
    pass


# from typing import Union      # caso eu queira informa mais informaçoes sobre os tipos dos dados 
# def funcao1() -> Union[list,dict]:     #para indicar varios tipos de retorno que eu poderia ter eu precisei importar do modulo typing para usar o Union.
     




# In Python 3.10, you can replace Union[float, int] with the more succinct float | int. The annotation of numbers is easier to read now, and as an
#  added bonus, you didn’t need to import anything from typing.

# A special case of union types is when a variable can have either a specific type or be None. You can annotate such optional types either as 
# Union[None, T] or, equivalently, Optional[T] for some type T. There is no new, special syntax for optional types, but you can use the new union 
# syntax to avoid importing typing.Optional:

# address: str | None
# In this example, address is allowed to be either None or a string.