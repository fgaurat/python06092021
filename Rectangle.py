


from ICalcMath import ICalcMath


class Rectangle(ICalcMath):
    """Rectangle class"""
    
    _cpt = 0
    
    def __init__(self,*,longueur=0,largeur=0) -> None: # double under init , dunder init
        print("def __init__(self)")
        self._longueur=longueur # définition de la propriété longueur
        self._largeur=largeur # définition de la propriété largeur
        Rectangle._cpt+=1

    @property
    def surface(self):
        return self._longueur*self._largeur

    @property
    def longueur(self):
        return self._longueur

    @longueur.setter
    def longueur(self,longueur):
        self._longueur = longueur

    @property
    def largeur(self):
        return self._largeur

    @largeur.setter
    def largeur(self,largeur):
        self._largeur = largeur

    def __str__(self) -> str:
        return f"{__class__.__name__} longueur : {self._longueur} largeur : {self._largeur}"
    
    
    def get_cpt():
        return Rectangle._cpt

