from Cartes_De import *
class Joueur:
    def __init__(self):
        self._argent = {

            1 : 3,
            5 : 0,
            10 : 0

        }
        self._liste_cartes = {

            "Champs de Blé": Etablissement("Champs de Blé",True),
            "Ferme": Etablissement("Ferme",True),
            "Boulangerie": Etablissement("Boulangerie",True),
            "Café": Etablissement("Café",True),
            "Supérette": Etablissement("Supérette",True),
            "Forêt": Etablissement("Forêt",True),
            "Fromagerie": Etablissement("Fromagerie",True),
            "Fabrique de meubles": Etablissement("Fabrique de meubles",True),
            "Mine": Etablissement("Mine",True),
            "Restaurant": Etablissement("Restaurant",True),
            "Verger": Etablissement("Verger",True),
            "Marché de Fruits et Légumes": Etablissement("Marché de Fruits et Légumes",True),
            "Stade": Etablissement("Stade",True),
            "Centre d'affaires": Etablissement("Centre d'affaires",True),
            "Chaîne de télévision": Etablissement("Chaîne de télévision",True),
            "Gare" : Monument("Gare"),
            "Centre Commercial" : Monument("Centre Commercial"),
            "Tour Radio" : Monument("Tour Radio"),
            "Parc d'attractions" : Monument("Parc d'attractions")

        }

    @property
    def liste_cartes(self):
        return self._liste_cartes
    @property
    def argent(self):
        return self._argent
    @argent.setter
    def argent(self,nv):
        self._argent = nv
    @property
    def total_argent(self):
        s = 0
        for valeur in [1,5,10]:
            s += valeur*self._argent[valeur]
        return s

    def construire(self, nom_etablissement:str):
        carte = self._liste_cartes[nom_etablissement]
        carte.construire()


    def transfert(self, joueur2, montant, partie):
        if self.total_argent <= montant:
            montant = self.total_argent
            
        if partie.banque.recevoir_argent(self, montant):
            partie.banque.donner_argent(joueur2, montant)
        else:
            return False
        return True




    