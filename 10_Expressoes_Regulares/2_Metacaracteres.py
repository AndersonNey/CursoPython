# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres que pode ser, mas representa apenas 1 letra


import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

#As flags mudam o comportamento de como as expressoes regulares funcionam

print(re.findall(r'João|Maria|ad....s',texto))          #Cuidado que ate os espacos entre palvras ou simbolos vao se tornar relevantes
print(re.findall(r'[Jj]oão|[Mmabcde]aria',texto))
print(re.findall(r'[a-z]aria',texto))                          #dentro de [] nao precisa escapar caracteres
print(re.findall(r'[a-zA-Z0-9_+.]aria|[a-zA-Z0-9]oão',texto))  #ai dentro dos conjuntos tem os ranges a-z A-Z 0-9 e outros caracteres soltos _ + .
print(re.findall(r'jOÃo|mArIa',texto, flags=re.IGNORECASE))  #ignora se é letra maiuscula ou minuscula (pesquisa de qualquer jeito que estiver escrito)















