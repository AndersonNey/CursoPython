#https://ffmpeg.org/download.html
#https://ffmpeg.org/documentation.html

#no local onde esse arquivo esta nao vai funcionar, porque tem espacos entre o nome na pasta
#tem como configurar para mandar o video para mesma pasta do original, mas com o nome diferente ,mas preferir nao incluir
#com o linux nao precisa baixar o arquivo ffmpeg.exe

"""
ffmpeg -i "Entrada" -i "Legenda" -c:v libx264 - crf 23 -present ultrafast -c:a aac -b:a 320k -c:s srt -map v:0 -map a -map 1:0 "Saida"
"""

#from genericpath import isfile    se nao funciona uma das possibilidades é falta dessa biblioteca
import os
import fnmatch
import sys

caminho = os.path.dirname(os.path.realpath(__file__))

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'

else:
    comando_ffmpeg = caminho + r'\ffmpeg.exe'

codec_video ='-c:v libx264'
crf = '-crf 23'                #18 melhor qualidade 28 pior qualidade
preset = '-preset ultrafast'   #-preset fast
codec_audio = '-c:a aac'
bitrate_audio= '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'     #para converter o video todo so colocar debug = ''

caminho_da_origem =caminho + r'\origem'
caminho_destino = caminho + r'\destino'


for raiz, pastas,arquivos in os.walk(caminho_da_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo,'*.mp4'):
            continue
        caminho_completo = os.path.join(raiz,arquivo)
        nome_arquivo , extensao_arquivo = os.path.splitext(caminho_completo)
        caminho_legenda = nome_arquivo + '.srt'
        
        if os.path.isfile(caminho_legenda):
            input_legenda = f'-i {caminho_legenda}'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_legenda = ''
            map_legenda = ''

        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

        arquivo_saida = f'{caminho_destino}\{arquivo}_novo{extensao_arquivo}'

        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} {codec_video} {crf} {preset} {codec_audio} {debug} {map_legenda} "{arquivo_saida}" '
        os.system(comando)

