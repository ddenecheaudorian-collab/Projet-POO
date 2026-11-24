from abc import ABC, abstractmethod
from Effets_Cartes import Effets
import numpy.random as npr
        
class Carte(ABC):

    _effets = {
        
            "Champs de Blé": Effets.champs_de_ble,
            "Ferme": Effets.ferme,
            "Boulangerie": Effets.boulangerie,
            "Café": Effets.cafe,
            "Supérette": Effets.superette,
            "Forêt": Effets.foret,
            "Fromagerie": Effets.fromagerie,
            "Fabrique de meubles": Effets.fabrique_de_meubles,
            "Mine": Effets.mine,
            "Restaurant": Effets.restaurant,
            "Verger": Effets.verger,
            "Marché de Fruits et Légumes": Effets.marche_fruit_legume,
            "Stade": Effets.stade,
            "Centre d'affaires": Effets.centre_affaire,
            "Chaîne de télévision": Effets.chaine_de_television,
            "Gare": Effets.gare,
            "Centre Commercial": Effets.centre_commercial,
            "Tour Radio": Effets.tour_radio,
            "Parc d'attractions": Effets.parc_attraction
        }

    _couts_construction = {
    
                "Champs de Blé": 1,
                "Ferme": 1,
                "Boulangerie": 1,
                "Café": 2,
                "Supérette": 2,
                "Forêt": 3,
                "Fromagerie": 5,
                "Fabrique de meubles": 3,
                "Mine": 6,
                "Restaurant": 3,
                "Verger": 3,
                "Marché de Fruits et Légumes": 2,
                "Stade": 6,
                "Centre d'affaires": 8,
                "Chaîne de télévision": 7,
                "Gare": 4,
                "Centre Commercial": 10,
                "Tour Radio": 22,
                "Parc d'attractions": 16
            }

    _types = {

            "Champs de Blé": "Agriculture",
            "Verger": "Agriculture",
            "Ferme": "Elevage",
            "Boulangerie": "Commerce",
            "Supérette": "Commerce",
            "Café": "Restauration",
            "Restaurant": "Restauration",
            "Forêt": "Naturel",
            "Mine": "Naturel",
            "Stade": "Complexe",
            "Centre d'affaires": "Complexe",
            "Chaîne de télévision": "Complexe",
            "Gare": "Monument",
            "Centre Commercial": "Monument",
            "Tour Radio": "Monument",
            "Parc d'attractions": "Monument"
        }
    
    def __init__(self, nom:str) -> None:
        self._nom = nom
        self._type:str = self._types.get(nom)
        self._cout_construction = self._couts_construction.get(nom)

    @property
    def nom(self):
        return self._nom
    @property
    def cout_construction(self):
        return self._cout_construction
    @property
    def type(self):
        return self._type

    @abstractmethod
    def effet_carte(self):
        pass
    
class Monument(Carte):
    _liste_monuments = ["Gare","Centre Commercial", "Tour Radio", "Parc d'attractions"]

    def __init__(self, nom:str) -> None:
        super().__init__(nom)
        self._type:str = self._types.get(nom)
        self._est_construit:bool = False

    @property
    def est_construit(self):
        return self._est_construit

    def construire(self):
        self._est_construit = True

    def effet_carte(self, joueur, partie):
            effet = self._effets.get(self._nom)
    
            if effet is not None:
                effet(joueur, partie)
    
class Etablissement(Carte):

    _rolls = {

        "Champs de Blé": [1],
        "Ferme": [2],
        "Boulangerie": [2, 3],
        "Café": [3],
        "Supérette": [4],
        "Forêt": [5],
        "Fromagerie": [7],
        "Fabrique de meubles": [8],
        "Mine": [9],
        "Restaurant": [9, 10],
        "Verger": [10],
        "Marché de Fruits et Légumes": [11, 12],
        "Stade": [6],
        "Centre d'affaires": [6],
        "Chaîne de télévision": [6]
    }


    def __init__(self, nom, varianteJoueur:bool = False):
        super().__init__(nom)
        self._roll:int = self._rolls.get(nom, [])
        if varianteJoueur:
            self._quantite = 0 if self._nom not in ["Champs de Blé","Boulangerie"] else 1
        else:
            self._quantite = 4 if self._type == "Complexe" else 6

    @property
    def roll(self):
        return self._roll
    @property
    def quantite(self):
        return self._quantite

    def effet_carte(self, roll, joueur, partie):
        effet = self._effets.get(self._nom)

        if effet is not None:
            effet(joueur, partie, roll)
    


