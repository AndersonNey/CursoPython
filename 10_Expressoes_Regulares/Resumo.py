

#findall - Vai encontrar todas as ocorrencias da expressao do padrao que eu quero encontrar dentro do meu texto (retorna uma lista,quando nao acha retorna uma lista vazia)
#search - Vai encontrar a primeira ocorrencia retornando um objeto match em qual indice ele encotrou e se ele encotrou 
#sub - substituir algo no texto com forme eu tiver passado
#compile - compilar expressoes regulares


# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )

# . Qualquer caractere (com exceção da quebra de linha)
# ^ -> começa com
# $ -> termina com
# *     0 ou n        #especifica a esquerda dele
# +     1 ou n        #especifica a esquerda dele
# ?     0 ou 1        #especifica a esquerda dele
# {n}                 #quantas vezes esse caracter vai repetir especificadamente
# {min, max}          #colocandio valor minimo e maximo para qunatas vezes que quero que aparecera obs: {1,} ->significa 1 ou ilimitada vezes
                                                                                                      # {,10} ->significa de zero a 10
                                                                                                      # {5,10} De 5 a 10
# [] conjunto de caracteres que pode ser, mas representa apenas 1 letra
# [^a-z] -> Negação   Quero qualquer coisa que nao seja entre a-z
# \ -> escapa caracter
# | OU
# ?: -> significa nao memorizar



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



# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> Multiline -> ^ $   (comeca e termina com)
# re.S -> Dotall \n'     (consegue ler memso com quebra de linha)












