from conexaoBiblioteca import cursor, conexao
import sqlite3

conexao = sqlite3.connect('biblioteca')
cursor = conexao.cursor()

# Cintia aqui. Não imagino situação de alterar autor ou editora por conta dos poucos campos,
# então deixei só esses dois pra criar. Não esqueçam que tem que dizer que parâmetro/campo 
# vai ser alterado então tem que entrar um if nesse alterar aí, ou só escolham um campo
# pra facilitar =D

def alterarUsuario():
    pass

def alterarLivro():
    pass

def removerUsuario():
    cursor.execute('DELETE FROM Usuario where id = ?', (1))        

def removerAutor():
     cursor.execute('DELETE FROM Autor where id = ?', (2))  

def removerEditora():
    cursor.execute('DELETE FROM Editora where id = ?', (1))  

def removerLivro():
    cursor.execute('DELETE FROM Livro where id = ?', (2)) 

conexao.commit()
conexao.close