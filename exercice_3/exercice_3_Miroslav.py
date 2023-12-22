"""
Exercice 3 : les plus grands nombres
Générer une liste aléatoire de 100 entiers puis en extraire les 10 plus grands.
Généraliser votre algorithme en créant une fonction prenant comme paramètres la taille
de la liste initiale et le nombre d’entiers à extraire.
Contrainte : ne pas utiliser les fonctions de tri sort() ou sorted(). Vous
pouvez toutefois utiliser ces fonctions dans un second temps pour vérifier vos résultats.
"""
"""
from random import *


def nombres_aleatoire():
    liste_de_nombre = []
    for i in range(1, 101):
        x = randint(1,100)
        liste_de_nombre.append(x)
    return liste_de_nombre


def plus_grand_nombre(list_nb):
    liste_de_nombre = list_nb
    liste_plus_grand_nombres = []
    nombre_plus_grand = liste_de_nombre[0]
    for x in range(1, 11):
        resultat = max(liste_de_nombre)
        liste_plus_grand_nombres.append(resultat)
        liste_de_nombre.remove(resultat)
    print(liste_de_nombre)
    print(liste_plus_grand_nombres)


liste_de_nombre = nombres_aleatoire()
plus_grand_nombre(liste_de_nombre)
"""

from random import *

def limite_nombre():
    while True:
        limite_str = input("Quel est la limite de nombre à trier ?")
        try:
            limite_int = int(limite_str)
            return limite_int
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre.")    

def nombres_aleatoire(maxi):
    liste_de_nombre = []
    for i in range(1, int(maxi)+1):
        x = randint(1,int(maxi))
        liste_de_nombre.append(x)
    return liste_de_nombre


def rangement_liste(list_nb):
    for index in range(0, len(list_nb)):
        min = list_nb[index]
        min_index = index
        for i in range(index+1, len(list_nb)):
            if list_nb[i] < min:
                min = list_nb[i]
                min_index = i
        list_nb[min_index] = list_nb[index]
        list_nb[index] = min
    return list_nb


def nombre_plus_grand(liste_rangee):
    liste_plus_grand_nombres = []
    liste_plus_grand_nombres.append(liste_rangee[90:])
    for element in liste_rangee[-10:-1]:
        liste_rangee.pop()
    print(liste_rangee)
    print(liste_plus_grand_nombres)
    

limite = limite_nombre()
liste_de_nombre = nombres_aleatoire(limite)
liste_rangee = rangement_liste(liste_de_nombre)
nombre_plus_grand(liste_rangee)