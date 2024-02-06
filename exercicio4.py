import sqlite3

conexao = sqlite3.connect('alunos')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "João", 20, "Engenharia")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Maria", 22, "Ciência da Computação")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Pedro", 21, "Administração")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Ana", 19, "Medicina")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Paulo", 23, "Direito")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(6, "Carla", 20, "Arquitetura")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(7, "Mariana", 22, "Economia")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(8, "Lucas", 21, "Psicologia")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(9, "Fernanda", 20, "Design")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(10, "Rafael", 24, "Biologia")')
# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Amanda", 18, "Engenharia")')

# dados1 =  cursor.execute('SELECT * FROM alunos')
# for aluno in dados1:
#     print(aluno)
# print('-----------------------')

# dados2 = cursor.execute('SELECT nome, idade FROM alunos WHERE idade >=20')
# for aluno in dados2:
#     print(aluno)
# print('-----------------------')

# dados3 = cursor.execute('SELECT nome FROM alunos WHERE curso="Engenharia" ORDER BY nome')
# for aluno in dados3:
#     print(aluno)
# print('-----------------------')

# dados4 = cursor.execute('SELECT * FROM alunos')
# soma = 0
# for aluno in dados4:
#     soma += 1
# print(f'Total de Alunos: {soma}')

# 4.AtualizaçãoeRemoção
# a) Atualize a idade de um aluno específico na tabela.
# b) Remova um aluno pelo seu ID.

cursor.execute('UPDATE alunos SET idade = 28 WHERE id = 3')
cursor.execute('DELETE FROM alunos WHERE id = 4')

conexao.commit()
conexao.close