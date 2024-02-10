from conexaoBiblioteca import cursor, conexao

# Listartodososlivrosdisponíveis
def listarLivros():
    listagem = conexao.execute('SELECT * FROM Livro')
    for livro in listagem:
        print(livro)    

def listarUsuarios():
    listagem = conexao.execute('SELECT * FROM Usuario')
    for usuario in listagem:
        print(usuario)

def listarAutores():
    listagem = conexao.execute('SELECT * FROM Autor')
    for autor in listagem:
        print(autor)

def listarEditoras():
    listagem = conexao.execute('SELECT * FROM Editora')
    for editora in listagem:
        print(editora)

# Encontrar todos os livros emprestados no momento
def buscarLivrosEmprestados():
    listagem = conexao.execute('SELECT Livro.titulo FROM Livro INNER JOIN Emprestimo ON Livro.id = Emprestimo.id_Livro WHERE Emprestimo.status = True;')
    for livro in listagem:
        print(livro)

# Localizar os livros escritos por um autor específico
def buscarLivroporAutor():
    pass

# Verificar o número de cópias disponíveis de um determinado livro
def buscarExemplaresPorLivro():
    pass

# Mostrar os empréstimos em atraso.
def buscarEmprestimosEmAtraso():
    pass
