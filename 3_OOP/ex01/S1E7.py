from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.first_name = first_name
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.first_name = first_name
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Méthode de classe pour créer une instance de Lannister"""
        return cls(first_name, is_alive)
