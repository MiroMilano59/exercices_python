"""
Exercice 2 : le jeu du plus ou moins
Coder le jeu suivant.
Pour commencer l'ordinateur va choisir au hasard un nombre compris entre 1 et 100.
L'utilisateur doit alors deviner ce nombre comme ceci :
L'utilisateur propose un nombre. L'ordinateur lui dit s'il est trop petit ou trop grand, et
ainsi de suite jusqu'à ce que l'utilisateur aie trouvé le bon nombre.
On pourra ajouter en options dans ce jeu les fonctionnalités suivantes :
• L'ordinateur affiche un message d'erreur si l'utilisateur propose un nombre
inférieur à 0 ou supérieur à 100.
• Vous pouvez choisir le niveau de difficulté (c’est-à-dire la taille de l’intervalle
possible)
• Vous pouvez inclure un mode multijoueur où un autre utilisateur entre le nombre
à deviner
• Vous pouvez ajouter une variable "compteur" qui fait en sorte de dire à
l'utilisateur en combien de coups il a réussi à découvrir le nombre (ex. : "Vous avez
trouvé le nombre en 5 coups")
• Vous pouvez ajouter un second compteur qui somme les scores de chaque partie
• Et enfin vous pouvez demander à l'utilisateur s'il veut refaire une partie ou pas
"""

from random import *

def nombrepc():
    nombre = randint(1,100)

def question():
    reponse = input("Quel est le nombre ?")
    return reponse

def tester_reponse(question()):
    while True:
        try:
            if 

tester_reponse(question())
print(nombre)