class Veiculo:
    def __init__(self, modelo, placa):
        self.__modelo = modelo
        self.__placa = placa
        self.__alugado = False

    def get_placa(self): return self.__placa
    def is_alugado(self): return self.__alugado
    def set_alugado(self, status): self.__alugado = status
    def __str__(self): return f"Modelo: {self.__modelo} | Placa: {self.__placa}"

class Locadora:
    def __init__(self):
        self.frota = []

    def cadastrar_veiculo(self, veiculo):
        self.frota.append(veiculo)

    def alugar_veiculo(self, placa):
        for v in self.frota:
            if v.get_placa() == placa and not v.is_alugado():
                v.set_alugado(True)
                return print("Veículo alugado!")
        print("Veículo indisponível ou não encontrado.")

    def devolver_veiculo(self, placa):
        for v in self.frota:
            if v.get_placa() == placa and v.is_alugado():
                v.set_alugado(False)
                return print("Veículo devolvido!")
        print("Placa não corresponde a um veículo alugado.")

    def listar_disponiveis(self):
        for v in self.frota:
            if not v.is_alugado(): print(v)