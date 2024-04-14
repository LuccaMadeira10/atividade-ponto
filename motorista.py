from corrida import Corrida

class Motorista:
    def __init__(self, corridas: list[Corrida], nota: int) -> None:
        self.corridas = corridas
        self.nota = nota

    def get_dict(self) -> dict:
        return {
            "Corridas": [corrida.get_dict() for corrida in self.corridas],
            "Nota": self.nota
        }