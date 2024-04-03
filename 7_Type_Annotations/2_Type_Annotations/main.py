#essa secao utiliza apartit do python 3.10 porque é apartir dessa versao quem vem alguns recursos
#o para checar usando o mypy


uma_string: str = 'um valor'
um_inteiro: int = 1234
um_float: float = 1.23
um_boolean: bool = True
um_set: set = {1,2,3}
uma_lista: list = []
uma_tupla: tuple = ()    #pode criar com ou sem os parenteses (se for somente um  elemento deve-se deixar uma virgula depois do valor )
um_dicionario: dict= {}





def soma(x:int ,y:int , z:float ) -> float:       #quando fala que pode retornar float pode ser inteiro ou float
    return x+y



lista_intiros: list[int] = [1,2,3,4]
lista_strings: list[str] = ["a","b","c","d"]
lista_tuplas:  list[tuple] = [ (1,"a") , (2,"b")]
lista_listas_int: list[list[int]] = [[1],[4,5]]


um_dict: dict[str , int] = {
    "A": 0,
    "B": 0,
    "C": 0,
}

um_dict_de_listas: dict[str,list[int]] = {
    "A":[1,2],
    "B":[3,4],
    "C":[5,6],
}


um_set_de_inteiros: set[int] = {1,2,3}


#alias de um tipo (apelido ,basicamente criar uma variavel para falar o tipo)

ListasInteiros = list[int]
DictListaInteiros = dict[str , ListasInteiros]


um_dict_de_Listas: DictListaInteiros = {
    "A":[1,2],
    "B":[3,4],
    "C":[5,6], 
}


string_e_inteiros: str | int = 1 # Union
string_e_inteiros = "A" #sem erros
string_e_inteiros = 2  #sem erros
lista: list[int | str] = [1,2,3,'a']



#tipos opcionais

#para caso eu queira falar que o parametro é opcional 

#Esse fiquei meio na duvida (pois aponta erro)

# def soma2(x: int , y: int | None = 1) -> int :
#     return x + y





#checagem em tempo de execucao

def soma2(x: int , y: float | None = None) -> float :
    if isinstance(y ,float | int ):
        return x + y
    return x + x

print(soma2(1,10))


#callable   (que pode chamar ou seja usar os parenteses na frente)


from collections.abc import Callable

SomaInteiros = Callable[[int,int],int]   # [[parametros],retorno]

def soma3(a:int , b:int ) -> int:   #por exemplo eu posso usar essa funcao no exemplo abaixo porque ela obdece a estrutura definida
    return a + b

def executa(func: SomaInteiros , a:int, b:int) -> int:   #(1°parametro -> funcao , 2°parametro -> numero inteiro , 3°parametro -> numero inteiro) -> numero inteiro
    return func(a ,b )


executa(soma3 , 1,2)


#Typevars

from typing import TypeVar

T = TypeVar('T')

#tudo que esta dentro da minha lista é do tipo T
#pelo o que eu entendi a lista toda teve ser do mesmo tipo do tipo do primeiro item que está no indice 0 

def get_item(list: list[T],index: int) -> T:
    return list[index]

list_int = get_item([1,2,3],1) #int
list_str = get_item(['a','b','c'],1) #str








class Person:
    def __init__(self, firstname , lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname

    @property
    def full_name(self):
        return f'{self.firstname} {self.lastname}'

#informa o tipo que sera recebido
def say_my_name(person: Person) -> str:
    return person.full_name

print(say_my_name(Person('john','Doe')))

def say_my_name1(person: Person) -> list[Person]:
    return [person.firstname , person.lastname ]

print(say_my_name1(Person('john','Doe')))







from typing import Any

#informa que vai receber qualquer coisa
def say(person: Any ) -> str:
    return person.full_name
