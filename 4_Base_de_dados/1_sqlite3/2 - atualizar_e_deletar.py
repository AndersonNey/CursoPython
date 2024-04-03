import sqlite3

conexao = sqlite3.connect(r'C:\PROJETO_PYTHON\PYTHON_VSCODE\Python_(Aulas)\aula 101 Base de Dados - sqlite3\basededados.db')  #precisei fazer isso porque tava jogando na pasta geral PYTHON_VSCODE
cursor = conexao.cursor()

#alterando id 13
cursor.execute('UPDATE clientes SET nome = :nome WHERE id = :id' , {'nome':'joana','id': 13})
conexao.commit()

cursor.execute('DELETE FROM clientes WHERE id=:id' , {'id': 13})
conexao.commit()


cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
    identificador , nome , peso = linha
    print(identificador,nome,peso)




cursor.close()
conexao.close()
