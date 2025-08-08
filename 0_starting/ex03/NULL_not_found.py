def NULL_not_found(object=any) -> int:
    if object is None:
        print("Nothing: None", type(object))
    elif object == 0 and isinstance(object, int):
        print("Zero: 0", type(object))
    elif object == '':
        print("Empty:", type(object))
    elif object is False:
        print("Fake: False", type(object))
    elif isinstance(object, float) and object != object:
        print("Cheese: nan", type(object))
    else:
        print("Type not found")
        return 1
    return 0
