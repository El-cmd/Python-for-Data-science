"""
Module: give_bmi
Contient deux fonctions :
- give_bmi : calcule l'IMC à partir de listes de tailles et poids
- apply_limit : compare les IMC à une limite donnée
"""


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
        ) -> list[int | float]:
    """
    Calcule l'IMC pour chaque paire (taille, poids).

    height: liste de tailles en mètres
    weight: liste de poids en kg
    return: liste des IMC
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("height and weight must be lists")
    if len(height) != len(weight):
        raise ValueError("height and weight lists must have the same length")
    for h in height:
        if not isinstance(h, (int, float)):
            raise TypeError("all height values must be int or float")
        if h <= 0:
            raise ValueError("height values must be positive")
    for w in weight:
        if not isinstance(w, (int, float)):
            raise TypeError("all weight values must be int or float")
        if w <= 0:
            raise ValueError("weight values must be positive")
    bmi = []
    for i in range(len(height)):
        bmi.append(weight[i] / (height[i] ** 2))
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Retourne True si l'IMC est au-dessus de limit, sinon False.

    bmi: liste des IMC
    limit: seuil
    """
    if not isinstance(bmi, list):
        raise TypeError("bmi must be a list")
    for val in bmi:
        if not isinstance(val, (int, float)):
            raise TypeError("all elements in bmi_list must be int or float")
    if not isinstance(limit, (int, float)):
        raise TypeError("limit must be an int or float")
    result = []
    for i in range(len(bmi)):
        if bmi[i] > limit:
            result.append(True)
        else:
            result.append(False)
    return result
