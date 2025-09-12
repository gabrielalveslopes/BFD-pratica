class Livro:
    def __init__(self, titulo, autor):
        self.titulo = "O senhor dos aneis"
        self.autor = "J.R.R Tolkien"
        
    def exibir_dados(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}")

livro = Livro('1984', 'George Orwell')
livro.exibir_dados()