

def soma(x:int , y:int):
    return x+y



print(__name__)  # quando ele é executado por aqui, diretamente o nome é __main__ ,
                 # quando ele é importado ele recebe o nome do arquivo, como nesse caso 'modulo'

def main():
    print(soma(4,5))
    print(soma(9,15))


if __name__ == '__main__':
    main()
