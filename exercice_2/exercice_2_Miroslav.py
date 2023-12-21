# """
# Exercice 2 : le jeu du plus ou moins
# Coder le jeu suivant.
# Pour commencer l'ordinateur va choisir au hasard un nombre compris entre 1 et 100.
# L'utilisateur doit alors deviner ce nombre comme ceci :
# L'utilisateur propose un nombre. L'ordinateur lui dit s'il est trop petit ou trop grand, et
# ainsi de suite jusqu'à ce que l'utilisateur aie trouvé le bon nombre.
# On pourra ajouter en options dans ce jeu les fonctionnalités suivantes :
# • L'ordinateur affiche un message d'erreur si l'utilisateur propose un nombre
# inférieur à 0 ou supérieur à 100.
# • Vous pouvez choisir le niveau de difficulté (c’est-à-dire la taille de l’intervalle
# possible)
# • Vous pouvez inclure un mode multijoueur où un autre utilisateur entre le nombre
# à deviner
# • Vous pouvez ajouter une variable "compteur" qui fait en sorte de dire à
# l'utilisateur en combien de coups il a réussi à découvrir le nombre (ex. : "Vous avez
# trouvé le nombre en 5 coups")
# • Vous pouvez ajouter un second compteur qui somme les scores de chaque partie
# • Et enfin vous pouvez demander à l'utilisateur s'il veut refaire une partie ou pas
# """

from random import *


def nombrepc(maxi):
    nombre = randint(1,int(maxi))
    return nombre


def question(maxi, nombre_du_pc):
    maxi = maxi
    nombre_magique = nombre_du_pc
    vies = 3
    while vies > 0:
        reponse_str = input("Quel est le nombre magique ?")
        try:
            reponse_int = int(reponse_str)
            if not 1 <= reponse_int <= maxi:
                print(f"ERREUR: Vous devez rentrer un nombre entre 1 et str({maxi}).")
            else:
                if reponse_int < nombre_magique:
                    print(f"le nombre est plus grand... Il vous reste {vies} vies.")
                    vies -= 1
                    if vies == 0:
                        print("Vous avez perdu !")
                        rejouer = input("Tapez 1 si vous soulez rejouer !")
                        if rejouer == "1":
                            system()
                        else:
                            return 
                elif reponse_int > nombre_magique:
                    print("le nombre est plus petit... Il vous reste {vies} vies.")
                    vies -= 1
                    if vies == 0:
                        print("Vous avez perdu !")
                        rejouer = input("Tapez 1 si vous soulez rejouer !")
                        if rejouer == "1":
                            system()
                        else:
                            return 
                else:
                    print("Bravo ! Vous avez gagné !")
                    print("FIN DU JEU")
                    print()
                    rejouer = input("Tapez 1 si vous soulez rejouer !")
                    if rejouer == "1":
                        system()
                    else:
                        return 
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre.")
    

def niveau_jeu():
    nb_max_str = input("Le nombre inférieur du jeu étant de 1. Quel est le nombre supérieur souhaité ?")
    nb_max_int = int(nb_max_str)
    return nb_max_int


def mode_multi():
    print("Bienvenue dans le jeu, vous devez deviner un nombre entre 1 et la valeur définie !")
    print("Vous avez 3 chances/vies pour trouver le nombre magique.")
    print("1) Souhaitez-vous jouer en solo ?")
    print("2) Souhaitez-vous jouer à deux ?")
    reponse_multi_str = input("Veuillez entrer votre réponse entre 1 et 2 :")
    while True:
        try:
            reponse_multi_int = int(reponse_multi_str)
            if not 1 <= reponse_multi_int <= 2:
                print("ERREUR: Vous devez rentrer un nombre entre 1 et 2.")
            return reponse_multi_int
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre.")

def system():
    choix_joueur = mode_multi()
    nb_max = niveau_jeu()
    nombre_magique = nombrepc(nb_max)
    question(nb_max, nombre_magique)

system()


