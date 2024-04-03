

#Sintaxe 
#   assert   condicao ,  Mensagem caso a condiçao seja falsa

#é como uma condicional que server para levantar uma exceçao(AssertionError) caso sao seja satisfeita
#assert é para outros desenvolvedores nao se utiliza para usuario final 


#tem como executar o programa desativado as 'assert's colocando '-O' antes do caminho ou nome do arquivo .py  


def soma(x,y):
    assert isinstance(x,(int,float)) ,  'X precisa ser numero inteiro ou float'  
    assert isinstance(y,(int,float)) ,  'Y precisa ser numero inteiro ou float'  
    return x+y


    