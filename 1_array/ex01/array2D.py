def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D list between two indexes and print its shapes
    before and after slicing.

    Args:
        array (list[list[int | float]]): The 2D array to slice.
                                         All rows must have the same length
                                         and contain only int or float.
        start (int): Starting index for the slice (inclusive).
        end (int): Ending index for the slice (exclusive).

    Raises:
        TypeError: If array is not a list of lists, or if start/end
        are not integers, or if elements are not int or float.
        ValueError: If array is empty or rows have different lengths.

    Returns:
        list[list[int | float]]: The sliced 2D list.

    Example:
        slice_me([[1, 2], [3, 4], [5, 6]], 0, 2)
        My shape is : (3, 2)
        My new shape is : (2, 2)
        [[1, 2], [3, 4]]
    """
    #   Vérification des types
    if not isinstance(family, list):
        raise TypeError("First argument must be a list")
    for row in family:
        if not isinstance(row, list):
            raise TypeError("Array must be a list of lists")
    #   Vérification taille des lignes
    if len(family) == 0:
        raise ValueError("Array cannot be empty")
    row_length = len(family[0])
    for row in family:
        if len(row) != row_length:
            raise ValueError("All rows must have the same size")
    #  Vérification des types des valeurs
    for row in family:
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError("All elements must be int or float")
    #  Vérification des arguments de slice
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end must be integers")
    new_list = family[start:end]
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    print(f"My new shape is : ({len(new_list)}, {len(new_list[0])})")
    return new_list
