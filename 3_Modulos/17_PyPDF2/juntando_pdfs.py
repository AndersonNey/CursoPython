#https://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/
#pip install PyPDF2 

import os
caminho = os.path.dirname(os.path.realpath(__file__))

import PyPDF2

caminho_dos_pdfs = caminho + r"\origem"
caminho_de_destino =caminho+r'\destino'

novo_pdf = PyPDF2.PdfFileMerger()
for root , dirs ,files in os.walk(caminho_dos_pdfs):
    for file in files:
        caminho_completo_arquivo = os.path.join(root,file)                       # poderia ser assim tbm -->  caminho_dos_pdfs + f'\\' + file
        
        arquivo_pdf = open(caminho_completo_arquivo, 'rb')
        novo_pdf.append(arquivo_pdf)    #coletando tudo que tem no pdf
        arquivo_pdf.close()

caminho_do_novo_doc= caminho_de_destino +'\\'+  'novo_arquivo.pdf'


with open(caminho_do_novo_doc , 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)










