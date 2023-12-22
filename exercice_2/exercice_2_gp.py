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

##

# MVP
import random

def compare_numbers(a,b):
    if int(a) < 0 or int (a) > 100:
         return "Message d'erreur"
    elif int(a) == 0:
        return "Vincent Lagaf : Bienvenue au juste prix, vous avez 30 secondes pour deviner le prix de cet objet. Je vous donne un indice : Son prix est compris entre 1 et 100"
    elif int(a) == int(b):
        return "C'est gagné!"
    elif int(a) < int(b):
        return "C'est plus..."
    elif int(a) > int(b):
        return "C'est moins..."

random_computer_number = random.randint(1, 100)
# print(random_computer_number)
player_1_number = 0
print(compare_numbers(player_1_number, random_computer_number))

while player_1_number != random_computer_number:
        
        player_1_number = int(input())
        print(compare_numbers(player_1_number, random_computer_number))