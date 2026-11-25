import numpy.random as npr
class Effets:

    @staticmethod
    def champs_de_ble(joueur,partie,roll):
        if roll==1:
            for j in partie.liste_joueur:
                carte=j.liste_cartes["Champs de Blé"]
                partie.banque.donner_argent(j,carte.quantite)

    @staticmethod
    def ferme(joueur,partie,roll):
        if roll==2:
            for j in partie.liste_joueur:
                carte=j.liste_cartes["Ferme"]
                partie.banque.donner_argent(j,carte.quantite)

    @staticmethod
    def boulangerie(joueur,partie,roll):
        if roll==2 or roll==3:
            carte=joueur.liste_cartes["Boulangerie"]
            partie.banque.donner_argent(joueur,carte.quantite)

    @staticmethod
    def cafe(joueur,partie,roll):
        if roll==3:
            for j in partie.liste_joueur:
                if j!=joueur:
                    carte=j.liste_cartes["Café"]
                    joueur.transfert(j,carte.quantite,partie)

    @staticmethod
    def superette(joueur, partie,roll):
        if roll==4:
                carte=joueur.liste_cartes["Supérette"]
                partie.banque.donner_argent(joueur,3*carte.quantite)

    @staticmethod
    def foret(joueur, partie,roll):
        if roll==5:
            for j in partie.liste_joueur:
                carte=j.liste_cartes["Forêt"]
                partie.banque.donner_argent(j,carte.quantite)

    @staticmethod
    def centre_affaire(joueur, partie,roll):
        if roll==6:
            carte=joueur.liste_cartes["Centre d'affaires"]
            if carte.quantite>0:
                partie.echange(joueur)

    @staticmethod
    def stade(joueur, partie,roll):
        if roll==6:
            carte=joueur.liste_cartes["Stade"]
            for j in partie.liste_joueur:
                if j!=joueur:
                    j.transfert(joueur,2*carte.quantite,partie)

    @staticmethod
    def chaine_de_television(joueur, partie,roll):
        if roll==6:
            carte=joueur.liste_cartes["Chaîne de télévision"]
            j = partie.liste_joueur[int(input(f"Choisissez un joueur pour qu'il vous donnent l'équivalent de 5 pièces : {[i for i in range(len(partie.liste_joueur)) if partie.liste_joueur[i] is not joueur]}"))]
            j.transfert(joueur,5*carte.quantite,partie)

    @staticmethod
    def fromagerie(joueur, partie,roll):
        if roll==7:
            carte=joueur.liste_cartes["Fromagerie"]
            cartes_elevage=[]
            for nom in joueur.liste_cartes:
                if joueur.liste_cartes[nom].type=="Elevage":
                    cartes_elevage.append(joueur.liste_cartes[nom])
            S=0
            for u in cartes_elevage:
                S+=u.quantite
            partie.banque.donner_argent(joueur,3*S*carte.quantite)
                        
    @staticmethod
    def fabrique_de_meubles(joueur, partie,roll):
        if roll==8:
            carte=joueur.liste_cartes["Fabrique de meubles"]
            cartes_naturel=[]
            for nom in joueur.liste_cartes:
                if joueur.liste_cartes[nom].type=="Naturel":
                    cartes_naturel.append(joueur.liste_cartes[nom])
            S=0
            for u in cartes_naturel:
                S+=u.quantite
            partie.banque.donner_argent(joueur,3*S*carte.quantite)

    @staticmethod
    def mine(joueur, partie,roll):
        if roll==9:
            for j in partie.liste_joueur:
                carte=j.liste_cartes["Mine"]
                partie.banque.donner_argent(j,5*carte.quantite)

    @staticmethod
    def restaurant(joueur, partie,roll):
        if roll==9 or roll==10:
            for j in partie.liste_joueur:
                if j!=joueur:
                    carte=j.liste_cartes["Restaurant"]
                    joueur.transfert(j,2*carte.quantite,partie)

    @staticmethod
    def verger(joueur, partie,roll):
        if roll==10:
            for j in partie.liste_joueur:
                carte=j.liste_cartes["Verger"]
                partie.banque.donner_argent(j,3*carte.quantite)

    @staticmethod
    def marche_fruit_legume(joueur, partie, roll):
        if roll==11 or roll==12:
            carte=joueur.liste_cartes["Marché de Fruits et Légumes"]
            cartes_agriculture=[]
            for nom in joueur.liste_cartes:
                if joueur.liste_cartes[nom].type=="Agriculture":
                    cartes_agriculture.append(joueur.liste_cartes[nom])
            S=0
            for u in cartes_agriculture:
                S+=u.quantite
            partie.banque.donner_argent(joueur,2*S*carte.quantite)

    @staticmethod
    def gare(joueur, partie):
        pass

    @staticmethod
    def centre_commercial(joueur, partie):
        pass

    @staticmethod
    def tour_radio(joueur, partie):
        pass
    
    @staticmethod
    def parc_attraction(joueur, partie):
        pass
