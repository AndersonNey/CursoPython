from tkinter import *
from tkinter import ttk

root = Tk()


#A opção de configuração "padding" é usada para solicitar espaço extra dentro do widget; desta forma, se você estiver
# colocando outros widgets dentro do quadro, haverá uma pequena margem ao redor. Um único número especifica o mesmo
# preenchimento em toda a volta, uma lista de dois números permite que você especifique o preenchimento horizontal e depois o
# vertical, e uma lista de quatro números permite que você
# Os quadros podem ter várias opções de configuração diferentes que podem alterar a forma como são exibidos.
# especifique o preenchimento esquerdo, superior, direito e inferior, nessa ordem.
# se nao tiver widget nao da nada

base = ttk.Frame(root ,padding=100)

base.grid(column=3 , row= 3)

ttk.Button(base, text= 'olá').grid(column=2,row=1)


root.mainloop()