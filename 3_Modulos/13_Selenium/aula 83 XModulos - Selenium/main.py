
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

#caminho para a raiz do projeto
caminho = Path(__file__)
#caminho para a raiz do projeto 

ROOT_FOLDER = os.path.dirname(os.path.realpath(__file__))
#caminho para pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER + r'\bin\chromedriver'

print(caminho)
print(ROOT_FOLDER)
print(CHROME_DRIVER_PATH)





