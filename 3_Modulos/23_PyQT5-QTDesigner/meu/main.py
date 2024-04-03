import sys 
from design import *
from PyQt5.QtWidgets import QMainWindow , QApplication
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap



class Novo(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)  #para executar a janela que foi criada
        self.btnEscolherArquivo.clicked.connect(self.abrir_imagem)
        self.btnRedimensionar.clicked.connect(self.redimensionar)
        self.btnSalvar.clicked.connect(self.salvar)

    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName( self.centralwidget , #quem é o pai dessa caixa de dialogo aqui 
                                                'Abrir imagem',  # titulo dessa janela,
                                                'c:\\',       # caminho que ela vai iniciar
                                                #options=QFileDialog.DontUseNativeDialog   #opcional se a caixa de dialogo nativa nao estiver funcionando
        )
        self.inputAbrirArquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.labelImg.setPixmap(self.original_img)
        self.inputLargura.setText(str(self.original_img.width()))     #setText espera uma string     e  width() retorna um inteiro
        self.inputAltura.setText(str(self.original_img.height())) 

    def redimensionar(self):
        largura = int(self.inputLargura.text())
        self.nova_imagem = self.original_img.scaledToWidth(largura)
        self.labelImg.setPixmap(self.nova_imagem)
        self.inputLargura.setText(str(self.nova_imagem.width()))     
        self.inputAltura.setText(str(self.nova_imagem.height())) 

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName( self.centralwidget , #quem é o pai dessa caixa de dialogo aqui 
                                        'Salvar imagem',  # titulo dessa janela,
                                        'c:\\',       # caminho que ela vai iniciar
                                        #options=QFileDialog.DontUseNativeDialog   #opcional se a caixa de dialogo nativa nao estiver funcionando
                                        )
        self.nova_imagem.save(imagem, 'PNG')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()








