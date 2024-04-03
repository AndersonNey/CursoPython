import sys
from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.QtWidgets import QWidget     # Utilizei para criar o central object
from PyQt5.QtWidgets import QGridLayout   #Para criar a grid

from PyQt5.QtWidgets import QPushButton  #vai ser o botao
from PyQt5.QtWidgets import QLineEdit    #vai ser o display da calculadora (mas na verdade ele é um input)
from PyQt5.QtWidgets import QSizePolicy  #vai ser para os botoes se auto encaixarem 


#.setStyleSheet percebi que server para setar valores tanto no widget quanto em escala global


class Calculadora(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora')   #Colocando titulo na interface
        self.setFixedSize(400,400)  # Travando a tela para nao aumentar e nem diminuir de tamanho
        self.cw = QWidget()         #acho que aqui estou criando o widget basico
        self.grid = QGridLayout(self.cw)   #acho que aqui esta adicionando a grid na janela

        self.display = QLineEdit();  #criando o (display) porque na verdade é um input modificado 
        self.grid.addWidget(self.display ,0,0,1,5) #colocando dentro da grid  e passando os parametros (linha, coluna ,quantas linhas esse widget vai ocupar e quantas colunas esse widget vai ocupar)
        self.display.setDisabled(True)   # desativando a funcao de poder digitar dentro desse campo
        self.display.setStyleSheet(
            '*{background: white; color: #000; font-size:30px;}'   # (*)tudo vai ter  as seguintes configuraçoes 
        )
        self.display.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Expanding)   #regra para o display ocupa toda a grid, mas conforme for adicionando botoes ele vai subindo

        self.add_btn(QPushButton('7'),1 , 0 ,1,1 ) #colocando o 7 dentro de QPushButton aqui dentro acho que ele vira um paramentro que tem como ser recuperado com text()
        self.add_btn(QPushButton('8'),1 , 1 ,1,1 ) 
        self.add_btn(QPushButton('9'),1 , 2 ,1,1 ) 
        self.add_btn(QPushButton('+'),1 , 3 ,1,1 ) 
        self.add_btn(
            QPushButton('C'),1 , 4 ,1,1 ,
            lambda:self.display.setText(''),  #setando o display como vazio (limpando o display)
            'background: #d5580d; color: #fff; font-weight: 700;'
            ) 

        self.add_btn(QPushButton('4'),2 , 0 ,1,1 ) 
        self.add_btn(QPushButton('5'),2 , 1 ,1,1 ) 
        self.add_btn(QPushButton('6'),2 , 2 ,1,1 ) 
        self.add_btn(QPushButton('-'),2 , 3 ,1,1 ) 
        self.add_btn(
            QPushButton('<-'),2 , 4 ,1,1,
            lambda: self.display.setText(
                self.display.text()[:-1]  #o texto que esta la menos 1
                ),
                 'background: #13823a; color: #fff; font-weight: 700;') 

        self.add_btn(QPushButton('1'),3 , 0 ,1,1 ) 
        self.add_btn(QPushButton('2'),3 , 1 ,1,1 ) 
        self.add_btn(QPushButton('3'),3 , 2 ,1,1 ) 
        self.add_btn(QPushButton('/'),3 , 3 ,1,1 ) 
        self.add_btn(QPushButton(''),3 , 4 ,1,1 )

        self.add_btn(QPushButton('.'),4 , 0 ,1,1 ) 
        self.add_btn(QPushButton('0'),4 , 1 ,1,1 ) 
        self.add_btn(QPushButton(''),4 , 2 ,1,1 ) 
        self.add_btn(QPushButton('*'),4 , 3 ,1,1 ) 
        self.add_btn(
            QPushButton('='),4 , 4 ,1,1,
            self.eval_igual,    #estou mandando executar essa funcao ,essa nao foi lambda para ser um pouco diferente , e acho que foi para poder validar alguma coisa
            'background: #095177; color: #fff; font-weight: 700;'
        ) 

        self.setCentralWidget(self.cw)   # estou definindo que o cw sera meu widget central  (Define o dado widget como o widget central da janela principal.)

    def add_btn(self,btn, row , col , rowspan , colspan,funcao=None, style = None):    # automatiza o processo de criar botoes na grid
        self.grid.addWidget(btn, row , col , rowspan , colspan)
        
        if not funcao: # se receber funcao executa isso
            btn.clicked.connect(
                lambda : self.display.setText(
                    self.display.text()  + btn.text()   #pegando o texto que esta no display e concatenando com o valor que estou pedindo para inserir nele
                )               # sentando o valor do botao no display
            )
        else:
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred,QSizePolicy.Expanding)   #regra para os botoes ocupa toda a grid, mas conforme for adicionando botoes ele vai subindo

    def eval_igual(self):  #validando o que esta no display
        try:
            self.display.setText(                   #acho que o display so aceita string nao tenho certeza
                str(eval(self.display.text()))    #O eval()método analisa a expressão passada para este método e executa a expressão python (código) dentro do programa.
            )
        except Exception as e:
            self.display.setText('Conta inválida')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()








