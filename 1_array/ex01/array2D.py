def slice_me(family: list, start: int, end: int) -> list:
        # Vérification des types
    if not isinstance(family, list):
        raise TypeError("First argument must be a list")
    for row in family:
        if not isinstance(row, list):
            raise TypeError("Array must be a list of lists")
    
    # Vérification taille des lignes
    if len(family) == 0:
        raise ValueError("Array cannot be empty")
    row_length = len(family[0])
    for row in family:
        if len(row) != row_length:
            raise ValueError("All rows must have the same size")
    
    # Vérification des types des valeurs
    for row in family:
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError("All elements must be int or float")
    
    # Vérification des arguments de slice
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end must be integers")
    new_list = family[start:end]
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    print(f"My new shape is : ({len(new_list)}, {len(new_list[0])})")
    return new_list
