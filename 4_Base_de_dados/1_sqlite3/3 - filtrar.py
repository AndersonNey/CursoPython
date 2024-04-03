import sqlite3

conexao = sqlite3.connect(r'C:\PROJETO_PYTHON\PYTHON_VSCODE\Python_(Aulas)\aula 101 Base de Dados - sqlite3\basededados.db')  #precisei fazer isso porque tava jogando na pasta geral PYTHON_VSCODE
cursor = conexao.cursor()


cursor.execute('SELECT nome , peso FROM clientes WHERE peso >= :peso', {'peso':60})





for linha in cursor.fetchall():
    nome , peso = linha
    print(nome,peso)




cursor.close()
conexao.close()
