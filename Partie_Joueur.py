from Cartes_De import *
from Effets_Cartes import Effets
from Banque import *

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

