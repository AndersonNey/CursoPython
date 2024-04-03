

# é um pouco etranho mas isso é para explicar como chamar de cima para baixo, que é algo nada comum

class Biblioteca:
    def chama_metodo_da_interface(self):      # o metodo pai chamando o metodo do filho isso nao é comum
        self.metodo_da_interface()



class Interface(Biblioteca):
    def metodo_da_interface(self):
        print('sou o metodo da interface')


#---------------------------------------------------------------------------------------------------------


i1= Interface()
i1.chama_metodo_da_interface()