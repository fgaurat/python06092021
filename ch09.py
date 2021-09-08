from Carre import Carre
from typing import SupportsFloat
from Rectangle import Rectangle


def show_surface(o):
    print(o)
    # print(o.surface)

def main():
    c = Carre(cote=3)
    r = Rectangle(longueur = 2,largeur = 3)
    show_surface(c)
    show_surface(r)

    print(f"{c.surface=} {c.cote=}")
  # r = Rectangle(longueur = 2,largeur = 3)
    # r2 = Rectangle(longueur = 2,largeur = 3)
    # print(r._longueur,r._largeur)
    # surface = r.surface # 24
    # print(surface)
    # # r.set_longueur(56)
    # print(r.longueur)
    # r.longueur = 56

    # # longueur = r.get_longueur() # 12
    # # print(longueur)
    # # largeur = r.get_largeur() # 2
    # # print(largeur)
    # print(r)
    # print("Rectangle.cpt",Rectangle.get_cpt())


if __name__ == '__main__':
    main()