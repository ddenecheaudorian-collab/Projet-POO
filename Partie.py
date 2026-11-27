from Cartes import *
from Effets_Cartes import Effets
from Banque import *
from Joueur import *
import numpy.random as npr

class De:
    def __init__(self):
        self._roll_mem:int = 0

    @property
    def roll_mem(self):
        return self._roll_mem
    @roll_mem.setter
    def roll_mem(self,nv):
        self._roll_mem = nv
    
    def roll(self):
        self._roll_mem = npr.randint(1,7)

class Partie:
    def __init__(self, liste_joueur):
        self._liste_joueur = liste_joueur
        self._banque:Banque = Banque(len(liste_joueur))
        self._De1:De = De()
        self._De2:De = De()
        self._joueur_actif:int = int(input(f"Quel joueur a visité un parc d'attractions le plus récemment ? {list(range(1,len(liste_joueur)+1))}"))-1
        self._reserve_etablissement = {

            "Café": Etablissement("Café"),
            "Stade": Etablissement("Stade"),
            "Chaîne de télévision": Etablissement("Chaîne de télévision"),
            "Restaurant": Etablissement("Restaurant"),
            "Champs de Blé": Etablissement("Champs de Blé"),
            "Ferme": Etablissement("Ferme"),
            "Boulangerie": Etablissement("Boulangerie"),
            "Supérette": Etablissement("Supérette"),
            "Forêt": Etablissement("Forêt"),
            "Fromagerie": Etablissement("Fromagerie"),
            "Fabrique de meubles": Etablissement("Fabrique de meubles"),
            "Mine": Etablissement("Mine"),
            "Verger": Etablissement("Verger"),
            "Marché de Fruits et Légumes": Etablissement("Marché de Fruits et Légumes"),
            "Centre d'affaires": Etablissement("Centre d'affaires"),
            "Gare" : Monument("Gare"),
            "Centre Commercial" : Monument("Centre Commercial"),
            "Tour Radio" : Monument("Tour Radio"),
            "Parc d'attractions" : Monument("Parc d'attractions")

        }



    @property
    def liste_joueur(self):
        return self._liste_joueur
    @property
    def banque(self):
        return self._banque
    @property
    def De1(self):
        return self._De1
    @property
    def De2(self):
        return self._De2
    @property
    def jouer_actif(self):
        return self._joueur_actif
    @property
    def reserve_etablissement(self):
        return self._reserve_etablissement


    
    def est_finie(self):
        for joueur in self._liste_joueur:
            temp = []
            for nom in joueur.liste_cartes:
                if joueur.liste_cartes[nom].type == "Monument":
                    temp.append(joueur.liste_cartes[nom])
            if all(monument._est_construit == True for monument in temp):
                return True, self._liste_joueur.index(joueur)+1
        return False,None

        

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
            carte_partie.detruire()
            return True
        else:
            raise ValueError(f"Le joueur ne peut pas construire la carte {nom_carte}")

    def echange(self, joueur1):

        carte1 = joueur1.liste_cartes[input(f"Choisissez une carte que vous vous voulez échanger : {[(joueur1.liste_cartes[c].nom, joueur1.liste_cartes[c].quantite) for c in joueur1.liste_cartes if joueur1.liste_cartes[c].type not in ["Complexe", "Monument"]]}")]
        joueur2 = self._liste_joueur[int(input(f"Choisissez le joueur avec lequel vous voulez échanger : {[i for i in range(len(self._liste_joueur)) if self._liste_joueur[i] is not joueur1]}"))]
        carte2 = joueur2.liste_cartes[input(f"Choisissez une carte du joueur avec qui vous échangez : {[(joueur2.liste_cartes[c].nom, joueur2.liste_cartes[c].quantite) for c in joueur2.liste_cartes if joueur2.liste_cartes[c].type not in ["Complexe", "Monument"]]}")]

        if carte1.type in ["Complexe","Monument"] or carte2.type in ["Complexe","Monument"]:
            raise ValueError(f"Impossible d'échanger les cartes {carte1.nom} et {carte2.nom}")

        carte1.detruire()
        carte2.detruire()

        joueur1.liste_cartes[carte2.nom].construire()
        joueur2.liste_cartes[carte1.nom].construire()


    def jouer(self):
        fin_partie = False
        while not fin_partie:
            if self._joueur_actif == 4:
                self._joueur_actif = 0
            self.deroulement_partie()
            self._De1.roll_mem,self._De2.roll_mem = 0,0
            fin_partie, gagnant = self.est_finie()

        print(f"Le joueur {gagnant+1} remporte la partie")
        for i in range(len(self._liste_joueur)):
            joueur = self._liste_joueur[i]
            print(f"Cartes du joueur {i+1} : {[(joueur.liste_cartes[c].nom, joueur.liste_cartes[c].quantite) for c in joueur.liste_cartes]}")


        
            

    def deroulement_partie(self):

        self._De1.roll()

        print(f"Argent de chaque joueur avant transactions : {[joueur.argent for joueur in self._liste_joueur]}")
        print(f"Résultat du lancer de dé : {self._De1.roll_mem}")

        joueur = self._liste_joueur[self._joueur_actif]
        self._joueur_actif += 1
        for nom in joueur.liste_cartes:
            carte = joueur.liste_cartes[nom]
            if carte.type == "Monument":
                carte.effet_carte(joueur , self, self._De1, self._De2)

        roll = self._De1.roll_mem + self._De2.roll_mem

        for nom in joueur.liste_cartes:
            carte = joueur.liste_cartes[nom]
            if carte.type != "Monument":
                carte.effet_carte(joueur , self, roll)

        print(f"Argent de chaque joueur après transactions : {[joueur.argent for joueur in self._liste_joueur]}")

        economiser = bool(input(f"Le joueur {self._joueur_actif} possède {joueur.argent[1]} pièces de 1, {joueur.argent[5]} pièces de 5 et {joueur.argent[10]} pièces de 10, pour un total de {joueur.total_argent}, doit-il économiser ?"))
        if economiser == True:
            pass
        else:
            construction_possible = []
            for nom in self._reserve_etablissement:
                carte_temp = self._reserve_etablissement[nom]
                if carte_temp.type == "Monument":
                    if joueur.liste_cartes[nom].est_construit == False:
                        construction_possible.append(carte_temp)
                elif carte_temp.quantite > 0:
                    construction_possible.append(carte_temp)
            for nom in joueur.liste_cartes:
                if joueur.liste_cartes[nom].type != "Monument":
                    if joueur.liste_cartes[nom].quantite > 0 and joueur.liste_cartes[nom].type == "Complexe":
                        for c in construction_possible:
                            if c.nom == nom:
                                construction_possible.remove(c)
            
            carte_a_construire = input(f"Voici la liste des bâtiments que le joueur {self._joueur_actif} peut construire : {[(c.nom,c.quantite) for c in construction_possible if c.type != "Monument"] + [(c.nom,c.est_construit) for c in construction_possible if c.type == "Monument"]} et la liste des cartes en sa posséssion : {[(joueur.liste_cartes[c].nom,joueur.liste_cartes[c].quantite) for c in joueur.liste_cartes if joueur.liste_cartes[c].type != "Monument"] + [(joueur.liste_cartes[c].nom,joueur.liste_cartes[c].est_construit) for c in joueur.liste_cartes if joueur.liste_cartes[c].type == "Monument"]}")
            print(f"Banque avant construction {self.banque.reserve}")
            self.construire(joueur,carte_a_construire)
            print(f"Banque après construction {self.banque.reserve}")


        
        

P = Partie([Joueur(),Joueur(),Joueur(),Joueur()])

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
"""
P._liste_joueur[0].liste_cartes["Verger"].quantite = 2
P._liste_joueur[2].liste_cartes["Mine"].quantite = 4


P.echange(P._liste_joueur[0])

print([(P._liste_joueur[0].liste_cartes[c].nom,P._liste_joueur[0].liste_cartes[c].quantite) for c in P._liste_joueur[0].liste_cartes if P._liste_joueur[0].liste_cartes[c].type != "Monument"])
print([(P._liste_joueur[2].liste_cartes[c].nom,P._liste_joueur[2].liste_cartes[c].quantite) for c in P._liste_joueur[2].liste_cartes if P._liste_joueur[2].liste_cartes[c].type != "Monument"])
print(P.est_finie())
"""

P.jouer()

