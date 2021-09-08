


class Rectangle:
    """Rectangle class"""

    def __init__(self,longueur,largeur) -> None: # double under init , dunder init
        print("def __init__(self)")
        self._longueur=longueur # définition de la propriété longueur
        self._largeur=largeur # définition de la propriété largeur

    def get_surface(self):
        return self._longueur*self._largeur

    def get_longueur(self):
        return self._longueur
    
    def set_longueur(self,longueur):
        self._longueur = longueur

    def get_largeur(self):
        return self._largeur
    
    def set_largeur(self,largeur):
        self._largeur = largeur

    def __str__(self) -> str:
        return f"{__class__} longueur : {self._longueur} largeur : {self._largeur}"
