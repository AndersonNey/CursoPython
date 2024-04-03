



#------------------------------------------------------------------------------------------------------------------------------------

class Arquivo:                          #importante debugar
    def __init__(self,arquivo,modo):
        print('abrindo arquivo')
        self.arquivo = open(arquivo,modo)

    def __enter__ (self):
        print('retorno o arquivo')
        return self.arquivo

        #__enter __Define o que o gerenciador de contexto deve fazer no início do bloco criado pela withinstrução. 
        #Observe que o valor de retorno de __enter__está vinculado ao destino da withinstrução ou ao nome após o as.

    def __exit__(self,exc_type,exc_val,exc_tb):  #isso sao exceçoes
        print('fechando o arquivo')
        self.arquivo.close()
        print(exc_type)                      #se ocorre 1 ou mais exceçoes eu trato ela e retorno True
        print(exc_val)
        print(exc_tb)

        #Define o que o gerenciador de contexto deve fazer após a execução (ou término) de seu bloco. Ele pode ser 
        # usado para tratar exceções, realizar limpeza ou fazer algo sempre feito imediatamente após a ação no bloco. 
        # Se o bloco for executado com sucesso, exception_type, exception_value, e tracebackserá None. Caso contrário, 
        # você pode optar por manipular a exceção ou deixar que o usuário a trate; se você quiser lidar com isso, certifique-se 
        # de __exit__retornar Truedepois que tudo estiver dito e feito. Se você não quiser que a exceção seja tratada pelo 
        # gerenciador de contexto, apenas deixe acontecer.
 

    #   return True
    

#----------------------------------------------------------------------------------------------------------------------------------
# abrindo arquivo
# retorno o arquivo
# fechando o arquivo
# None                        esta tudo nome porque nao ocoreu nenhum exceçao aqui dentro
# None
# None

with Arquivo('abc.txt' , 'w') as arquivo:
    arquivo.write('kkkkkkkkkkkkkkkk')


