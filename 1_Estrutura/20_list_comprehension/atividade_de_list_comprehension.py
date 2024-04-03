carrinho = []

carrinho.append(('produto1', 30))
carrinho.append(('produto2', 20))
carrinho.append(('produto3', 50))

# fazendo dessa maneira que ocupa mais epaço
total=0
for valor in carrinho:
    total+=valor[1]

print(total)

#fazendo com list comprehension

total1 = sum([float(y) for x,y in carrinho])

print(total1)