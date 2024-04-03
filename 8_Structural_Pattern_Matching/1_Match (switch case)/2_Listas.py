def execute_command(command):
    match command.split():   # separa cada palavra para item de uma lista
        case ['ls', path, *resto, utimo_item]:   # [se o primeiro item da lista for 'ls' , pega o segundo item da lista e seta em path , todos os itens restantes vao fica na variavel 'resto' , o ultimo item da lista ]
            print('$ listing files from', resto , utimo_item)
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

execute_command('ls carro mesa olá cadeira vassoura')




def execute_command1(command):
    match command.split():  
        case ['ls', *directories, '--force']:
            for directory in directories:
                print('$ listing files FORCED', directory)
        case ['ls', *directories]:
            for directory in directories:
                print('$ listing files', directory)    

        case ['cd', path]:
            print('$ changing directory to', path)
        case _:
            print('$ command not implemented')


execute_command1('ls /home /users /etc --force')
execute_command1('ls /home /users /etc')