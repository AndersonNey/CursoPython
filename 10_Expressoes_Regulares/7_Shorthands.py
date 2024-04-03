# \w -> [a-zA-Z0-9À-ú_]
# \w -> [a-zA-Z0-9_] -> re.A    (nao pega letras acentuadas com a flag)
# \W -> [^a-zA-Z0-9À-ú_]
# \W -> [^a-zA-Z0-9_] -> re.A
# \d -> [0-9]
# \D -> [^0-9]
# \s -> [ \r\n\f\n\t]
# \S -> [^ \r\n\f\n\t]
# \b -> borda     (comeca com ou termina com o valor que infomei)
# \B -> não borda

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem veem vem"!
'''

#Pegando as palvras que possuem letras maiusculas e minusculas de duas maneiras diferentes 
print(re.findall(r'[a-z]+',texto, flags=re.I))  # print(re.findall(r'[a-zA-Z]+',texto))
print()
#Pegando os numeros tbm 
print(re.findall(r'[a-zA-Z0-9]+',texto))
print()
#Pegando letras com acentos
print(re.findall(r'[a-zA-Z0-9À-ú]+',texto))
print()

print('\n1\n\n')
print(re.findall(r'[a-z]+', texto, flags=re.I))
print('\n2\n\n')
print(re.findall(r'[a-zA-Z]+', texto))
print('\n3\n\n')
print(re.findall(r'[a-zA-Z0-9]+', texto))
print('\n4\n\n')
print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))
print('\n5\n\n')
print(re.findall(r'\w+', texto, flags=re.I))
print('\n6\n\n')
print(re.findall(r'\W+', texto, flags=re.I))
print('\n7\n\n')
print(re.findall(r'\d+', texto, flags=re.I))
print('\n8\n\n')
print(re.findall(r'\D+', texto, flags=re.I))
print('\n9\n\n')
print(re.findall(r'\s+', texto, flags=re.I))
print('\n10\n\n')
print(re.findall(r'\S+', texto, flags=re.I))
print('\n11\n\n')
print(re.findall(r'\be\w+', texto, flags=re.I))  #palavras que começam com e
print('\n12\n\n')
print(re.findall(r'\w+e\b', texto, flags=re.I))   #palavras que terminam com e
print('\n13\n\n')
print(re.findall(r'\b\w{4}\b', texto, flags=re.I))  #uma string vazia no começo e no fim da palavra e 4 letras no meio (ou seja garantindo que é uma palavra com 4 letras) se eu nao fizesse isso iria pegar palavras cortadas
print('\n14\n\n')
print(re.findall(r'\w{4}', texto, flags=re.I))  # trazendo palavras cortadas
print('\n15\n\n')
print(re.findall(r'flores\B', texto, flags=re.I))


















