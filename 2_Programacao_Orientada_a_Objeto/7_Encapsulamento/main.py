"""
public  - todos tem acesso                                  |       valor           Tem como acessar e alterar por fora
protected - tem acesso na classe e na nas classes filhas    |       _valor          Tem como acessar e alterar por fora, porém é somente na ideia de que não pode mexer.
private - tem acesso somente na classe                      |       __valor         Não tem como acessar e alterar  por fora, nao tem como mudar seu valor diretamnete usando 
                                                                                    seu nome  ex bd.__valor = 'novo valor' --> isso criaria outra variavel de nome semelhante,
                                                                                    para proteger a variavel __valor(original);
                                                                                    ou exibir  ex print(bd.__valor) daria como se variavel nao existesse. ou exibiria 
                                                                                    'novo valor' se eu rodasse bd.__valor = 'novo valor'antes de print(bd.__valor)

                                                                                    Mas para realmente modificar ou acessar seu valor seria desta maneira.
                                                                                    bd._BaseDeDados__dados

                                                                                    Isso acontece porque o python renomeia a varivavel que esta __ caso alguem 
                                                                                    crie variavel de mesmo nome, ele renomeia usando o nome da classe.
"""

class BaseDeDados:

    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id , nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id:nome}
        else:
            self.__dados['clientes'].update({id:nome})

    def lista_clientes(self):
        for id , nome in self.__dados['clientes'].items():
            print(id ,nome)

    def apaga_cliente(self,id):
        del self.__dados['clientes'][id]



bd = BaseDeDados()
bd.inserir_cliente(1 , 'Otávio')
bd.inserir_cliente(2 , 'Miranda')
bd.inserir_cliente(3 , 'Rose')
print(bd.dados)
#bd.dados = 'ola'       #como eu nao criei o set ele nao consegue setar esse valor

#bd.dados = 'outro valor'    # quebraria a classe inteira

#bd.lista_clientes()
