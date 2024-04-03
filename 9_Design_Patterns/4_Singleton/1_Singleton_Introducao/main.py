#se ela ja foi instaciada uma vez eu quero que ela retorne o mesmo objeto

#quando chama o new é porque estou criando uma nova classe

#o super dessa classe é o object ,ou seja , esta inplicito porque é o padrao

#https://stackoverflow.com/questions/38728839/why-does-if-not-none-return-true
#https://stackoverflow.com/questions/3289601/null-object-in-python


#toda vez que uma instancia for feita o init vai ser chamado e isso é um problema


class AppSettings:
    _instance = None

    def __new__(cls, *args,**kwargs):
        if not cls._instance:   #isso so vai ocorrer se ela nao ja tiver sido criada antes. # se ela  ja tiver sido criada sempre vai retornar _instance
            cls._instance = super().__new__(cls,*args,**kwargs)
        return cls._instance

    def __init__(self) -> None:
        self.tema = 'o tema escuro'
        self.font = '18px'


if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = 'O tema claro'
    print(as1.tema)

    as2 = AppSettings()   #essa inicializacao zerou a classe denovo (voltou tudo ao padrao)(isso nao ocorre em classe que nao tem __init__)
    print(as1.tema)
