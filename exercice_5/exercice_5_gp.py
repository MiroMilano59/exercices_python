# Exercice 5 : des conversions
# Écrire un programme qui convertit un nombre entier de secondes fourni au départ, en un
# nombre d'années, de mois, de jours, de minutes et de secondes.
# Contraintes:
# • Ne pas utiliser le package datetime
# • Afficher le résultat sous la forme :
# 3430061596791935255 secondes correspondent à :
# 108 692 093 086 années 8 mois 1 jours
# 15 heures 51 minutes 28 secondes

def convert_seconds(s):

    years = s / 60 / 60 / 24 / 365.25

    r_years = years - int(years)
    
    print(years)
    print(int(years))
    print(r_years)

    months = r_years * 12
    r_months = months - int(months)
    print(months)
    print(int(months))
    print(r_months)

    days = r_months * (365.25/ 12)
    r_days = days - int(days)
    print(int(days))
    print(r_days)

    hours = r_days * 24
    r_hours = hours - int(hours)
    print(int(hours))
    print(r_hours)

    minutes = r_hours * 60
    r_minutes = minutes - int(minutes)
    print(int(minutes))
    print(r_minutes)

    seconds = r_minutes * 60
    r_seconds = seconds - int(seconds)
    print(int(seconds))
    print(r_seconds)

    return f"{int(years)} années {int(months)} mois {int(days)} jours {int(hours)} heures {int(minutes)} minutes {int(seconds)} secondes"


print(convert_seconds(3430061596791935255))