def combinaison_pieces(montant, pieces):
        """
        combinaison_pieces prend en argument un montant d'argent, et un dictionnaire de pieces de 1, 5 et 10, et renvoie une 
        combinaison de pieces qui realise ce montant sans modifier le dictionnaire, si aucune combinaison n'est trouvee, renvoie None
        """
        for p10 in range(min(pieces[10], montant // 10), -1, -1):
            """
            On compare le nombre de pieces de 10 dans le dictionnaire et le nombre de pieces de 10 maximum que l'on peut utiliser pour realiser le montant
            On utilise le range pour tester differentes combinaisons
            """ 
            reste = montant - 10 * p10

            for p5 in range(min(pieces[5], reste // 5), -1, -1): # Meme chose que pour les pieces de 10

                reste_final = reste - 5 * p5

                if pieces[1] >= reste_final:
                    """
                    Si apres la decomposition en pieces de 10 et de 5 il y a suffisement de pieces de 1 dans le dictionnaire 
                    pour realiser le montant, renvoie la combinaison, sinon on teste d'autres combinaisons de pieces de 10 et 5
                    """
                    return {
                        1: reste_final,
                        5: p5,
                        10: p10
                    }

        return None

def trouver_paiement(montant, pieces_joueur, reserve):

    """
    trouver_paiement prend en argument un montant de pieces qu'un joueur veut envoyer a la banque (exemple : construire une etablissement)
    Un dictionnaire pieces_joueur, qui correspond a l'argent en pieces que le joueur possede et reserve le dictionnaire qui repertorie les
    pieces de la banque

    Cette fonction permet de trouver toutes les combinaisons de pieces que le joueur peut faire et qui permettent de payer le montant,
    ces combinaisons peuvent donner un resultat superieur a montant, dans ce cas la banque fait la monnaie et rend au joueur ce qu'il a paye en trop
    """

    combinaisons = []
    """
    Ici on cherche toutes les combinaisons qui permettent au joueur de payer le montant, meme si elles le depasse et on stocke toutes ces 
    combinaisons sous forme de dictionnaire dans une liste, exemple : montant = 12, on peut avoir des combinaisons avec comme total 12,13,17,...
    """
    for p10 in range(pieces_joueur[10] + 1):
        for p5 in range(pieces_joueur[5] + 1):
            for p1 in range(pieces_joueur[1] + 1):

                valeur = 10 * p10 + 5 * p5 + p1

                if valeur >= montant:
                    combinaisons.append({
                        1: p1,
                        5: p5,
                        10: p10
                    })
    """
    Ici on trie la liste des combinaisons pour les ranger dans l'ordre suivant :
    Si montant = 12, et [c1,c2,c3] = [17,12,13] le total d'argent des combinaisons 1,2,3
    Alors la liste triee devient [c2,c3,c1] = [12,13,17], on trie en fait les combinaisons dans l'ordre croissant
    par rapport a la difference entre le montant a payer et l'argent total des combinaisons
    """
    combinaisons.sort(key=lambda p: (10 * p[10] + 5 * p[5] + p[1] - montant))

    for paiement in combinaisons:
        valeur_paiement = (paiement[1] + 5 * paiement[5] + 10 * paiement[10])

        monnaie_a_rendre = valeur_paiement - montant # On calcule combien la banque doit rendre au joueur

        reserve_temp = { # On simule ici la reception des pieces du joueur par la banque, dans une variable temporaire
            1: reserve[1] + paiement[1],
            5: reserve[5] + paiement[5],
            10: reserve[10] + paiement[10]
        }

        monnaie = combinaison_pieces(monnaie_a_rendre, reserve_temp) # On verifie que apres reception des pieces du joueur, la banque peut rendre ce que le joueur a paye en trop

        if monnaie is not None:
            """
            Si oui, on renvoie paiement, un dictionnaire qui contient les pieces que le joueur envoie a la banque
            et monnaie, un dictionnaire qui contient les pieces que le joueur a paye en trop et que la banque lui envoie
            Si non, on test une autre combinaison
            """
            return paiement, monnaie

    return None # Si aucune combinaison ne permet d'atteindre le montant ou superieur, ou si la banque ne peut faire la monnaie d'aucune combinaison, renvoie None


class Banque:
    def __init__(self, nbjoueur):
        self._reserve = {
            1 : 36 - 3*nbjoueur, # Chaque joueur recoit 3 pieces de 1 au debut de partie
            5 : 9,
            10 : 9
        }

    @property
    def reserve(self):
        return self._reserve
    
    def recevoir_argent(self, joueur, montant):

        if montant < 0:
            raise ValueError("Le montant doit être positif")

        if joueur.total_argent < montant:
            return False

        resultat = trouver_paiement(montant, joueur.argent, self._reserve)

        if resultat is None:
            return False

        paiement, monnaie = resultat

        for valeur in [1, 5, 10]:
            joueur.argent[valeur] -= paiement[valeur]
            self._reserve[valeur] += paiement[valeur]

        for valeur in [1, 5, 10]:
            self._reserve[valeur] -= monnaie[valeur]
            joueur.argent[valeur] += monnaie[valeur]

        return True

    def donner_argent(self, joueur, montant):

        if montant < 0:
            raise ValueError("Le montant doit être positif")

        pieces = combinaison_pieces(montant, self._reserve)

        if pieces is None:
            return False

        for valeur in [1, 5, 10]:
            self._reserve[valeur] -= pieces[valeur]
            joueur.argent[valeur] += pieces[valeur]

        return True
