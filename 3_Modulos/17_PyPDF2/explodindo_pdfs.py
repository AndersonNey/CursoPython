import PyPDF2
import os
caminho = os.path.dirname(os.path.realpath(__file__))
caminho_de_destino =caminho+r'\destino'
caminho_do_novo_doc= caminho_de_destino +'\\'+  'novo_arquivo.pdf'
caminho_do_novo_doc_explodido = caminho + r'\destino_explodido' + '\\'

#indo buscar o arquivo que eu juntei no script anterior para separa-lo
with open(caminho_do_novo_doc, 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = leitor.getNumPages()

    for num_pagina in  range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(num_pagina)
        escritor.addPage(pagina_atual)

        with open(f'{caminho_do_novo_doc_explodido}{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)


