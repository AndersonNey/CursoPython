#se pedir para colocar dois produtos iguais nao dara certo , porque dicionario nao aceita chave de memo valor
class Cliente:

    def __init__(self,NOME,IDADE):
        self.nome =NOME
        self.idade = IDADE                   #Composiçao                                  
        self.carrinho = CarrinhoDeCompras()  #criando o objeto em self.carrinho, eu poderia ter criado o objeto fora da classe e ter atribuido aqui ai seria Associaçao
                                             #mas neste caso se eu exclui o cliente o carrinho tambem é deletado
    def meucarrinho(self):
        self.carrinho.exibircarrinho()

    def adicionar_produto(self,produtoemsi):
        self.carrinho.adicionar_produto(produtoemsi)


class CarrinhoDeCompras:
    def __init__(self):
        self.dicionario = {}

    def exibircarrinho(self):
        for x , y in self.dicionario.items():
            print(f'Produto -> {x}   Valor-> {y}')

                                                              #Agregaçao
    def adicionar_produto(self,produto):                      #recebendo um objeto como parametro
        dicionario_transicao = {produto.nome:produto.preco}
        self.dicionario.update(dicionario_transicao)


class Produtos:

    def __init__(self,NOME,PRECO):
        self.nome = NOME
        self.preco = PRECO


pessoa1 = Cliente('luciana','18')
pessoa2 = Cliente('fernanda','30')
fruta1 = Produtos('maça', '15')
fruta2 = Produtos('banana', '55')
fruta3 = Produtos('melancia', '35')

print('Pessoa 1')
pessoa1.meucarrinho()
print('...')
pessoa1.adicionar_produto(fruta1)
print('...')
pessoa1.adicionar_produto(fruta2)
print('...')
pessoa1.meucarrinho()
print('...')
print()
print()
print()

print('Pessoa 2')
pessoa2.meucarrinho()
print('...')
pessoa2.adicionar_produto(fruta3)
print('...')
pessoa2.adicionar_produto(fruta3)
print('...')
pessoa2.meucarrinho()
print('...')

print()
print()
print()

print('Pessoa 1')
pessoa1.meucarrinho()

print('Pessoa 2')
pessoa2.meucarrinho()