"""
Exercice 5 : des conversions
Écrire un programme qui convertit un nombre entier de secondes fourni au départ, en un
nombre d'années, de mois, de jours, de minutes et de secondes.
Contraintes:
• Ne pas utiliser le package datetime
• Afficher le résultat sous la forme :
3430061596791935255 secondes correspondent à :
108 692 093 086 années 8 mois 1 jours
15 heures 51 minutes 28 secondes
Écrire un programme qui convertit en mètres par seconde et en km/h une vitesse fournie
par l'utilisateur en miles/heure (1 mile = 1609 mètres). Afficher le résultat avec
uniquement 2 chiffres après la virgule

"""

# temps = 3430061596791935255

# def calcul_temps(total):
#     temps = total
#     annee = 31536000
#     mois = 2629800
#     jour = 86400
#     heures = 3600
#     minute = 60
#     temps_restant = annee // temps
#     while True:
#         while temps > annee:
#             reste = temps // annee
#             print(reste)
#             while reste > mois:
#                 reste_deux = reste // mois
#                 print(reste_deux)
#                 while reste_deux > jour:
#                     reste_trois = reste_deux // jour
#                     print(reste_trois)
#                     while reste_trois > heures:
#                         reste_quatre = reste_trois // heures
#                         print(reste_quatre)
#                         while reste_quatre > minute:
#                             reste_cinq = reste_quatre // minute
#                             print(reste_cinq)
#                             break
#     print(f"{temps} secondes correspond à : /n {reste} années. /n {reste_deux} mois. /n {reste_trois} jours. /n {reste_quatre} heures. /n {reste_cinq} minutes.")
#     return reste_cinq

# calcul_temps(temps)

temps = 3430061596791935255

def calcul_temps(total):
    temps = total
    annee = 31536000
    mois = 2629800
    max_mois = mois * 12
    jour = 86400
    max_jour = jour * 30.4375
    heure = 3600
    max_heure = heure * 24
    minute = 60

    reste = temps // annee
    temps %= annee
    print(reste)

    reste_deux = reste // max_mois
    temps %= mois
    print(reste_deux)

    reste_trois = reste_deux // max_jour
    temps %= jour
    print(reste_trois)

    reste_quatre = reste_trois // max_heure
    temps %= heure
    print(reste_quatre)

    reste_cinq = reste_quatre // minute
    print(reste_cinq)

    print(f"{temps} secondes correspond à : \n {reste} années. \n {reste_deux} mois. \n {reste_trois} jours. \n {reste_quatre} heures. \n {reste_cinq} minutes.")
    return reste_cinq

calcul_temps(temps)