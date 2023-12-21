"""
Exercice 1 : les impairs
Écrire une fonction qui prend 2 nombres en paramètres, et qui affiche, dans l'ordre
croissant, tous les entiers impairs se trouvant entre ces deux nombres. Vous devez
afficher ces nombres, en les séparant uniquement d'un espace.
Exemple : fonction(42.75, 52.23) doit renvoyer 43 45 47 49 51
"""
"""
def fonction(nbun, nbdeux):
    liste = [round(nbun), round(nbdeux)]
    liste.sort()
    depart = liste[0]
    dernier = liste[-1]
    elements = abs(int(depart) - int(dernier))
    listedeux = [int(nbun), int(nbdeux)]
    for i in range(elements+1):
        if (depart % 2) == 0:
            depart += 1
        else:
            listedeux.append(int(depart))
            depart += 1
    listedeux.sort()
    print(listedeux)

fonction(10.74,24.44)

"""
def fonction(nbun, nbdeux):
    liste = [round(nbun), round(nbdeux)]
    liste.sort()
    depart = liste[0]
    resultat = ""
    for i in range(liste[0], liste[-1]):
        if (depart % 2) == 0:
            depart += 1
        else:
            resultat += str(depart) + " "
            depart += 1
    print(resultat)

fonction(55.74,24.44)
