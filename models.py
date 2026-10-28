# Classes des personnages et des monstres
class Combattant:
    def __init__(self, nom, attaque, defense, points_de_vie):
        self.nom = nom
        self.atk = attaque
        self.defense = defense
        self.hp = points_de_vie
        self.hp_max = points_de_vie

    # Verifier si le combattant est vivant
    def est_vivant(self):
        return self.hp > 0

    def attaquer(self, cible):
        # Calculer les degats en fonction de la defense
        # Faire au moins 1 degat
        degats = self.atk - cible.defense
        if degats < 1:
            degats = 1
        cible.hp -= degats
        if cible.hp < 0:
            cible.hp = 0
        return degats

     # Afficher les informations du combattant
    def __str__(self):
        return f"{self.nom} - {self.atk} ATK - {self.defense} DEF - {self.hp} HP"

# Classe des personnages
class Personnage(Combattant):
    pass

# Classe des monstres
class Monstre(Combattant):
    pass