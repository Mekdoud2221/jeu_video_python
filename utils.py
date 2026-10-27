# Fonctions de connexion, saisies et affichage

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

# Connexion à la base jeu_video
def get_db():
    # Attendre au maximum 3 secondes
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)

    try:
        # Vérifier que MongoDB fonctionne
        client.admin.command("ping")
    except ServerSelectionTimeoutError:
        print("Impossible de se connecter à MongoDB. Le service est-il lancé ?")
        return None

    return client["jeu_video"]