import random

class Carte:
    def __init__(self, valeur, nom):
        self.valeur = valeur
        self.nom = nom
def pioche(carte) :
    carte = Carte(pioche[0].valeur, pioche[0].nom)
    del pioche[0]

Ezmo1 = Carte(1, "Ezmo")
Ezmo2 = Carte(1, "Ezmo")
Ezmo3 = Carte(1, "Ezmo")
Ezmo4 = Carte(1, "Ezmo")
Bob1 = Carte(2, "Bob")
Bob2 = Carte(2, "Bob")
Bob3 = Carte(2, "Bob")
Bob4 = Carte(2, "Bob")
Flies1 = Carte(3, "Giant flies")
Flies2 = Carte(3, "Giant flies")
Flies3 = Carte(3, "Giant flies")
Flies4 = Carte(3, "Giant flies")
Sharkonaut1 = Carte(4, "Sharkonaut")
Sharkonaut2 = Carte(4, "Sharkonaut")
Sharkonaut3 = Carte(4, "Sharkonaut")
Sharkonaut4 = Carte(4, "Sharkonaut")
Robots1 = Carte(5, "Robots")
Robots2 = Carte(5, "Robots")
Robots3 = Carte(5, "Robots")
Robots4 = Carte(5, "Robots")


pioche = [Ezmo1, Ezmo2, Ezmo3, Ezmo4, Bob1, Bob2, Bob3, Bob4, Flies1, Flies2, Flies3, Flies4,
          Sharkonaut1, Sharkonaut2, Sharkonaut3, Sharkonaut4, Robots1, Robots2, Robots3, Robots4]


scoreJ1 = 0
scoreJ2 = 0
scoreJ3 = 0
cartes = [CJ1HG,CJ2HG,CJ3HG,CJ1HD,CJ2HD,CJ3HD,CJ1BG,CJ2BG,CJ3BG,CJ1BD,CJ2BD,CJ3BD]
condJoueur50 = False

#Boucle de Partie
while not condJoueur50:

    random.shuffle(pioche)

    defausse = []
    for i in range(0, len(cartes)):
        pioche(cartes[i])



    defausse.append(Carte(pioche[0].valeur, pioche[0].nom))
    del pioche[0]

    cartesJ1 = [CJ1HG,CJ1HD, CJ1BG, CJ1BD]
    cartesJ2 = [CJ2HG,CJ2HD, CJ2BG, CJ2BD]
    cartesJ3 = [CJ3HG,CJ3HD, CJ3BG, CJ3BD]

    print("Main J1:", "\n",cartesJ1[0].valeur, cartesJ1[0].nom, cartesJ1[1].valeur, cartesJ1[1].nom,
          "\n",cartesJ1[2].valeur, cartesJ1[2].nom, cartesJ1[3].valeur, cartesJ1[3].nom, "\n")

    print("CarteHautDefausse :", defausse[0].valeur, defausse[0].nom)

    totalJ1 = cartesJ1[0].valeur + cartesJ1[1].valeur + cartesJ1[2].valeur + cartesJ1[3].valeur
    totalJ2 = cartesJ1[0].valeur + cartesJ1[1].valeur + cartesJ1[2].valeur + cartesJ1[3].valeur
    totalJ3 = cartesJ1[0].valeur + cartesJ1[1].valeur + cartesJ1[2].valeur + cartesJ1[3].valeur

    finManche = False
    dernierTourJ1 = False
    dernierTourJ2 = False
    dernierTourJ3 = False
    #Boucle de Manche
    while not finManche:

        if dernierTourJ1 == True:
            finManche = True
            break

        if len(pioche) == 0:
            for i in defausse[1:]:
                pioche.append(Carte(defausse[0].valeur, defausse[0].nom))
                del defausse[0]
            random.shuffle(pioche)

        choixJ1 = input("D = Defausser une carte, P = Piocher, E = Echanger : ")

        if choixJ1 == "D" or choixJ1 == "d":
            carteAdefausser = input("Quelle carte voulez-vous défausser ? 1, 2 3 ou 4 ?")
            if carteAdefausser == 1 and cartesJ1[0].valeur == defausse[0].valeur:
                cartesJ1[0] = Carte(0, "Vide")
            if carteAdefausser == 2 and cartesJ1[1].valeur == defausse[0].valeur:
                cartesJ1[1] = Carte(0, "Vide")
            if carteAdefausser == 3 and cartesJ1[2].valeur == defausse[0].valeur:
                cartesJ1[2] = Carte(0, "Vide")
            if carteAdefausser == 4 and cartesJ1[3].valeur == defausse[0].valeur:
                cartesJ1[3] = Carte(0, "Vide")

        if choixJ1 == "P" or choixJ1 == "p":

            print("La carte piochée :", pioche[0].valeur, pioche[0].nom)

            choixPJ1 = input("Voulez-vous l'échanger (E) ou la défausser (D) ? : ")

            if choixPJ1 == "E" or choixPJ1 == "e":
                carteEchange = input("Avec quelle carte ? 1, 2, 3, 4 : ")
                if carteEchange == 1:
                    #defausse.insert(0, Carte(cartesJ1[0].valeur, cartesJ1[0].nom))
                    cartesJ1[0] = Carte(pioche[0].valeur, pioche[0].nom)
                    del pioche[0]
                if carteEchange == 2:
                    #defausse.insert(0, Carte(cartesJ1[0].valeur, cartesJ1[0].nom))
                    cartesJ1[1] = Carte(pioche[0].valeur, pioche[0].nom)
                    del pioche[0]
                if carteEchange == 3:
                    #defausse.insert(0, Carte(cartesJ1[0].valeur, cartesJ1[0].nom))
                    cartesJ1[2] = Carte(pioche[0].valeur, pioche[0].nom)
                    del pioche[0]
                if carteEchange == 4:
                    #defausse.insert(0, Carte(cartesJ1[0].valeur, cartesJ1[0].nom))
                    cartesJ1[3] = Carte(pioche[0].valeur, pioche[0].nom)
                    del pioche[0]

        print("Main J1:", "\n", cartesJ1[0].valeur, cartesJ1[0].nom, cartesJ1[1].valeur, cartesJ1[1].nom,
            "\n", cartesJ1[2].valeur, cartesJ1[2].nom, cartesJ1[3].valeur, cartesJ1[3].nom, "\n")