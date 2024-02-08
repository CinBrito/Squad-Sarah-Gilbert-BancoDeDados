import sqlite3

con = sqlite3.connect('exercicio5')

cursor = con.cursor()

"""
5. Criar uma Tabela e Inserir Dados
Crie uma tabela chamada "clientes" com os campos: id (chave
primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
registros de clientes na tabela.
"""

cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')
cursor.execute('DROP TABLE clientes')
cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo ) VALUES(1, "STELLA CARVALHO", 18, 3500.00);')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo ) VALUES(2, "JULIANA DA SILVA", 35, 500.00);')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo ) VALUES(3, "HEITOR ALENCAR", 24, 2800.00);')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo ) VALUES(4, "ISABELA ALMEIDA", 21, 1500.00);')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo ) VALUES(5, "FELIPE DIAS", 45, 7500.00);')




con.commit()
con.close