import sqlite3
conexao=sqlite3.connect("banco")
cursor = conexao.cursor()

cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1,"Luana",22, "Ciência da Computação");')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(2,"Maria",25, "Sistemas da Informação");')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(3,"Amanda",30, "Sistemas da Informação");')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4,"Amanda",20, "Engenharia da Computação");')


conexao.commit()
conexao.close()