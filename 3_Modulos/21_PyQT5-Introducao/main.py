"""
PyQT é um toolkit desenvolvido em C++ utilizado por vários programas para
criação de aplicações GUI (Interface Gráfica). Também inclui diversas
funcionalidades, como: acesso a base de dados, threads, comunicação de rede,
etc...
pip install pyqt5
"""

import sys      # ele vai precisar disso para inicializar
from  PyQt5.QtWidgets import QMainWindow , QApplication , QPushButton , QWidget, QGridLayout

class App(QMainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)  #contruindo uma grid

        self.btn = QPushButton('Texto do botao') #  criando o  botao

        self.btn.setStyleSheet('font-size: 40px')  # editando caracteristicas do botao utilizando css

        self.grid.addWidget(self.btn , 0,0,1,1 )  #colocando o botao dentro da grid  e passando os parametros (linha, coluna ,quantas linhas esse botao vai ocupar e quantas colunas esse botao vai ocupar)

        #Pegando o evento de quando o botao é clicado e mandando executar uma acao atraves de um metodo passado
        self.btn.clicked.connect(self.acao)  #se mandar parenteses da erro , tem que mandar o nome da funcao que ele executarar

        self.setCentralWidget(self.cw)

    def acao(self):
        print('ola mundo')

if __name__ == '__main__':
    qt = QApplication(sys.argv)   #para mim conseguir iniciar a interface

    app = App()
    app.show()
    qt.exec_()






