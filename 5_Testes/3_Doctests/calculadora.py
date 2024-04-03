#Doctests é utilizar a documentacao para fazer testes
#é necessario utilizar 3 sinais de maior que '>>>'
#dentro da documentaçao pedimos para executar a funcao e colocamos o resultado desejado (por padrao se der tudo certo ele nao vai exibir nada)
#caso eu queira que exiba precisei colocar verbose=True

#se por acaso colocar a funcao para executar e eu nao coloquei o resultado esperado , isso significa que eu nao espero receber nada,
#e se ele retornar algo isso significa que o teste falhou

#tambem posso esperar um erro como retorno, ai no caso eu posso colocar que nem no exemplo abaixo, para resumo o codigo de erro que obtivi:

#RESUMO

# Traceback (most recent call last):
# ...
# AssertionError: X precisa ser numero inteiro ou float

#ERRO OCORRIDO

# Exception raised:
#     Traceback (most recent call last):
#       File "C:\Users\computador\AppData\Local\Programs\Python\Python310\lib\doctest.py", line 1350, in __run
#         exec(compile(example.source, filename, "single",
#       File "<doctest __main__.soma[2]>", line 1, in <module>
#         soma('10',20)
#       File "c:\PROJETO_PYTHON\PYTHON_VSCODE\Python_(Aulas)\aula 152 Testes - Doctests\calculadora.py", line 26, in soma
#         assert isinstance(x,(int,float)) ,  'X precisa ser numero inteiro ou float'


#Observacao: O Doctestes tipo joga no modo imperativo do python e ver se o comando e a resposta passado por mim bate com o comando e a resposta obtido pela execucao

def soma(x,y):
    """Soma x e y

    
    >>> soma(10,20)
    30
    >>> soma(-10, 20)
    10
    >>> soma('10',20)
    Traceback (most recent call last):
    ...
    AssertionError: X precisa ser numero inteiro ou float
    >>> soma(10,20)
    30
    """



    assert isinstance(x,(int,float)) ,  'X precisa ser numero inteiro ou float'  
    assert isinstance(y,(int,float)) ,  'Y precisa ser numero inteiro ou float'  
    return x+y

def subtrai(x,y):
    """subtrai
    
    >>> subtrai(10,5)
    5
    >>> subtrai('10',5)
    Traceback (most recent call last):
    ...
    AssertionError: X precisa ser numero inteiro ou float
    """
    assert isinstance(x,(int,float)) ,  'X precisa ser numero inteiro ou float'  
    assert isinstance(y,(int,float)) ,  'Y precisa ser numero inteiro ou float'  
    return x-y

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)  # para ver os testes que passaram