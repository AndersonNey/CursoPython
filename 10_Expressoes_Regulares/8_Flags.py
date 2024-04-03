# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> Multiline -> ^ $   (comeca e termina com)
# re.S -> Dotall \n'     (consegue ler memso com quebra de linha)
import re

texto = '''
131.768.460-53 ABC
055.123.060-50 DEF
955.123.060-90
'''

print(re.findall( r'\d{3}\.\d{3}\.\d{3}\-\d{2}',texto))
# ['131.768.460-53', '055.123.060-50', '955.123.060-90']

print(re.findall( r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$',texto))
# []

print(re.findall( r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$',texto, flags=re.M))   # o re.M faz com que ai invez de checar a string como um todo, ele checa cada linha 
# ['955.123.060-90']

print('=================================================')

texto2 = '''O João gosta de folia \n E adora ser amado'''
texto3 = '''O João gosta de folia    E adora ser amado'''

print(re.findall( r'^o.*o$',texto2 , flags=re.I))
# []
print(re.findall( r'^o.*o$',texto3 , flags=re.I))
# ['O João gosta de folia    E adora ser amado']

print(re.findall( r'^o.*o$',texto2 , flags=re.I | re.S))   # com | consegue colocar mais flags
# ['O João gosta de folia \n E adora ser amado']

