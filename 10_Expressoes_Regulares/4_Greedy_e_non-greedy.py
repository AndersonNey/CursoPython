

# *     0 ou n       
# +     1 ou n      
# ?     0 ou 1       


import re

texto = """
<p>Frase 1</p> <p>Eita</p> <p>Qualquer Frase</p> <div>Frase 4</div>
"""

           # Nesse caso {1,3} vai ser aplicado a [pdiv] ,ou seja, [pdiv] pode ser de 1 a 3 letras  
print(re.findall(r'<[pdiv]{1,3}>',texto))
#terminal
# ['<p>', '<p>', '<p>', '<div>']

                                  #essa barra invertida é para escapar a barra
print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>',texto)) #nesse caso ele checa sempre se tem algo ainda que pode fechar depois e vai checando ate o final (GULOSO) 
#Terminal
# ['<p>Frase 1</p> <p>Eita</p> <p>Qualquer Frase</p> <div>Frase 4</div>']


print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>',texto)) #nesse caso ele fecha ja na primeira ocorrencia de fechamento (NAO GULOSO) 
#Terminal
# ['<p>Frase 1</p>', '<p>Eita</p>', '<p>Qualquer Frase</p>', '<div>Frase 4</div>']






