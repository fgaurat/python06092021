from ICalcMath import ICalcMath
import math


class Cercle(ICalcMath):

    def __init__(self,*,rayon=0) -> None:
        self._rayon = rayon

    @property
    def rayon(self):
        return self._rayon

    @rayon.setter
    def rayon(self,rayon):
        self._rayon = rayon
    
    @property
    def surface(self):
        return math.pi*self._rayon**2

