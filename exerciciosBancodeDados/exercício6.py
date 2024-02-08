import sqlite3

con = sqlite3.connect('exercicio5')

cursor = con.cursor()

# cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')
#cursor.execute('DROP TABLE clientes')
# cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo ) VALUES(1, "STELLA CARVALHO", 18, 3500.00);')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo ) VALUES(2, "JULIANA DA SILVA", 35, 500.00);')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo ) VALUES(3, "HEITOR ALENCAR", 24, 2800.00);')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo ) VALUES(4, "ISABELA ALMEIDA", 21, 1500.00);')
# cursor.execute('INSERT INTO clientes(id, nome, idade, saldo ) VALUES(5, "FELIPE DIAS", 45, 7500.00);')

"""
6. Consultas e Funções Agregadas
Escreva consultas SQL para realizar as seguintes tarefas:
"""

# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30;')
result_a = cursor.fetchall()
print("a) Nome e idade dos clientes com idade superior a 30 anos:")
for row in result_a:
    print(row)

# b) Calcule o saldo médio dos clientes.
cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes;')
result_b = cursor.fetchone()
print("\nb) Saldo médio dos clientes:")
print(result_b[0])

# c) Encontre o cliente com o saldo máximo.
cursor.execute('SELECT * FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes);')
result_c = cursor.fetchone()
print("\nc) Cliente com o saldo máximo:")
print(result_c)

# d) Conte quantos clientes têm saldo acima de 1000.
cursor.execute('SELECT COUNT(*) AS total_clientes_saldo_acima_1000 FROM clientes WHERE saldo > 1000;')
result_d = cursor.fetchone()
print("\nd) Número de clientes com saldo acima de 1000:")
print(result_d[0])

con.close()
