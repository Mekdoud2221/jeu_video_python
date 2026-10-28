# Logique du jeu : equipe, combats, scores
import random 
from datetime import datetime

from models import Personnage, Monstre
import utils

def creer_equipe(db):
     # Récupération de tous les personnages enregistrés dans MongoDB
    docs = list(db.personnages.find())

    # Vérifier si il ya au moins trois personnages dispo
    if len(docs) < 3:
        print("Pas assez de personnages en base, lance db_init.py en premier")
        return None
    
    # Créer une liste vide
    equipe = []
    while len(equipe) < 3:
        utils.afficher_equipe(equipe)

        noms_pris = [p.nom for p in equipe]
        print("\nPersonnages disponible :")
        for i, d in enumerate(docs, 1):
            pris = ""
            if d["nom"] in noms_pris:
                pris = "[deja choisi]"
            print(f"{i}. {d['nom']} - {d['atk']} ATK - {d['defense']} DEF - {d['hp']} HP{pris}")

        choix = int(input(f"\nChoix du personnage {len(equipe) + 1}/3 : "))
        d = docs[choix - 1]

        if d ["nom"] in noms_pris:
            print("Ce personnage est deja dans ton equipe")
            continue
        equipe.append(Personnage(d["nom"], d["atk"], d["defense"], d["hp"]))

    utils.afficher_equipe(equipe)
    return equipe

def monstre_aleatoire(db):
    docs = list(db.monstres.find())
    d = random.choice(docs)
    return Monstre(d["nom"], d["atk"], d["defense"], d["hp"])

def combats(equipe, monstre):
    # true si c'est victoire, false si c'est defaite
    tour = 1
    while True:
        print(f"\n -- Tour {tour} --")

        #l'equipe attaque en premier
        for perso in equipe:
            if perso.est_vivant():
                degats = perso.attaquer(monstre)
                print(f" {perso.nom} attaque {monstre.nom} : -{degats} HP (reste {monstre.hp})")

                if not monstre.est_vivant():
                    return True

        # puis le monstre attaque un personnage au hasard
        vivants = [p for p in equipe if p.est_vivant()]
        cible = random.choice(vivants)
        degats = monstre.attaquer(cible)
        print(f" {monstre.nom} attaque {cible.nom} : -{degats} HP (reste {cible.hp})")

        if not any(p.est_vivant() for p in equipe):
            return False

        tour += 1

def jouer(db, equipe):
    vagues = 0
    while True:
        monstre = monstre_aleatoire(db)
        print(f"\n===== VAGUE {vagues + 1} =====")
        print(f"Un {monstre} apparait")

        victoire = combats(equipe, monstre)
         
        # Si l'équipe gagne, on augmente le nombre de vagues réussies
        if victoire:
            vagues += 1
            print(f"\nVictoire contre {monstre.nom} vagues survecues : {vagues}")
             # Affichage des points de vie de chaque personnage
            print("Etat de l'equipe :")
            for p in equipe:
                print(f" {p.nom} : {p.hp}/{p.hp_max} HP")
        else:
            print("\nTon equipe a ete vaincu")
            return vagues

def sauvegarder_score(db, joueur, score):
    # Enregistrement du joueur, son score..
    db.scores.insert_one({
        "joueur" : joueur,
        "score" : score,
        "date" : datetime.now()
    })

def top_scores(db):
    # Récupération des 3 meilleurs scores
    return list(db.scores.find().sort("score", -1).limit(3))

 

