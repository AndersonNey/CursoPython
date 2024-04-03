#quantidade de caracteres
#o len nao funciona com numeros
usuario = input("escreva algo: ")
valor_recebido = len(usuario)
print(usuario, valor_recebido, type(valor_recebido))

#outra maneira
print(usuario.__len__())  #outra maneira de usar o len

"""Embora você possa chamar esses métodos diretamente ( [10, 20].__len__()por exemplo), 
a presença dos sublinhados é uma dica de que esses métodos devem ser invocados indiretamente 
( len([10, 20])por exemplo). A maioria dos operadores python tem um método "mágico" associado 
(por exemplo, a[x]é a maneira usual de invocar a.__getitem__(x))."""