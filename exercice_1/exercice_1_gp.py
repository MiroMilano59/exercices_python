# Exercice 1 : les impairs
# Écrire une fonction qui prend 2 nombres en paramètres, et qui affiche, dans l'ordre
# croissant, tous les entiers impairs se trouvant entre ces deux nombres. Vous devez
# afficher ces nombres, en les séparant uniquement d'un espace.
# Exemple : fonction(42.75, 52.23) doit renvoyer 43 45 47 49 51

##

def les_impairs (a,b):
    liste = list(range(round(a), round(b)))
    liste_impairs = []
    for i in liste:
         if i % 2 != 0:
            liste_impairs.append(str(i))
         else:
             True
    return ' '.join(liste_impairs)

print(les_impairs(62.75, 52.23))