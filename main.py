# Menu principal du jeu

import utils
import game


def demarrer_partie(db):
    nom = utils.saisir_nom()
    equipe = game.creer_equipe(db)
    if equipe is None:
        return

    print("\nLe combat commence !")
    score = game.jouer(db, equipe)

    game.sauvegarder_score(db, nom, score)
    print(f"\nPartie terminee {nom} ! Score : {score} vague(s) survecue(s).")
    utils.afficher_classement(game.top_scores(db))


def main():
    db = utils.get_db()
    if db is None:
        return

    while True:
        print("\n===== JEU DE COMBAT =====")
        print("1. Demarrer le jeu")
        print("2. Afficher le classement")
        print("3. Quitter")
        choix = utils.saisir_entier("Ton choix : ", 1, 3)

        if choix == 1:
            demarrer_partie(db)
        elif choix == 2:
            utils.afficher_classement(game.top_scores(db))
        else:
            print("A bientot !")
            break


if __name__ == "__main__":
    main()