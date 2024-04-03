import sys
from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.QtWidgets import QWidget     # Utilizei para criar o central object
from PyQt5.QtWidgets import QGridLayout   #Para criar a grid



class Calculadora(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora')   #Colocando titulo na interface
        self.setFixedSize(400,400)  # Travando a tela para nao aumentar e nem diminuir de tamanho
        self.cw = QWidget()         #acho que aqui estou criando o widget basico
        self.grid = QGridLayout(self.cw)   #acho que aqui esta adicionando a grid na janela
        


        self.setCentralWidget(self.cw)   # estou definindo que o cw sera meu widget central  (Define o dado widget como o widget central da janela principal.)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()








