import sqlite3

conexao = sqlite3.connect('biblioteca')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE Usuario(id INT PRIMARY KEY, nome VARCHAR(255), nacionalidade VARCHAR(255), telefone VARCHAR(20));')
# cursor.execute('CREATE TABLE Autor(id INT PRIMARY KEY, nome VARCHAR(255), nacionalidade VARCHAR(255));')
# cursor.execute('CREATE TABLE Editora(id INT PRIMARY KEY, nome VARCHAR(255));')
# cursor.execute('CREATE TABLE Livro (id INT PRIMARY KEY, titulo VARCHAR(255), genero VARCHAR(50), id_Editora INT, status BOOLEAN, id_Autor INT, Exemplares INT, FOREIGN KEY (id_Autor) REFERENCES Autor(id), FOREIGN KEY (id_Editora) REFERENCES Editora(id));')
# cursor.execute('CREATE TABLE Emprestimo (id INT PRIMARY KEY, id_Usuario INT, id_Livro INT, status VARCHAR(20), data_emprestimo DATE, data_devolucao DATE, renovacao INT, FOREIGN KEY (id_Usuario) REFERENCES Usuario(id), FOREIGN KEY (id_Livro) REFERENCES Livro(ID), FOREIGN KEY (status) REFERENCES Livro(status));')


conexao.commit()
conexao.close