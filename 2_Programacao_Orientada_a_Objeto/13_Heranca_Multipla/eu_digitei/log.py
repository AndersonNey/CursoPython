class LogMixin:   #vai dar outra funcionalidade para outras classes
    
    @staticmethod
    def write(msg):        #vou usar ele de estilo publico
        with open ('C:/PROJETO_PYTHON/PYTHON_VSCODE/Python_(Aulas)/aula 56 POO - Heranca Multipla/eu_digitei/REGISTROS.log','a+') as regist:
            regist.write(msg)
            regist.write('\n')
        

    # as funçoes abaixo nao sao estaticas
    
    def log_info(self,msg):
        self.write(f'INFO: {msg}')

    def log_erro(self,msg):
        self.write(f'ERROR: {msg}')
