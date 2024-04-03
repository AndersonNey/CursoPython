import os
import sqlite3

# A estrutura do banco esta assim no DB Browser

# CREATE TABLE "agenda" (
# 	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
# 	`nome`	TEXT,
# 	`telefone`	TEXT UNIQUE
# )

caminho = os.path.dirname(os.path.realpath(__file__))


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()


    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()

#INSERT OR IGNORE     insira o valor na tabela caso de algum erro ignore
#lembrando que o banco possui uma regra de UNIQUE para telefone


if __name__ == '__main__':
    agenda = AgendaDB(caminho + r'\agenda.db')
    agenda.inserir('carlos','54445')
    agenda.listar()
    # agenda.buscar('luiz')

    agenda.fechar()
