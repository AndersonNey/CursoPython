from pessoa import Pessoa

#apartir do momento que eu crio pessoas elas ,sao diferentes ,mas podem utilizar os metodos e de 
#forma totalmente independentes, o estado de uma nao interfere na outra  nesse caso (nao sei ainda como fazer )

p1 = Pessoa('luiz',17)
p2 = Pessoa('João', 32)

print(p1.ano_atual)      # da pra usar ate a variavel geral para as pessoas criadas
print(Pessoa.ano_atual)  #e tanto para a classe em si


resposta = p1.ano_nascimento()
print(resposta)
resposta = p2.ano_nascimento()
print(resposta)

p1.comer('banana')
p2.comer('laranja')
p1.falar('carro')




# p1.comer('maça')
# p1.comer('maça')
# p1.parar_de_comer()
# p1.parar_de_comer()
# p1.comer('maça')
# p1.falar('carro')
# p1.parar_de_comer()
# p1.falar('moto')
# p1.falar('trem')
# p1.parar_de_falar()
# p1.parar_de_falar()











# p1.nome = 'Luiz'         #nesse caso estou criando um atributo da pessoa 1 , lemnbrando que nem precisaria do metodo construtor para isso funcionar
# print(p1.nome)

