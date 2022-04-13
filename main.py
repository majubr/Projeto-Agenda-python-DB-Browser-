import sqlite3

class Agenda:
    def __init__(self, arquivo):
        self.conexao = sqlite3.connect (arquivo)
        self.cursor = self.conexao.cursor ()

    def inserir (self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?,?)'
        self.cursor.execute (consulta, (nome, telefone))
        self.conexao.commit()

    def editar (self,nome, telefone,id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone,id))
        self.conexao.commit()

    def excluir (self,id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conexao.commit()

    def listar (self):
        self.cursor.execute('SELECT * FROM agenda')
        for i in self.cursor.fetchall():
            print (i)

    def buscar (self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE?'
        self.cursor.execute(consulta, (f'%{valor}%',))
        for i in self.cursor.fetchall():
            print (i)

    def fechar (self):
         self.cursor.close()


if __name__ == '__main__':
    agenda = Agenda('agenda.db')
    agenda.inserir('Marcelo','123456')
    agenda.inserir('Joao', '143456')
    agenda.inserir('Eduardo', '123656')
    agenda.inserir('Livia', '923456')
    agenda.inserir('Pequi', '166456')
    agenda.inserir('Profeta', '020456')
    agenda.listar()
