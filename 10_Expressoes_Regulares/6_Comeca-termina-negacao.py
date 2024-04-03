# Meta caracteres:
# ^ -> começa com
# $ -> termina com
# [^a-z] -> Negação   Quero qualquer coisa que nao seja entre a-z
# ?: -> significa nao memorizar
import re

cpf = '147.852.963-12'
 
#se a expressao fosse  'a 147.852.963-12 a' nao passaria na validacao por que deveria comecar e terminar exatamente como a expressao quer
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$',cpf))

print(re.findall(r'[^0-9]+' ,cpf))














