
from livro import Livro

livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("1984", "George Orwell", 1949)
livro3 = Livro("Brave New World", "Aldous Huxley", 1932)
livro4 = Livro("Another Book from 1949", "Another Author", 1949)

livro2.emprestar()

print(f"Disponível após emprestar '{livro2.titulo}': {livro2.disponivel}")

livros_disponiveis_1949 = Livro.verificar_disponibilidade(1949)
print("Livros disponíveis publicados em 1949:")
for livro in livros_disponiveis_1949:
    print(livro)
