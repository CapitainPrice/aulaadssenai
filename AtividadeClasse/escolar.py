class Aluno:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
        self.__notas = []

    def get_matricula(self): return self.__matricula
    def get_nome(self): return self.__nome
    def adicionar_nota(self, nota): self.__notas.append(nota)
    
    def calcular_media(self):
        return sum(self.__notas) / len(self.__notas) if self.__notas else 0

    def __str__(self):
        return f"Aluno: {self.__nome} | Matrícula: {self.__matricula} | Média: {self.calcular_media():.2f}"

class Escola:
    def __init__(self):
        self.alunos = []

    def matricular_aluno(self, aluno):
        self.alunos.append(aluno)

    def lancar_nota(self, matricula, nota):
        for a in self.alunos:
            if a.get_matricula() == matricula:
                a.adicionar_nota(nota)
                return print("Nota lançada!")
        print("Aluno não encontrado.")

    def listar_alunos(self):
        for a in self.alunos: print(a)

# Menu do Sistema Escolar
escola = Escola()
while True:
    print("\n--- ESCOLA ---")
    op = input("1-Matricular 2-Lançar Nota 3-Listar 0-Sair: ")
    if op == '1': 
        escola.matricular_aluno(Aluno(input("Nome: "), input("Matrícula: ")))
    elif op == '2': 
        escola.lancar_nota(input("Matrícula: "), float(input("Nota: ")))
    elif op == '3': 
        escola.listar_alunos()
    elif op == '0': break