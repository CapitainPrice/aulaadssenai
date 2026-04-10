class Animal:
    def __init__(self, nome, especie, dono):
        self.__nome = nome
        self.__especie = especie
        self.__dono = dono

    def get_nome(self): return self.__nome
    def get_dono(self): return self.__dono
    def __str__(self): return f"Animal: {self.__nome} ({self.__especie}) | Dono(a): {self.__dono}"

class Clinica:
    def __init__(self):
        self.pacientes = []

    def cadastrar_animal(self, animal):
        self.pacientes.append(animal)

    def buscar_pelo_dono(self, nome_dono):
        encontrados = [a for a in self.pacientes if a.get_dono().lower() == nome_dono.lower()]
        if encontrados:
            for e in encontrados: print(e)
        else:
            print("Nenhum animal cadastrado para este dono.")

    def listar_todos(self):
        for a in self.pacientes: print(a)