# pip install selenium
#checar a versao do drive do chrome com a versao do navegador

from selenium import webdriver
from time import sleep

#retirei o driver do chrome da pasta

import os 
caminho = os.path.dirname(os.path.realpath(__file__))
caminho = caminho + r'\chromedriver'

#se eu fizer um perfil ele serar salvo dentro dessa pasta aqui XXXXXXX

class ChromeAuto:
    def __init__(self) -> None:
        self.driver_path = caminho
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=' + caminho + r'\Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )
    
    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_ele

        except:
            pass

    def acessa(self,site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()
        
    

if __name__ == "__main__":
    chrome = ChromeAuto()
    chrome.acessa('https://www.youtube.com/')
    sleep(3)
    chrome.sair()






















