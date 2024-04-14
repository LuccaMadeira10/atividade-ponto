from database import Database
from motristaDAO import MotoristasDAO
from motoristaCLI import MotoristaCLI


motorista_DAO = MotoristasDAO("atlas_cluster","usuarios") ##fiz usando o atlas 

motorista_CLI = MotoristaCLI(motorista_DAO)
motorista_CLI.run()