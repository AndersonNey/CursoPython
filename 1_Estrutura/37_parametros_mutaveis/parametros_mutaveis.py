#mutavel: Listas , dicionarios
#Imutavel: Tuplas, Strings Numeros ,True ,False , None


#o estranho que acontece aqui é a funcao guardar os valores de por onde ela ja passou, 
#mesmo ela seno chamada com outros valores  (pensando que ela ira iniciar uma lista nova para guardar os novos valores)

def lista_de_cliente(clientes_interavel,lista=[]):    #pode causar comportamento estranhos no python, usar desta maneira
    lista.extend(clientes_interavel)                  #lembrando que o interpretador python seta os valores dos parametros apenas 1 vez 
    return lista

clientes1 = lista_de_cliente(['joao','maria','eduardo'])     
 
clientes2 = lista_de_cliente(['marcos','jonas','zico'])   #a ideia é que ela gerasse uma lista com os valores 
                                                        #inseridos, mas repare que ela guardou os valores de outra situaçao 
clientes3 = lista_de_cliente(['jose'])
print(clientes1)    
