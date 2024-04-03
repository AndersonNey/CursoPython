
#type é um metaclasse para criar classes
A = type('A',(),{'attr':'Olá Mundo'})

#objeto = type( nome da classe - de quem ela herda - seus atributos  )
print(A.attr)
print(A)