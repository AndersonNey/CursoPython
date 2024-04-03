

class A:
    def __init__(self):
        pass

    def __del__(self):   #esse metodo sempre vai ser chamado quando esse objeto nao ta sendo mais usado no programa , nem sempre vai ser executado TER CUIDADO.
        print('objeto coletado')
    
    def __str__(self) -> str:
        return 'viu retornei, oi'

    def __len__(self):
        return 55

a = A()
print(a)
print(len(a))