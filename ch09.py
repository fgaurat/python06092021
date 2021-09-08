from typing import SupportsFloat
from Rectangle import Rectangle


def main():
    r =Rectangle(12,2)
    surface = r.get_surface() # 24
    longueur = r.get_longueur() # 12
    largeur = r.get_largeur() # 2
    print(surface)
    print(longueur)
    print(largeur)


if __name__ == '__main__':
    main()