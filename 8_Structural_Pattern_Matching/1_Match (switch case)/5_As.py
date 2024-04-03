

# AS - esta dando o valor a uma variavel com o que esta atras do 'as' ,para poder usar em outros lugares  (apelido)

def execute_command(command):
    match command.split():
        case ['ls' | 'list' as the_command, *directories] as the_list if len(directories) > 1:
            for directory in directories:
                print('$ listing ALL directories from', directory)
            print(f'{the_command=}, {the_list=}')
        case ['ls' | 'list', *directories] if len(directories) <= 1:
            print('$ listing ONE directory from', directories[0])
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code' , the_list)


execute_command('ls /home/ /Users /mais')
execute_command('ls /one/')