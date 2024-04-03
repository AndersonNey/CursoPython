# With dicts
# case {'name': _, 'last': 'Doe'}:
# case {'name': 'Otávio' as name, 'last': 'Doe'} as data:

#lembrando que apenas um case é executado 

def execute_command(command):
    match command:
        case {'chave': 'ls', 'directories': [_, *_]}:   #ou seja , esta condicao precisa que exista duas chaves 
            for directory in command['directories']:  #pegando o valor da chave directories dentro do dicionario command
                print('$ listing ALL directories from', directory)
        
        case {'chave': 'ls'}: #se encontrar o par de chave-valor vai fazer isso independente se tem mais chave no dicionario ou nao
            print('olá')
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


execute_command({'chave': 'ls' , 'directories': ['/users' , '/etc']})
