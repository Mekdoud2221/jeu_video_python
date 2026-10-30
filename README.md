# Jeu vidéo en Python

## Présentation

Ce projet est un petit jeu de combat en Python. Le joueur choisit 3 personnages et affronte des monstres jusqu'à ce que son équipe perde.

Les données sont enregistrées dans MongoDB.

## Installation

- Installer Python 3.8 ou plus.
- Installer et lancer MongoDB.
- Installer PyMongo avec la commande :

-pip install pymongo

## Lancer le jeu

Pour remplir la base de données :

- python db_init.py

--Pour lancer le jeu :

- python main.py


## Règles du jeu

- Choisir 3 personnages différents.
- L'équipe attaque en premier.
- Le monstre attaque ensuite un personnage vivant au hasard.
- Les dégâts dépendent de l'attaque et de la défense. Il y a toujours au moins 1 dégât.
- Les points de vie ne sont pas restaurés entre les combats.
- Le score correspond au nombre de vagues gagnées.
- Le classement affiche les 3 meilleurs scores.

## Base de données

La base s'appelle `jeu_video`. Elle contient 3 collections :

- `personnages` : les personnages du jeu.
- `monstres` : les monstres à combattre.
- `scores` : les noms des joueurs, leurs scores et la date.

## Fichiers

- `main.py` : menu principal.
- `db_init.py` : ajoute les données dans MongoDB.
- `game.py` : gère les combats.
- `models.py` : contient les classes des personnages et des monstres.
- `utils.py` : gère la connexion, les saisies et l'affichage.
