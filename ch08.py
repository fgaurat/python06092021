import sys

def division(a,b):
    return a/b


def call_division(a,b):
    return division(a,b)

def main():
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
    
    
    print("pas finally : après... erreurs ou pas d'erreurs")

if __name__ == '__main__':
    main()