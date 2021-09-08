


class Rectangle:
    """Rectangle class"""
    cpt = 0
    def __init__(self,*,longueur=0,largeur=0) -> None: # double under init , dunder init
        print("def __init__(self)")
        self._longueur=longueur # définition de la propriété longueur
        self._largeur=largeur # définition de la propriété largeur
        Rectangle.cpt+=1

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
