from eletronico import Eletronico
from log import LogMixin

class Smartphone(Eletronico,LogMixin):
    
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False
    
    def conectar(self):
        if not self._ligado:
            print(f'{self._nome} nao esta ligado')
            self.log_erro(f'{self._nome} nao esta ligado')
            return

        if self._conectado:
            print(f'{self._nome} já esta conectado')
            self.log_info(f'{self._nome} já esta conectado')
            return

        self._conectado = True
        print('aparelho agora esta conectado')
        self.log_info('aparelho agora esta conectado')
        
        

    def desconectar(self):
        if not self._ligado:
            print(f'{self._nome} nao esta ligado')
            self.log_erro(f'{self._nome} nao esta ligado')
            return

        if not self._conectado:
            print(f'{self._nome} já esta desconectado')
            self.log_info(f'{self._nome} já esta desconectado')
            return
            
        self._conectado = False
        print('aparelho agora esta desconectado')
        self.log_info('aparelho agora esta desconectado')