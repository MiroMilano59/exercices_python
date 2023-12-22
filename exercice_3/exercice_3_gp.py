# Exercice 3 : les plus grands nombres
# Générer une liste aléatoire de 100 entiers puis en extraire les 10 plus grands.
# Généraliser votre algorithme en créant une fonction prenant comme paramètres la taille
# de la liste initiale et le nombre d’entiers à extraire.
# Contrainte : ne pas utiliser les fonctions de tri sort() ou sorted(). Vous 
# pouvez toutefois utiliser ces fonctions dans un second temps pour vérifier vos résultats.

# On génère une liste aléatoire de 100 entiers

# Exercice python sans utiliser les fonctions sort() ou sorted.

# Créer une fonction list_of_x_random_int comprenant deux arguments pour générer une liste de x entiers aléatoires.
# Créer une fonction top_x comprenant deux arguments permettant de récupérer les x plus grands nombres d'une liste d'entiers.

# Contrainte : Ne pas utiliser les fonctions sort() ou sorted.

# Je voudrais uniquement utiliser les boucles for et importer random




import random

def list_of_x_random_integers(x, int_max):
    list = []
    for i in range(0, int(x)):
        n = random.randint(1, int(int_max))
        list.append(n)
    return list

def top_x(x, list):
    top_x = [0,0,0,0,0,0,0,0,0,0]
    # for n in range(0, x):
    #     # top_x.append(min(list))
    for i in list:
        for n in range(0, x):
            if int(i) > top_x[int(n)]:
                top_x[int(n)] = i
            else :
                True
    return top_x
            

print(list_of_x_random_integers(100,1000))
print(top_x(10, list_of_x_random_integers(100,1000)))

