import sys 
from design import *
from PyQt5.QtWidgets import QMainWindow , QApplication


class Novo(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)  #para executar a janela que foi criada


    
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()








