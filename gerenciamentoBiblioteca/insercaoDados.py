from conexaoBiblioteca import cursor, conexao

def inserirUsuario(idUsuario, nomeUsuario, nacionalidadeUsuario, telefoneUsuario):
    sql_query = 'INSERT INTO Usuario(id, nome, nacionalidade, telefone) VALUES (:id, :nome, :nacionalidade, :telefone)'
    values = {'id': idUsuario, 'nome': nomeUsuario, 'nacionalidade': nacionalidadeUsuario, 'telefone': telefoneUsuario}
    cursor.execute(sql_query, values)
    conexao.commit()
    conexao.close

def inserirAutor(idAutor, nomeAutor, nacionalidadeAutor):
    sql_query = 'INSERT INTO Autor(id, nome, nacionalidade) VALUES (:id, :nome, :nacionalidade)'
    values = {'id': idAutor, 'nome': nomeAutor, 'nacionalidade': nacionalidadeAutor}
    cursor.execute(sql_query, values)
    conexao.commit()
    conexao.close

def inserirEditora(idEditora, nomeEditora):
    sql_query = 'INSERT INTO Editora(id, nome) VALUES (:id, :nome)'
    values = {'id': idEditora, 'nome': nomeEditora}
    cursor.execute(sql_query, values)
    conexao.commit()
    conexao.close


def inserirLivro(idLivro, titulo, genero, idEditora, idAutor, Exemplares):
    sql_query = 'INSERT INTO Livro(id, titulo, genero, id_Editora, status, id_Autor, Exemplares) VALUES (:id, :titulo, :genero, :id_Editora, :status, :id_Autor, :Exemplares)'
    values = {'id': idLivro, 'titulo': titulo, 'genero': genero, 'id_Editora': idEditora, 'status': True, "id_Autor": idAutor, "Exemplares": Exemplares}
    cursor.execute(sql_query, values)
    conexao.commit()
    conexao.close


# inserirUsuario("Fatima Abreu", "Brasil", "21 99999999")
# cursor.execute('UPDATE Usuario SET id=1 WHERE nome="Fatima Abreu"')
# conexao.commit()
# inserirUsuario(2, "Andressa Cabral", "Brasil", "21 989898989")  
# inserirAutor(1, "Robert Cecil Martin", "EUA")
# inserirEditora(1, "Alta Books")
# inserirLivro(1, "Código Limpo", "Livro Técnico", 1,1,5)
    

inserirUsuario(31, "Aurora Martins", "Argentina", "89 7898596874") 
inserirUsuario(32, "Elijah Keith", "Italia", "22 659852116")
inserirUsuario(33, "Ruanito Marchal", "Mexico", "88 999 8787")

inserirAutor(25, "Jane Austen", "Inglaterra")
inserirAutor(26, "Virginia Woolf", "EUA")
inserirAutor(27, "Agatha Cristie", "Brasil")

inserirEditora(11, "Penguin Random House")
inserirEditora(12, "Harper Collins Publishers")
inserirEditora(13, "Simon & Schuster")

inserirLivro(2,"Orgulho e Preconceito", "Drama", 11, 25, 87)
inserirLivro(3,"Ao Farol", "Literatura", 12, 26, 55)
inserirLivro(4, "Mistério do Relógio", "Crime", 13, 27, 66)



"""
Quem for responsável por inserir novas entradas é só usar a função como
feito aqui em cima. Chama a função e insere os parâmetros na ordem ;)
"""

# teste = conexao.execute('SELECT * FROM Usuario')
# for usuario in teste:
#     print(usuario)

# teste2 = conexao.execute('SELECT * FROM Autor')
# for autor in teste2:
#     print(autor)

# teste3 = conexao.execute('SELECT * FROM Editora')
# for editora in teste3:
#     print(editora)

# teste4 = conexao.execute('SELECT * FROM Livro')
# for livro in teste4:
#     print(livro)
