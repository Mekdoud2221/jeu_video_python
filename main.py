# Menu principal du jeu

import utils
import game

# Demarrer une partie
def demarrer_partie(db):
    nom = utils.saisir_nom() # demander le nom du joueur
    equipe = game.creer_equipe(db) # choisir le perso

    if equipe is None:
        return

    print("\nLe combat commence !")
    score = game.jouer(db, equipe)

    # Enregistrer le score du joueur
    game.sauvegarder_score(db, nom, score)
    print(f"\nPartie terminee {nom} ! Score : {score} vague(s) survecue(s).")

    # afficher le meilleur score
    utils.afficher_classement(game.top_scores(db))


def main():
    db = utils.get_db()

    if db is None:
        return

    # afficher le menu du depart
    while True:
        print("\n===== JEU DE COMBAT =====")
        print("1. Demarrer le jeu")
        print("2. Afficher le classement")
        print("3. Quitter")

        choix = int(input("Ton choix : "))

        # verifier le choix
        while choix < 1 or choix > 3:
            choix = int(input("Choix invalide. Entre 1 et 3 : "))

        if choix == 1:
            demarrer_partie(db)
        elif choix == 2:
            utils.afficher_classement(game.top_scores(db))
        else:
            print("A bientot !")
            break

# lancer le jeu
if __name__ == "__main__":
    main()
