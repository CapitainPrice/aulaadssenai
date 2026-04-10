class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = True

    def get_titulo(self): return self.__titulo
    def is_disponivel(self): return self.__disponivel
    def set_disponivel(self, status): self.__disponivel = status

    def __str__(self):
        status = "Disponível" if self.__disponivel else "Emprestado"
        return f"Título: {self.__titulo} | Autor: {self.__autor} | Status: {status}"

class Biblioteca:
    def __init__(self):
        self.livros = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)
        print("Livro cadastrado com sucesso!")

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.get_titulo() == titulo and livro.is_disponivel():
                livro.set_disponivel(False)
                return print(f"Livro '{titulo}' emprestado!")
        print("Livro não encontrado ou já emprestado.")

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.get_titulo() == titulo and not livro.is_disponivel():
                livro.set_disponivel(True)
                return print(f"Livro '{titulo}' devolvido!")
        print("Livro não encontrado ou não estava emprestado.")

    def listar_livros(self):
        if not self.livros: print("Biblioteca vazia.")
        for l in self.livros: print(l)

# Menu Simples (Exemplo de execução)
bib = Biblioteca()
while True:
    op = input("\n1-Cadastrar 2-Emprestar 3-Devolver 4-Listar 0-Sair: ")
    if op == '1': bib.cadastrar_livro(Livro(input("Título: "), input("Autor: ")))
    elif op == '2': bib.emprestar_livro(input("Título: "))
    elif op == '3': bib.devolver_livro(input("Título: "))
    elif op == '4': bib.listar_livros()
    elif op == '0': break