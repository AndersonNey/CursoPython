# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto
import re

#findall - Vai encontrar todas as ocorrencias da expressao do padrao que eu quero encontrar dentro do meu texto (retorna uma lista,quando nao acha retorna uma lista vazia)
#search - Vai encontrar a primeira ocorrencia retornando um objeto match em qual indice ele encotrou e se ele encotrou 
#sub - substituir algo no texto com forme eu tiver passado
#compile - compilar expressoes regulares

#O python toda vez vai compilar as expressoes regulares toda vez que for executado


string = 'Este é um teste de teste expressoes regulares.'
print(re.search(r'teste',string))    #esse 'r' evita de escrever varias vezes \\
#terminal 
#<re.Match object; span=(10, 15), match='teste'>
#              onde inicia | onde termina

print(re.findall(r'teste',string)) 
#terminal 
#['teste', 'teste']
# retornou uma lista


#substituio a palavra teste por casinha em todas as ocorrencias (o padrao de é count=0 (todas as ocorrencias))
print(re.sub('teste','casinha',string))


#substituio a palavra teste por casinha somente na primeira ocorrencia
print(re.sub('teste','balao',string,count=1))

#COMPILE   (PARA REUTILIZAR AS EXPRESSOES REGULARES OUTRAS VEZES )
print('============Compile============')


regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('balao',string))