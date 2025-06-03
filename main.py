import random

def affichage_joueur (nickname):
    print(f"Joueurs presents dans la partie: {nickname} ")



def defis(list_defis):
    alea = random.choice(list_defis)
    print(alea)
    list_defis.remove(alea)

def choix_aleatoire_joueur(j):
    random_player = random.choice(j)
    j.remove(random_player)
    return random_player



"""------------------------PROGRAMME PRINCIPAL------------------------------------------------------"""
def nombre_joueur_et_demander_pseudo():
    list_defis = ["DGL", "Fix B", "Escargot", "Scream-Like", "Samouraï", "RUSH-MID", "SCOUTKNIVEZ", "No-Defuse",
                  "3-6 ou rien"]
    nbrjoueur_int = 1
    liste_pseudo = []
    while nbrjoueur_int < 2 or nbrjoueur_int > 5:
        nbrjoueur_str = input("Combien êtes vous à jouer ?(2 à 5 joueurs) :")
        try:
            nbrjoueur_int = int(nbrjoueur_str)
        except ValueError:
            print("Renseignez un nombre compris entre 2 et 5 !")
            continue
        if nbrjoueur_int < 2 or nbrjoueur_int > 5:
            print("2 joueurs minimum, 5 max.")
            continue


    for i in range(nbrjoueur_int):
        reponse_p = input("Quel est votre pseudo ")
        liste_pseudo.append(reponse_p)
    affichage_joueur(liste_pseudo)

    while liste_pseudo:
        print("\nJoueur choisi :")
        joueur_choisi = choix_aleatoire_joueur(liste_pseudo)
        print(joueur_choisi)

        print("Ton défi :")
        defis(list_defis)

    print("\nTous les joueurs ont été choisis et leurs défis donnés.")



"""----------------------LANCEMENT DE LA FONCTION PRINCPALE-------------------------------"""


nombre_joueur_et_demander_pseudo()