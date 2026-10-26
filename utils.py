
# Fonctions  connexion, saisies, affichage

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

# connexion a la base jeu_video
def get_db():
    # attente max de 3 secondes si le serveur ne repond pas
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
    try:
           # ping pour verifier que MongoDB est bien lance
        client.admin.command("ping")
    except ServerSelectionTimeoutError:
        print("Impossible de se connecter a MongoDB. Le service est-il lance ?")
        return None
    return client["jeu_video"]
