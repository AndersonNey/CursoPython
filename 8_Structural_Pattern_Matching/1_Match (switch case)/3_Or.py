

def execute_command(command):
    match command.split():
        case ['ls' | 'list', *directories]:   #ou seja, tanto faz o primeiro comando ser 'ls' ou 'list' esse parametro vai ser executado
            for directory in directories:
                print('$ listing directory from', directory)
        case ['cd' | 'change', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')



execute_command('ls /home /users /etc --force')
execute_command('list /home /users /etc --force')

execute_command('cd /home')
execute_command('change /home')