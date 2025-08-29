from abc import ABC, abstractmethod


class Character(ABC):
    """Class abstraite Character"""
    @abstractmethod
    def __init__(self, name, is_alive=True):
        """Initialise le nom et l'etat de vie de la classe abstraite"""
        self.name = name
        self.is_alive = is_alive

    def die(self):
        """Change l'etat de vie de la classe abstraite"""
        self.is_alive = False


class Stark(Character):
    """Class héritée de Character"""

    def __init__(self, name, is_alive=True):
        """Initialise le nom et l'etat de vie de la classe héritée"""
        super().__init__(name, is_alive)

    def die(self):
        """Change l'etat de vie de la classe héritée"""
        super().die()
