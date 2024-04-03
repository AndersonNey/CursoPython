class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total
                                      #Agregaçao: uma classe precisa da outra classe
                                      #ambas existem mas para funcionarem perfeitamente uma depende de outra 

class Produto:        #Classe Produto pode ser usado para outras coisas e nao depende em nada da classe CarrinhoDeCompras
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor