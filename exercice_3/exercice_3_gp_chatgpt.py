import random

def list_of_x_random_int(x, min_val=0, max_val=100):
    """
    Génère une liste de x entiers aléatoires dans la plage [min_val, max_val).
    """
    random_list = [random.randint(min_val, max_val - 1) for _ in range(x)]
    return random_list

def top_x(input_list, x):
    """
    Récupère les x plus grands nombres d'une liste d'entiers.
    """
    if x <= 0:
        return []

    top_x_list = []
    for _ in range(x):
        max_num = None
        for num in input_list:
            if max_num is None or num > max_num:
                max_num = num
        if max_num is not None:
            top_x_list.append(max_num)
            input_list.remove(max_num)

    return top_x_list

# Exemple d'utilisation :
random_numbers = list_of_x_random_int(10)
print("Liste générée aléatoirement :", random_numbers)

x_largest_numbers = top_x(random_numbers, 3)
print("Les 3 plus grands nombres :", x_largest_numbers)