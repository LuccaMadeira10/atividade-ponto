from motristaDAO import MotoristasDAO
from motorista import Motorista
from corrida import Corrida
from passageiro import Passageiro

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Digite um comando: ")
            if command == "sair":
                print("Fim, até logo!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido")

class MotoristaCLI(SimpleCLI):
    def __init__(self, motoristaDAO: MotoristasDAO):
        super().__init__()
        self.motoristaDAO = motoristaDAO
        self.add_command("criar", self.cria_motorista)
        self.add_command("ler", self.le_motorista)
        self.add_command("atualizar", self.atualiza_motorista)
        self.add_command("excluir", self.exclui_motorista)

    def cria_motorista(self):
        corridas = []
        notas = 0
        n_corridas = 0

        while True:
            n_corridas += 1

            print(f'Corrida: {n_corridas}')

            nota = int(input('\tNota: '))
            distancia = float(input('\tDistancia: '))
            valor = float(input('\tValor: '))

            print('\tPassageiro')
            nome = str(input('\t\tNome: '))
            documento = str(input('\t\tDocumento: '))

            passageiro = Passageiro(nome, documento)

            corrida = Corrida(nota, distancia, valor, passageiro)

            corridas.append(corrida)
            notas += nota

            if input('Deseja cadastrar outra corrida? "s/n" ').lower() == 'n':
                break

        nota_media = int(notas / n_corridas)
        motorista = Motorista(corridas, nota_media)

        self.motoristaDAO.cria_motorista(motorista)

    def le_motorista(self):
        id = input("ID do motorista: ")
        motorista = self.motoristaDAO.le_motorista_by_id(id)
        if motorista:
            print(f'Nota: {motorista["nota"]}')
            print('Corridas: ')
            for corrida in motorista["corridas"]:
                passageiro = corrida["passageiro"]

                print(f'\tNota: {corrida["nota"]}')
                print(f'\tDistância: {corrida["distancia"]}')
                print(f'\tValor: {corrida["valor"]}')

                print('\tPassageiro: ')
                print(f'\t\tNome: {passageiro["nome"]}')
                print(f'\t\tDocumento: {passageiro["documento"]}')

    def atualiza_motorista(self):
        id = input("ID do motorista: ")

        corridas = []
        notas = 0
        n_corridas = 0

        while True:
            n_corridas += 1

            print(f'Corrida: {n_corridas}')

            nota = int(input('\tNota: '))
            distancia = float(input('\tDistância: '))
            valor = float(input('\tValor: '))

            print('\tPassageiro')
            nome = str(input('\t\tNome: '))
            documento = str(input('\t\tDocumento: '))

            passageiro = Passageiro(nome, documento)

            corrida = Corrida(nota, distancia, valor, passageiro)

            corridas.append(corrida)
            notas += nota

            if input('Deseja atualizar outra corrida? "s/n" ').lower() == 'n':
                break

        nota_media = int(notas / n_corridas)
        motorista_atualizado = Motorista(corridas, nota_media)

        self.motoristaDAO.atualiza_motorista(id, motorista_atualizado)

    def exclui_motorista(self):
        id = input("ID do motorista: ")
        self.motoristaDAO.apaga_motorista(id)

    def run(self):
        print("Bem-vindo ao Motorista CLI")
        print("Comandos disponíveis: criar, ler, atualizar, excluir, sair")
        super().run()