
from tkinter import *
from tkinter import ttk


#3 maneiras de colocar algo na tela place , pack , grid
#grid transforma a tela em grades

janela = Tk()

class Aplicacao():
    def __init__(self):
        self.janela=janela
        self.tela()
        self.frames()
        self.widget_do_frame_superior()
        self.widget_do_frame_inferior()
        janela.mainloop()

    
    def tela(self):
        self.janela.title('Sistem YA')
        self.janela.configure(background= '#708090' )
        self.janela.geometry('720x500')
        self.janela.resizable(True,True)    # o usuario pode mexer na H ou na V da tela
        self.janela.maxsize(width=1000 , height= 1000)     #limite maximo que pode esticar
        self.janela.minsize(width=500,height=500)

    def frames(self):
        self.frame_superior = Frame(self.janela , bd = 4 , bg= '#D3D3D3' , highlightbackground= '#000000' , highlightthickness=2 )  #bd = borda , bg= background , 
        self.frame_superior.place(relx= 0.02 , rely=0.02 , relwidth= 0.96 , relheight= 0.46)    #escala funciona de 0 á 1

        self.frame_inferior = Frame(self.janela , bd = 4 , bg= '#D3D3D3' , highlightbackground= '#000000' , highlightthickness=2 )  #bd = borda , bg= background , 
        self.frame_inferior.place(relx= 0.02 , rely=0.5 , relwidth= 0.96 , relheight= 0.46)

    def widget_do_frame_superior(self):
        #BOTOES

        self.botao_limpar = Button(self.frame_superior, text='LIMPAR', bd = 2 , bg = '#107db2' , fg = 'white', font= ('verdana',8, 'bold') )
        self.botao_limpar.place(relx=0.2 , rely= 0.1 , relwidth= 0.1 , relheight= 0.15)

        self.botao_buscar = Button(self.frame_superior, text='BUSCAR', bd = 2 , bg = '#107db2' , fg = 'white', font= ('verdana',8, 'bold') )
        self.botao_buscar.place(relx=0.3 , rely= 0.1 , relwidth= 0.1 , relheight= 0.15)

        self.botao_novo = Button(self.frame_superior, text='NOVO', bd = 2 , bg = '#107db2' , fg = 'white', font= ('verdana',8, 'bold') )
        self.botao_novo.place(relx=0.6 , rely= 0.1 , relwidth= 0.1 , relheight= 0.15)

        self.botao_alterar = Button(self.frame_superior, text='ALTERAR', bd = 2 , bg = '#107db2' , fg = 'white', font= ('verdana',8, 'bold') )
        self.botao_alterar.place(relx=0.7 , rely= 0.1 , relwidth= 0.1 , relheight= 0.15)

        self.botao_apagar = Button(self.frame_superior, text='APAGAR', bd = 2 , bg = '#107db2' , fg = 'white', font= ('verdana',8, 'bold') )
        self.botao_apagar.place(relx=0.8 , rely= 0.1 , relwidth= 0.1 , relheight= 0.15)

        #Label e INPUT do tkinter

        #codigo
        self.etiqueta1 = Label(self.frame_superior, text= 'Código',bg='#D3D3D3', fg= '#107db2')
        self.etiqueta1.place(relx= 0.05, rely= 0.05 )

        self.entrada_dado1 = Entry(self.frame_superior)
        self.entrada_dado1.place(relx= 0.05, rely= 0.15 , relwidth= 0.07 )

        #nome

        self.etiqueta2 = Label(self.frame_superior, text= 'Nome',bg='#D3D3D3', fg= '#107db2')
        self.etiqueta2.place(relx= 0.05, rely= 0.35 )

        self.entrada_dado2 = Entry(self.frame_superior)
        self.entrada_dado2.place(relx= 0.05, rely= 0.45 , relwidth= 0.85 )

        #telefone

        self.etiqueta3 = Label(self.frame_superior, text= 'Telefone',bg='#D3D3D3', fg= '#107db2')
        self.etiqueta3.place(relx= 0.05, rely= 0.6 )

        self.entrada_dado3 = Entry(self.frame_superior)
        self.entrada_dado3.place(relx= 0.05, rely= 0.7 , relwidth= 0.4 )

        #cidade

        self.etiqueta4 = Label(self.frame_superior, text= 'Cidade',bg='#D3D3D3', fg= '#107db2')
        self.etiqueta4.place(relx= 0.5, rely= 0.6 )

        self.entrada_dado4 = Entry(self.frame_superior)
        self.entrada_dado4.place(relx= 0.5, rely= 0.7 , relwidth= 0.4 )

    def widget_do_frame_inferior(self):

        #tabela
        self.lista_de_amostra = ttk.Treeview(self.frame_inferior, height= 3 , columns=('coluna1','coluna2','coluna3','coluna4'))
        self.lista_de_amostra.heading('#0',text='')
        self.lista_de_amostra.heading('#1',text='Codigo')
        self.lista_de_amostra.heading('#2',text='Nome')
        self.lista_de_amostra.heading('#3',text='Telefone')
        self.lista_de_amostra.heading('#4',text='Cidade')

        self.lista_de_amostra.column('#0',width=1)
        self.lista_de_amostra.column('#1',width=50)
        self.lista_de_amostra.column('#2',width=200)
        self.lista_de_amostra.column('#3',width=125)
        self.lista_de_amostra.column('#4',width=125)

        self.lista_de_amostra.place(relx=0.01 , rely= 0.1 , relwidth= 0.95 ,relheight=0.85 )

        #barra de rolagem
        self.barra_de_rolagem = Scrollbar(self.frame_inferior,orient='vertical')
        self.lista_de_amostra.configure(yscroll=self.barra_de_rolagem.set)
        self.barra_de_rolagem.place(relx= 0.96, rely= 0.1 , relwidth= 0.04 , relheight= 0.85)





Aplicacao()