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
        if carte_partie.quantite == 0:
            raise ValueError(f"Il n'a plus de carte {nom_carte} dans la réserve")
        if carte_partie.type == "Complexe":
            if joueur.liste_cartes[nom_carte].quantite == 1:
                raise ValueError(f"Un joueur ne peut posséder qu'une seule carte {nom_carte}")
        if joueur.liste_cartes[nom_carte] == "Monument":
            if joueur.liste_cartes[nom_carte].est_construit == True:
                raise ValueError(f"Le joueur a déja construit le monument {nom_carte}")
        if self.banque.donner_argent(carte_partie.cout_construction, joueur.argent):
            joueur.construire(nom_carte)
        else:
            raise ValueError(f"Le joueur ne peut pas construire la carte {nom_carte}")

        
        
        
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

print(P.banque._reserve)
print(P.banque.recevoir_argent(P._liste_joueur[0],17))
print(P.banque._reserve)
#P._liste_joueur[0].transfert(P._liste_joueur[2],17,P)

#print(P._liste_joueur[0].argent)
#print(P._liste_joueur[2].argent)
