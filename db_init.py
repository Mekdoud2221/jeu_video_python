
from utils import get_db

# Liste des personnages jouables
personnages = [
    {"nom": "Paladin", "atk": 20, "defense": 12, "hp": 120},
    {"nom": "Chevalier", "atk": 22, "defense": 10, "hp": 110},
    {"nom": "Berserker", "atk": 29, "defense": 6, "hp": 90},
    {"nom": "Archer", "atk": 26, "defense": 7, "hp": 85},
    {"nom": "Sorcier", "atk": 32, "defense": 4, "hp": 75},
    {"nom": "Guerrier", "atk": 24, "defense": 8, "hp": 100},
    {"nom": "Moine", "atk": 22, "defense": 9, "hp": 95},
    {"nom": "Voleur", "atk": 28, "defense": 5, "hp": 80},
    {"nom": "Chasseur", "atk": 23, "defense": 8, "hp": 90},
    {"nom": "Druide", "atk": 21, "defense": 9, "hp": 100},
]

# Liste des monstres
monstres = [
    {"nom": "Gobelin", "atk": 10, "defense": 6, "hp": 150},
    {"nom": "Orc", "atk": 10, "defense": 8, "hp": 180},
    {"nom": "Dragon", "atk": 10, "defense": 12, "hp": 200},
    {"nom": "Zombie", "atk": 10, "defense": 7, "hp": 160},
    {"nom": "Troll", "atk": 10, "defense": 10, "hp": 190},
    {"nom": "Spectre", "atk": 24, "defense": 6, "hp": 170},
    {"nom": "Golem", "atk": 21, "defense": 14, "hp": 210},
    {"nom": "Vampire", "atk": 26, "defense": 9, "hp": 175},
    {"nom": "Loup-garou", "atk": 24, "defense": 8, "hp": 185},
    {"nom": "Squelette", "atk": 19, "defense": 7, "hp": 155},
]

# Liste des scores
scores = [
    {"joueur": "sdfgg", "score": 6},
    {"joueur": "Essayez 2", "score": 9},
    {"joueur": "Try3", "score": 6},
    {"joueur": "rme", "score": 10},
    {"joueur": "dsfgddf", "score": 35},
    {"joueur": "rme", "score": 14},
    {"joueur": "rme", "score": 54},
    {"joueur": "rme", "score": 51},
]


def main():
    # Connexion à la base de données
    db = get_db()
    if db is None:
        return

    # Ajout des personnages
    db.personnages.delete_many({})
    db.personnages.insert_many(personnages)

    # Ajout des monstres
    db.monstres.delete_many({})
    db.monstres.insert_many(monstres)

    # Ajout des scores
    db.scores.delete_many({})
    db.scores.insert_many(scores)

    # Affichage du nombre d'éléments enregistrés
    print("Personnages insérés :", db.personnages.count_documents({}))
    print("Monstres insérés :", db.monstres.count_documents({}))
    print("Scores insérés :", db.scores.count_documents({}))


if __name__ == "__main__":
    main()