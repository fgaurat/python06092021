from Calc import Calc
import sys

def division(a,b):
    return a/b


def call_division(a,b):
    resultat=0
    try:
        resultat = division(a,b)
    except ZeroDivisionError as e:
        print("ZeroDivisionError dans call_division")# 1
        print("après ZeroDivisionError dans call_division")
        raise e
    finally:
        print("traitement intermédiaire")# 2
    
    return resultat

def main_1():
    try:
        b=0
        a = int(input("Please enter a number: "))
        c= call_division(b,a) # < ici !
        print(c)
    except ZeroDivisionError as e:
        print("ZeroDivisionError",e)
    except ValueError as e:
        print("ValueError",e)
    except Exception as e:
        print("Exception",e.__class__.__name__,e)
    else:
        print("après... si pas d'erreurs")
    finally:
        print("finally : après... erreurs ou pas d'erreurs")
    # print("pas finally : après... erreurs ou pas d'erreurs")



def main():
    try:

        c = Calc()
        r = c.division(12,0)
    except ZeroDivisionError as e:
        print("ZeroDivisionError !")
    except Exception as e:
        print("Exception")


if __name__ == '__main__':
    main()