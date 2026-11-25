import numpy.randum as npr
class Effets:

    @staticmethod
    def champs_de_ble(joueur,partie,roll):
        if roll==1:
            for j in partie.liste_joueur:
                carte=next((j.liste_cartes[c] for c in j.liste_cartes if c=="Champs de Blé")) #on regarde la liste des liste_cartess du joueur et renvoie champs de ble
                partie.banque.donner_argent(j,carte.quantite)



    @staticmethod
    def ferme(joueur,partie,roll):
        if roll==2:
            for j in partie.liste_joueur:
                carte=next((j.liste_cartes[c] for c in j.liste_cartes if c=="Ferme"))
                partie.banque.donner_argent(j,carte.quantite)

    @staticmethod
    def boulangerie(joueur,partie,roll):
        if roll==2 or roll==3:
            carte=next((joueur.liste_cartes[c] for c in joueur.liste_cartes if c=="Boulangerie"))
            partie.banque.donner_argent(joueur,carte.quantite)



    @staticmethod
    def cafe(joueur,partie,roll):
        if roll==3:
            for j in partie.liste_joueur:
                if j!=joueur:
                    carte=next((j.liste_cartes[c] for c in j.liste_cartes if c=="Café")) #parcour la liste et si elle trouve café elle la stocke dans carte sinon renvoie None
                    joueur.transfert(j,carte.quantite,partie)

    @staticmethod
    def superette(joueur, partie,roll):
        if roll==4:
                carte=next((joueur.liste_cartes[c] for c in joueur.liste_cartes if c=="Supérette"))
                partie.banque.donner_argent(joueur,3*carte.quantite)

    @staticmethod
    def foret(joueur, partie,roll):
        if roll==5:
            for j in partie.liste_joueur:
                carte=next((j.liste_cartes[c] for c in j.liste_cartes if c=="Forêt"))
                partie.banque.donner_argent(j,carte.quantite)

    @staticmethod
    def centre_affaire(joueur, partie,roll):
        if roll==6:
            carte=next((joueur.liste_cartes[c] for c in joueur.liste_cartes if c=="Centre d'affaires'"))
            if carte.quantite>0:
                partie.echanger(joueur)


    @staticmethod
    def stade(joueur, partie,roll):
        if roll==6:
            carte=next((joueur.liste_cartes[c] for c in joueur.liste_cartes if c=="Stade"))
            for j in partie.liste_joueur:
                if j!=joueur:
                    j.transfert(joueur,2*carte.quantite,partie)

                
        

    @staticmethod
    def chaine_de_television(joueur, partie,roll):
        if roll==6:
            carte=next((joueur.liste_cartes[c] for c in joueur.liste_cartes if c=="Chaîne de télévision"))
            j = partie.liste_joueur[input(f"Choisissez le joueur de votre choix : {[i for i in range(len(partie.liste_joueur)) if partie.liste_joueur[i] is not joueur]}")]
            j.transfert(joueur,5*carte.quantite,partie)


    @staticmethod
    def fromagerie(joueur, partie,roll):
        if roll==7:
            carte=next((joueur.liste_cartes[c] for c in joueur.liste_cartes if c=="Fromagerie"))
            cartes_elevage=[]
            for nom in joueur.liste_cartes:
                if joueur.liste_cartes[nom].type=="Elevage":
                    cartes_elevage.append(joueur.liste_cartes[nom])
            S=0
            for u in cartes_elevage:
                S+=u.quantite
        partie.banque.donner_argent(joueur,3*S)
                        

    @staticmethod
    def fabrique_de_meubles(joueur, partie,roll):
        if roll==8:
            carte=next((joueur.liste_cartes[c] for c in joueur.liste_cartes if c=="Fabrique de meubles"))
            cartes_naturel=[]
            for nom in joueur.liste_cartes:
                if joueur.liste_cartes[nom].type=="Naturel":
                    cartes_naturel.append(joueur.liste_cartes[nom])
            S=0
            for u in cartes_naturel:
                S+=u.quantite
        partie.banque.donner_argent(joueur,3*S)

    @staticmethod
    def mine(joueur, partie,roll):
        if roll==9:
            for j in partie.liste_joueur:
                carte=next((j.liste_cartes[c] for c in j.liste_cartes if c=="Mine"))
                partie.banque.donner_argent(j,5*carte.quantite)

    @staticmethod
    def restaurant(joueur, partie,roll):
        if roll==9 or roll==10:
            for j in partie.liste_joueur:
                if j!=joueur:
                    carte=next((j.liste_cartes[c] for c in j.liste_cartes if c=="Restaurant"),None) #parcour la liste et si elle trouve café elle la stocke dans carte sinon renvoie None
                    joueur.transfert(j,2*carte.quantite,partie)



    @staticmethod
    def verger(joueur, partie,roll):
        if roll==10:
            for j in partie.liste_joueur:
                carte=next((j.liste_cartes[c] for c in j.liste_cartes if c=="Verger"))
                partie.banque.donner_argent(j,3*carte.quantite)

    @staticmethod
    def marche_fruit_legume(joueur, partie, roll):
        if roll==11 or roll==12:
            carte=next((joueur.liste_cartes[c] for c in joueur.liste_cartes if c=="Marché de Fruits et Légumes"))
            cartes_agriculture=[]
                for nom in joueur.liste_cartes:
                    if joueur.liste_cartes[nom].type=="Agrigulture":
                        cartes_naturel.append(joueur.liste_cartes[nom])
            S=0
            for u in cartes_agriculture:
                S+=u.quantite
        partie.banque.donner_argent(joueur,2*S)

    @staticmethod
    def gare(joueur, partie):
        pass

    @staticmethod
    def centre_commercial(joueur, partie):
        pass

    @staticmethod
    def tour_radio(joueur, partie):
        print("tour radiioo")

    @staticmethod
    def parc_attraction(joueur, partie):
        pass
