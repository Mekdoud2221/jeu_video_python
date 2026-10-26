
# Fonctions  connexion, saisies, affichage

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


def get_db():
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
    try:
        client.admin.command("ping")
    except ServerSelectionTimeoutError:
        print("Impossible de se connecter a MongoDB. Le service est-il lance ?")
        return None
    return client["jeu_video"]