class Usuario:
    def __init__(self,NOME) -> None:
        self.nome = NOME
    

class Administrador(Usuario):
    
    def __init__(self,NOME,IDADE) -> None:
        self.nome = NOME
        self.idade = IDADE 



    @classmethod
    def troca_de_permissao(cls,OBJETO,IDADE):
        novousuario = cls(OBJETO.nome, IDADE)
        return novousuario


class Master(Administrador,Usuario):
    pass
  


pessoa1 = Usuario('joao')
print(pessoa1.__class__)
print(pessoa1.nome)

pessoa1 = Administrador.troca_de_permissao(pessoa1,17)

print(pessoa1.__class__)
print(pessoa1.nome)
