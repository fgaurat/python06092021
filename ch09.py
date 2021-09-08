from typing import SupportsFloat
from Rectangle import Rectangle


def main():
    r =Rectangle(12,2)
    print(r._longueur,r._largeur)
    surface = r.get_surface() # 24
    print(surface)
    longueur = r.get_longueur() # 12
    print(longueur)
    largeur = r.get_largeur() # 2
    print(largeur)
    sr = str(r)
    print(r)


if __name__ == '__main__':
    main()