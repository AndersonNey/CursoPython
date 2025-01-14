#https://docs.python.org/3/library/functions.html#open

#outras funcoes
#nome_arquivo ,ext_arquivo = os.path.splitext(caminho_completo)    #separa o caminho do tipo do arquivo




import os

caminho_procura = input('Digite um caminho: ')
termo_procura = input('Digite um termo: ')

def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'

    tamanho = round(tamanho,2)
    return f'{tamanho}{texto}'.replace('.',',')



conta = 0
for raiz , diretorios , arquivos in os.walk(caminho_procura):   #percorrer dentro das subpastas que estao dentro da pasta ,retorna uma tupla ([caminho],[diretorios],arquivos)
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta+=1
                caminho_completo = os.path.join(raiz,arquivo)          #unindo as strings para formar um caminho completo com o nome do arquivo
                nome_arquivo ,ext_arquivo = os.path.splitext(arquivo)   #separa o nome do arquivo do tipo do arquivo
                tamanho = os.path.getsize(caminho_completo)             #retornando o tamanho do arquivo em bytes
                
                print()
                print('Encontrei o arquivo:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arquivo)
                print('Extensão:', ext_arquivo)
                print('Tamanho:', tamanho)
                print('Tamanho Formatado:', formata_tamanho(tamanho))
            
            except PermissionError as e:
                print('Sem permissões.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado.')
            except Exception as e:
                print('Erro desconhecido:', e)

print()
print(f'{conta} arquivo(s) encontrado(s).')


























