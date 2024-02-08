import sqlite3

conexao = sqlite3.connect('bd01')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

"""
2. Insira pelo menos 5 registros de alunos na tabela que você criou no
exercício anterior.
"""

cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "João", 20, "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Maria", 22, "Ciência da Computação")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Pedro", 21, "Administração")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Ana", 19, "Medicina")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Paulo", 23, "Direito")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(6, "Carla", 20, "Arquitetura")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(7, "Mariana", 22, "Economia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(8, "Lucas", 21, "Psicologia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(9, "Fernanda", 20, "Design")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(10, "Rafael", 24, "Biologia")')


conexao.commit()
conexao.close()