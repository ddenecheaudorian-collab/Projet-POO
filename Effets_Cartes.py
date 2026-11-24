class Effets:

    @staticmethod
    def champs_de_ble(joueur,partie,roll):
        if roll==1
        for j in partie.liste_joueur:
            carte=next((c for c in j.batiment if c.nom="Champs de Blé")) #on regarde la liste des batiments du joueur et renvoie champs de ble
            donner_argent(j,carte.quantite)



    @staticmethod
    def ferme(joueur,partie,roll):
        if roll==2
        for j in partie.liste_joueur:
            carte=next((c for c in j.batiment if c.nom="Ferme"))
            donner_argent(j,carte.quantite)

    @staticmethod
    def boulangerie(joueur,partie,roll):
        if roll==2 or de.roll==3:
            carte=next((c for c in joueur.batiment if c.nom="Boulangerie"))
            donner_argent(joueur,carte.quantite)



    @staticmethod
    def cafe(joueur,partie,roll):
        if roll==3:
            for j in partie.liste_joueur:
                if j!=joueur:
                    carte=next((c for c in j.batiment if c.nom="Café"),None) #parcour la liste et si elle trouve café elle la stocke dans carte sinon renvoie None
                    if carte.quantite>0:
                            #joueur envoie decomposer(carte.quantite) à j

    @staticmethod
    def superette(joueur, partie,roll):
        if roll==4
            carte=next((c for c in joueur.batiment if c.nom="Supérette"))
            donner_argent(joueur,3*carte.quantite)

    @staticmethod
    def foret(joueur, partie,roll):
        if roll==5
        for j in partie.liste_joueur:
            carte=next((c for c in j.batiment if c.nom="Forêt"))
            donner_argent(j,carte.quantite)

    @staticmethod
    def centre_affaire(joueur, partie):
        pass

    @staticmethod
    def stade(joueur, partie,roll):
        if roll==6:
            carte=next((c for c in joueur.batiment if c.nom="Stade"))
            if carte.quantite>0:
                for j in partie.liste_joueur:
                    if j!=joueur:
                        # j donne 2 pièce à joueur
                
        

    @staticmethod
    def chaine_de_television(joueur, partie):
        pass

    @staticmethod
    def fromagerie(joueur, partie,roll):
        if roll==7:
            carte=next((c for c in joueur.batiment if c.nom="Fromagerie"))
            if carte.quantite>0:
                cartes_elevage=next((cartes_elevage.append(c) for c in joueur.batiment if c.type="Elevage"))
                S=0
                for u in carte_elevage:
                    S+=u.quantite     
        donner_argent(joueur,3*S)
                        

    @staticmethod
    def fabrique_de_meubles(joueur, partie,roll):
        if roll==8:
            carte=next((c for c in joueur.batiment if c.nom="Fabrique de meubles"))
            if carte.quantite>0:
                cartes_naturel=next((cartes_naturel.append(c) for c in joueur.batiment if c.type="Naturel"))
                S=0
                for u in carte_naturel:
                    S+=u.quantite     
        donner_argent(joueur,3*S)

    @staticmethod
    def mine(joueur, partie,roll):
        if roll==9
        for j in partie.liste_joueur:
            carte=next((c for c in j.batiment if c.nom="Mine"))
            donner_argent(j,5*carte.quantite)

    @staticmethod
    def restaurant(joueur, partie,roll):
        if roll==9 or roll==10:
            for j in partie.liste_joueur:
                if j!=joueur:
                    carte=next((c for c in j.batiment if c.nom="Restaurant"),None) #parcour la liste et si elle trouve café elle la stocke dans carte sinon renvoie None
                    if carte.quantite>0:
                            #joueur envoie decomposer(carte.quantite) à j


    @staticmethod
    def verger(joueur, partie,roll):
        if roll==10
        for j in partie.liste_joueur:
            carte=next((c for c in j.batiment if c.nom="Verger"))
            donner_argent(j,3*carte.quantite)

    @staticmethod
    def marche_fruit_legume(joueur, partie):
        if roll==11 or roll==12:
            carte=next((c for c in joueur.batiment if c.nom="Marché de Fruits et Légumes"))
            if carte.quantite>0:
                cartes_agriculture=next((cartes_agriculture.append(c) for c in joueur.batiment if c.type="Agriculture"))
                S=0
                for u in carte_agriculture:
                    S+=u.quantite     
        donner_argent(joueur,2*S)

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
