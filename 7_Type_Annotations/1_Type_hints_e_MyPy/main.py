
# Para instalar o MyPy:
# pip install mypy
# Para checar o arquivo que quer checar:
# mypy <nome do arquivo>.py

# O PYCHARM POSSUI UM PLUGIN SE PRECISAR...

# PARA O VSCODE TEM A EXTENSAO DO PYTHON PELA MICROSOFT QUEM JA VEM COM ISSO BASTA ATIVAR.
# "python.linting.mypyEnabled": true,

#TALVEZ ALGUNS DOS RECURSOS JA PODEM ESTAR INTEGRADOS NATIVAMENTE ,MAS ESSES AINDA CONTINUAM FUNCIONANDO

#-------------------------------------------------------------------------------------------

from typing import Any, List , Union , Tuple ,Dict , Any , NewType , Callable , Sequence , Iterable


#NAO NECESSITA DO MODULO TYPE ------------------------------------------------------
#PRIMITIVOS

#nome da variavel , tipo que se espera , valor da variavel
numero: int = 10
flutuante: float = 10.5
booleano: bool = True
string: str = 'ola pessoal'

#sequencias

lista: list = [1, 2, 3]
tupla: tuple = (1, 2, 3)


#NECESSITA DO MODULO TYPE ------------------------------------------------------

lista1: List[int] = [1, 2, 3,]
lista2: List[Union[int,str]] = [1, 2, 3,'carro']

tupla1: Tuple[int,int,int,str] = (1, 2, 3 , 'luiz')   #em tupla é necessario informa o tipo de cada item

#Dicionario e conjunto

pessoa1: Dict[str,str] = {'nome': 'luiz' , 'sobrenome': 'miranda'}
pessoa2: Dict[str,Union[str,int]] = {'nome': 'luiz' , 'sobrenome': 'miranda' , 'idade':17}
pessoa3: Dict[str, Any] = {'nome': 'luiz' , 'sobrenome': 'miranda' , 'idade': 17}
pessoa4: Dict[str, Union[str, int, List[int] ]] = {'nome': 'luiz' , 'sobrenome': 'miranda' , 'idade': 17 , 'l': [1,2]}

#criando um apelido para o tipo

MeuDict = Dict[str, Union[str, int, List[int] ]]

pessoa5: MeuDict  = {'nome': 'luiz' , 'sobrenome': 'miranda' , 'idade': 17 , 'l': [1,2]}

#criando o meu proprio tipo

UserId = NewType('UserId' ,int )
var = UserId(45445)


# callable[o que ela recebe de parametros(se nao receber nada insira dois colchetes [])    ,   o que ela retorna,]
#EXEMPLO 1
def retorna_funcao1(funcao:Callable[[],None]) -> Callable:  #esse callable ta falando que vai retorna uma funcao
    return funcao

def fala_oi():
    print('oi')

retorna_funcao1(fala_oi)()  #executando o retorno que no caso irar ser uma funcao

#EXEMPLO 2
def retorna_funcao2(funcao:Callable[[int,int],int]) -> Callable:  #esse callable ta falando que vai retorna uma funcao
    return funcao

def soma(x:int,y:int) ->int:
    return x+y


retorna_funcao2(soma)(4,5)

class Pessoa:
    def __init__(self, nome:str , sobrenome: str, idade:int ) -> None:
        self.nome:str = nome
        self.sobrenome:str = sobrenome
        self.idade: int = idade


    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está falando...')




def interar1(sequencia:Union[List,Tuple,str]):
    pass

def interar2(sequencia:Sequence[int]):
    return [x for x in sequencia]

print(interar2([1,2,3]))  #mandando uma lista
print(interar2((1,2,3)))  #mandando uma tupla

#print(interar2(('a',2,3)))  #Apesar de esperar so inteiros nao significa que o vai impedir do codigo funcionar


def interar3(sequencia:Iterable[int]):
    return [x for x in sequencia]


print(interar3([1,2,3]))  #mandando uma lista
print(interar3((1,2,3)))  #mandando uma tupla
