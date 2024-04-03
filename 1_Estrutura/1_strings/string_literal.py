#https://pt.stackoverflow.com/questions/80545/qual-%C3%A9-a-diferen%C3%A7a-entre-string-e-rstring-em-python#:~:text=atividade%20dessa%20publica%C3%A7%C3%A3o-,O%20que%20%C3%A9%20esse%20r%20que%20antecede%20a%20declara%C3%A7%C3%A3o%20da,%2C%20%5Ct%20)%20e%20outros.


# O r antes das aspas vem de raw, ou seja, a string será interpretada como uma string literal.

# Em uma string comum, temos a \ como caracter de escape para representar quebras de linha 
# (como \n, \r, \t) e outros. Em uma string literal, esses elementos não são processados.


#lembrando que a string literal nao pode terminar com '\' como ultimo caracter

variavel =r'oi ge\n \t nte testes'

print(variavel)