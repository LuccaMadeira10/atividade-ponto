from pymongo import MongoClient
from bson.objectid import ObjectId
from database import Database
from motorista import Motorista

class MotoristasDAO:
    def __init__(self, database: str, collection: str) -> None:
        self.db = Database(database, collection)

    def cria_motorista(self, motorista: Motorista):
        try:
            res = self.db.collection.insert_one(motorista.get_dict())
            print(f"Motorista criado com o ID: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Erro ao criar motorista: {e}")
            return None

    def le_motorista_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Motorista encontrado: {res}")
            return res
        except Exception as e:
            print(f"Erro ao encontrar motorista: {e}")
            return None

    def atualiza_motorista(self, id: str, motorista: Motorista):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": motorista.get_dict()})
            print("Motorista atualizado com sucesso")
            return res.modified_count
        except Exception as e:
            print(f"Erro ao atualizar motorista: {e}")
            return None

    def apaga_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print("Motorista deletado com sucesso")
            return res.deleted_count
        except Exception as e:
            print(f"Erro ao deletar motorista: {e}")
            return None