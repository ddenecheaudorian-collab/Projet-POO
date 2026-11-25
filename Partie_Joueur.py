from Cartes_De import *
from Effets_Cartes import Effets
from Banque import *
from Joueur import *

class Partie:
    def __init__(self, liste_joueur):
        self._liste_joueur = liste_joueur
        self._banque:Banque = Banque(len(liste_joueur))
        self._reserve_etablissement = {

            "Champs de Blé": Etablissement("Champs de Blé"),
            "Ferme": Etablissement("Ferme"),
            "Boulangerie": Etablissement("Boulangerie"),
            "Café": Etablissement("Café"),
            "Supérette": Etablissement("Supérette"),
            "Forêt": Etablissement("Forêt"),
            "Fromagerie": Etablissement("Fromagerie"),
            "Fabrique de meubles": Etablissement("Fabrique de meubles"),
            "Mine": Etablissement("Mine"),
            "Restaurant": Etablissement("Restaurant"),
            "Verger": Etablissement("Verger"),
            "Marché de Fruits et Légumes": Etablissement("Marché de Fruits et Légumes"),
            "Stade": Etablissement("Stade"),
            "Centre d'affaires": Etablissement("Centre d'affaires"),
            "Chaîne de télévision": Etablissement("Chaîne de télévision"),
            "Gare" : Monument("Gare"),
            "Centre Commercial" : Monument("Centre Commercial"),
            "Tour Radio" : Monument("Tour Radio"),
            "Parc d'attractions" : Monument("Parc d'attractions")

        }

        self._est_finie:bool = False


    @property
    def liste_joueur(self):
        return self._liste_joueur
    @property
    def banque(self):
        return self._banque
    @property
    def reserve_etablissement(self):
        return self._reserve_etablissement

        

    def construire(self, joueur, nom_carte:str):
        carte_partie = self._reserve_etablissement[nom_carte] 

        if carte_partie.type == "Monument":
            if joueur.liste_cartes[nom_carte].est_construit:
                raise ValueError(f"Le joueur a déja construit le monument {nom_carte}")
            else:
                if self.banque.recevoir_argent(joueur,carte_partie.cout_construction):
                    joueur.construire(nom_carte)
                    return True

        if carte_partie.quantite == 0:
            raise ValueError(f"Il n'a plus de carte {nom_carte} dans la réserve")
        
        if carte_partie.type == "Complexe":
            if joueur.liste_cartes[nom_carte].quantite == 1:
                raise ValueError(f"Un joueur ne peut posséder qu'une seule carte {nom_carte}")
 
        if self.banque.recevoir_argent(joueur,carte_partie.cout_construction):
            joueur.construire(nom_carte)
        else:
            raise ValueError(f"Le joueur ne peut pas construire la carte {nom_carte}")

    def echange(self, joueur1):

        carte1 = joueur1.liste_cartes[input(f"Choisissez une carte que vous vous voulez échanger : {[(joueur1.liste_cartes[c].nom, joueur1.liste_cartes[c].quantite) for c in joueur1.liste_cartes if joueur1.liste_cartes[c].type not in ["Complexe", "Monument"]]}")]
        joueur2 = self._liste_joueur[int(input(f"Choisissez le joueur avec lequel vous voulez échanger : {[i for i in range(len(self._liste_joueur)) if self._liste_joueur[i] is not joueur1]}"))]
        carte2 = joueur2.liste_cartes[input(f"Choisissez une carte du joueur avec qui vous échangez : {[(joueur2.liste_cartes[c].nom, joueur2.liste_cartes[c].quantite) for c in joueur2.liste_cartes if joueur2.liste_cartes[c].type not in ["Complexe", "Monument"]]}")]

        if carte1.type in ["Complexe","Monument"] or carte2.type in ["Complexe","Monument"]:
            raise ValueError(f"Impossible d'échanger les cartes {nom_carte1} et {nom_carte2}")

        carte1.detruire()
        carte2.detruire()

        joueur1.liste_cartes[carte2.nom].construire()
        joueur2.liste_cartes[carte1.nom].construire()


        
        
        
P = Partie([Joueur(),Joueur(),Joueur(),Joueur()])

P._liste_joueur[0].argent = {
    1 : 5,
    5 : 2,
    10 : 1
}

P._liste_joueur[2].argent = {
    1 : 11,
    5 : 0,
    10 : 2
}
"""
print(P._liste_joueur[0].argent)
print(P._liste_joueur[2].argent)
P._liste_joueur[0].transfert(P._liste_joueur[2],0,P)
print(P._liste_joueur[0].argent)
print(P._liste_joueur[2].argent)
"""
"""
print(P._liste_joueur[0].argent)
print(P._liste_joueur[2].argent)
"""
"""
print(P._liste_joueur[0].liste_cartes["Mine"].quantite)
P.construire(P._liste_joueur[0],"Mine")
print(P._liste_joueur[0].argent)
print(P._liste_joueur[0].liste_cartes["Mine"].quantite)
"""

P._liste_joueur[0].liste_cartes["Verger"].quantite = 2
P._liste_joueur[2].liste_cartes["Mine"].quantite = 4


P.echange(P._liste_joueur[0])

print([(P._liste_joueur[0].liste_cartes[c].nom,P._liste_joueur[0].liste_cartes[c].quantite) for c in P._liste_joueur[0].liste_cartes if P._liste_joueur[0].liste_cartes[c].type != "Monument"])
print([(P._liste_joueur[2].liste_cartes[c].nom,P._liste_joueur[2].liste_cartes[c].quantite) for c in P._liste_joueur[2].liste_cartes if P._liste_joueur[2].liste_cartes[c].type != "Monument"])
