import sqlite3

conexao = sqlite3.connect(r'C:\PROJETO_PYTHON\PYTHON_VSCODE\Python_(Aulas)\aula 101 Base de Dados - sqlite3\basededados.db')  #precisei fazer isso porque tava jogando na pasta geral PYTHON_VSCODE
cursor = conexao.cursor()


cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'nome TEXT,'
    'peso REAL'
')')
#se eu mnadar um valor do tipo inteiro para o ponto flutuante o banco ira converte de inteiro para ponto flutuante


#maneira perigosa pode permitir o sql inject

cursor.execute('INSERT INTO clientes (nome,peso) VALUES ("Luiz Otávio",80.5)')
conexao.commit()   #o professor nao falou, mas eu li na internet que serve para confirmar a transferencia

#maneira um pouco mais segura
cursor.execute('INSERT INTO clientes (nome,peso) VALUES (?,?)', ('Maria',50))
conexao.commit()

#outra maneira
cursor.execute('INSERT INTO clientes (nome,peso) VALUES (:nome,:peso)', {'nome':'joaozinho','peso':25})
conexao.commit()

#outramaneira  (como eu tirei do inicio as colunas que eu estaria me referindo eu preciso mandar 
#               o id como None (isso ja estava acontecendo de forma automatica com as outras maneiras de enviar).)
#              Agora eu tenho que deixar explicito porque o banco nao saberia as quais colunas eu estaria me referindo ))

cursor.execute('INSERT INTO clientes VALUES (:id , :nome,:peso)', {'id':None,'nome':'Daniel','peso':113})
conexao.commit()



cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    identificador , nome , peso = linha
    print(identificador,nome,peso)




cursor.close()
conexao.close()
