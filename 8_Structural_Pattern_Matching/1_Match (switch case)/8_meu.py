
#LEMBRANDO QUE O CASE SEGUE A ORDEM E AO ENCONTRAR O QUE JA SATISFAZ ELE JA PARA.
# O '_' SEGUINIFICA VALOR GENERICO 'QUALQUER COISA'
#E SEMPRE TER CUIDADO COM A ORDEM DOS CASES
#Tutorial completo da aula

#https://peps.python.org/pep-0636/

def teste1(resposta):
    match resposta:
        case 2:
            print('FERRARI')
        case 2:
            print('LAMBORGHINI')
        case 3:
            print('NISSAN')

#teste1(2)


def teste2(resposta):
    match resposta:
        case {'carro':'100'}:
            print('FERRARI')
        case 2:
            print('LAMBORGHINI')
        case 3:
            print('NISSAN')

teste2({'carro':'100','barco':'2000' })






def teste3(resposta):
    match resposta.split():   
        case ['ls', path, *_ , utimo_item]:       #nao da para recuperar variaveis genericas
            print('$ listing files from', utimo_item)
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

teste3('ls carro mesa olá cadeira vassoura')
