import sqlite3

def marcarLivroDevolvido(id_emprestimo):
    conexao = sqlite3.connect('biblioteca')
    cursor = conexao.cursor()

    
    sql_query = 'UPDATE emprestimos SET devolvido = 1 WHERE id_emprestimo = ?'
    values = (id_emprestimo,)
    cursor.execute(sql_query, values)

   
    conexao.commit()

   
    livros_devolvidos = conexao.execute("SELECT * FROM emprestimos WHERE id_emprestimo = ? AND devolvido = 1", (id_emprestimo,))
    livro_devolvido = livros_devolvidos.fetchone()
    if livro_devolvido:
        print("O livro foi marcado como devolvido com sucesso.")
    else:
        print("O livro não foi marcado como devolvido.")

   
    conexao.close()


id_emprestimo_1 = 1
id_emprestimo_2 = 4

marcarLivroDevolvido(id_emprestimo_1)
marcarLivroDevolvido(id_emprestimo_2)
