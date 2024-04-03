





#como o pessoal fazia, com risco de esquecer de fechar

arquivo = open('abc.txt', 'w')
arquivo.write('alguma coisa')
arquivo.close()

# pode usar o gerenciador de contexto para fazer uma conexao de rede, base de dados e se voce tiver criado algo que nao tem suporte ao gerenciador de contexto
#voc3 pode criar o seu proprio

class Arquivo:
    def __init__(self,arquivo,modo):
        print('abrindo arquivo')
        self.arquivo = open(arquivo,modo)

    def __enter__ (self):
        print('retorno o arquivo')
        return self.arquivo

    def __exit__(self,exc_type,exc_val,exc_tb):
        print('fechando o arquivo')
        self.arquivo.close()


with Arquivo('abc.txt' , 'w') as arquivo:
    arquivo.write('kkkkkkkkkkkkkkkk')


# with open('abc.txt', 'w') as arquivinho:
#     pass




























