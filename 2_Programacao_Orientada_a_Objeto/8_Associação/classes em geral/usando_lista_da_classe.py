


class Pessoa:
	def __init__(self,NOME,RG):
		self.nome = NOME
		self.rg = RG



class Banco():
	lista =[]

	def cadastro(self):
		resp1 = 'joao'    #input('Insira seu nome: ')
		resp2 = '8762933'    #input('Insira seu RG: ')
		self.clientes = Pessoa(resp1,resp2)
		self.__class__.lista.append(self.clientes)                    #self.__class__.lista       está se referindo ao atributo da propria classe
		
	def exibir_cliente(self):
		for x in self.__class__.lista:
			print(x)




yabank = Banco()

yabank.cadastro()
yabank.cadastro()
yabank.exibir_cliente()

troll = Banco()
troll.exibir_cliente()