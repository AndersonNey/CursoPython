import pymysql.cursors


#fetchall pegar todos os registros vindas dessa consulta
#fetchmany pegar uma quantidade determinada de valores
#fetchon pegar apenas 1 linha

#se eu por acaso nao quisesse informar a base de dados nao tem problemas, mas as consultas sql teriam que incluir o banco ficando assim:
#cursor.execute('select * from clientes.clientes')        database.tabela

conexao = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    db = 'clientes',
    charset= 'utf8mb4',
    cursorclass= pymysql.cursors.DictCursor      #serve para ter as consultas como dicionario 
)


#cursor = conexao.cursor()  <-- o gerenciador de contexto ja descarta isso

with conexao.cursor() as cursor:  #isso somente facilita ,mas nao fecha a conexao
    cursor.execute('select * from clientes  ORDER BY id ASC LIMIT 100')    # LIMIT a consulta somente traria no maximo 100 registros
    resultado = cursor.fetchall()                        
    for linha in resultado:
        print(linha)
        #print(linha['id'],linha['nome'],linha['sobrenome'],linha['idade'],linha['peso']) 

cursor.close()
conexao.close()