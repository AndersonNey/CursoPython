#from formata import preco    ocorre erro se importa desse jeito  nao sei porque


from vendas.formata import preco     # importando para usar a funçao real()           




def aumento(valor , porcentagem,formata=False):
    r = valor + (valor*porcentagem/100)
    
    if formata:
        return preco.real(r)
    else:
        return r

def reducao(valor , porcentagem,formata=False):
    r = valor - (valor*porcentagem/100)

    if formata:
        return preco.real(r)
    else:
        return r

