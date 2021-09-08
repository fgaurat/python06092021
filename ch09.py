from typing import SupportsFloat
from Rectangle import Rectangle


def main():
    r =Rectangle(longueur = 2,largeur = 3)
    print(r._longueur,r._largeur)
    surface = r.get_surface() # 24
    print(surface)
    longueur = r.get_longueur() # 12
    print(longueur)
    largeur = r.get_largeur() # 2
    print(largeur)
    print(r)
    print("Rectangle.cpt",Rectangle.cpt)


if __name__ == '__main__':
    main()