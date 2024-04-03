import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db = 'clientes',
        charset= 'utf8mb4',
        cursorclass= pymysql.cursors.DictCursor     
    )
    try:
        yield conexao
    finally:
        conexao.close()

#INSERINDO UM REGISTRO

with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome,idade,peso) VALUES (%s,%s,%s,%s)'
        cursor.execute(sql,('Jack','Moroe',112,220))
        conexao.commit()

#INSERINDO VARIOS REGISTROS DE UMA VEZ SO

with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome,idade,peso) VALUES (%s,%s,%s,%s)'

        dados = [
            ('MURIEL','FIGUEIREDO',19,55),
            ('ROSE','FIGUEIREDO',19,55),
            ('JOSE','FIGUEIREDO',19,55),
        ]

        cursor.executemany(sql,dados)

        conexao.commit()


#APAGANDO UM REGISTRO

with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id = %s'
        cursor.execute(sql,(6,))   #tem que ser uma tupla contendo o id que eu quero apagar ou a referencia
        conexao.commit()

#APAGANDO VARIOS REGISTROS

with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
        cursor.execute(sql,(7,8,9))   
        conexao.commit()

#APAGANDO DE OUTRA MANEIRA VARIOS REGISTROS (ENTRE UM RANGE)

with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
        cursor.execute(sql,(10,40))   
        conexao.commit()

#ATUALIZANDO REGISTROS

with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql,('JOANA', 5))   
        conexao.commit()



#LENDO OS REGISTROS DO BANCO DE DADOS

with conecta() as conexao:               #esse serve para fechar a conexao 
    with conexao.cursor() as cursor:      #o professor disse que esse serve para fechar o cursor, mas ele nao implementou o cursor.close()  eu acho 
        cursor.execute('select * from clientes  ORDER BY id ASC LIMIT 100')   
        resultado = cursor.fetchall()                        
        for linha in resultado:
            print(linha)

