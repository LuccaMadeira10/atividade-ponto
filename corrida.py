from passageiro import Passageiro

class Corrida:
    def __init__(self, nota: int, distancia: float, valor: float, passageiro: Passageiro) -> None:
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

    def get_dict(self) -> dict:
        return {
            "Nota": self.nota,
            "Distancia": self.distancia,
            "Valor": self.valor,
            "Passageiro": self.passageiro.get_dict()
        }