#from pprint import pprint #O professor usou mas eu preferir nao usar , isso é um print bonitinho

# (Luiz|Otávio) aqui é especificadamente Luiz ou Otávio 
# para saber qual o numero dos grupos é so conta as aberturas dos parenteses

# ()     \1
# () ()  \1 \2
# (())()   \1 \2 \3

import re


texto = """
<p>Frase 1</p> <p>Eita</p> <p>Qualquer Frase</p> <div>Frase 4</div>
"""

#os grupos sao retornados

print(re.findall(r'<([pdiv]{1,3})>.*?<\/\1>',texto))
#Terminal
# ['p', 'p', 'p', 'div']


print('=============================================')

tags =re.findall(r'(<([pdiv]{1,3})>.*?<\/\2>)',texto)   #esse \2 significa o segundo grupo, ou seja, ([pdiv]{1,3})
print(tags)
#Terminal
# [('<p>Frase 1</p>', 'p'), ('<p>Eita</p>', 'p'), ('<p>Qualquer Frase</p>', 'p'), ('<div>Frase 4</div>', 'div')]



# print('=============================================')
# for tag in tags:
#     um , dois = tag
#     print(um)

print('=============================================')
tags =re.findall(r'(<([pdiv]{1,3})>(.*?)<\/\2>)',texto)   
print(tags)

#Terminal
#[('<p>Frase 1</p>', 'p', 'Frase 1'), ('<p>Eita</p>', 'p', 'Eita'), ('<p>Qualquer Frase</p>', 'p', 'Qualquer Frase'), ('<div>Frase 4</div>', 'div', 'Frase 4')]

for tag in tags:
    um , dois, tres = tag
    print(tres)

#Terminal
# Frase 1
# Eita
# Qualquer Frase
# Frase 4

print('=============================================')
#   esse ?: significa que eu nao quero salvar o grupo ,ou seja , nao vai ter um retrovirsor para referenciar o grupo e esse grupo nem vai ser retornado.
tags =re.findall(r'<([pdiv]{1,3})>(?:.*?)<\/\1>',texto)   
print(tags)

#Terminal
#['p', 'p', 'p', 'div']


print('=============================================')

cpf = '147.852.963-12'
#                        a barra usei para escapar o ponto
print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}',cpf))

print('=============================================')

cpf = '147.852.963-12'

print(re.findall(r'([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}',cpf))

#Terminal  retornou o ultimo valor que ficou salvo na memoria referente a esse grupo
#['852.']

print('=============================================')

cpf = '147.852.963-12'

print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})',cpf))

#Terminal 
#['147.852.963-12']


print('=============================================')
#nomeando um grupo, so tem em python
tags =re.findall(r'<(?P<tag>[pdiv]{1,3})>(.+?)<\/(?P=tag)>',texto)   
print(tags)

print('=============================================')

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1"\3"\4',texto))

