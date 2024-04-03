


#codigo usando IF - ELIF - ELSE
def execute_command(command):
    if command =='ls':
        print('$ listing files')
    elif command =='cd':
        print('$ changing directory')
    else:
        print('$ command not implemented')
    
    print('...rest of the code')

#codigo usando MATCH  (tipo switch case)

def execute_command1(command):
    match command:
        case 'ls':
            print('$ listing files')
        case 'cd':
            print('$ changing directory')
        case _:  #Nao obrigatorio  (esse _ é uma variavel normal)(no match ele possui algumas funçoes neste caso ele esta fanzendo o papel do else , ou seja, vai ser executado caso nao for nenhum dos casos )
            print('$ command not implemented')
    
    print('...rest of the code')












