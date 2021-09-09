import sys
def main():
    try:
        a = int(input("Please enter a number: "))
        b=2
        c= b/a # < ici !
        print(c)
    except ZeroDivisionError as e:
        # print("Erreur !ZeroDivisionError",file=sys.stderr)
        print("ZeroDivisionError",e)
    except Exception as e:
        # print("Erreur !ZeroDivisionError",file=sys.stderr)
        print("Exception",e)


if __name__ == '__main__':
    main()