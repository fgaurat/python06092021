import sys
def main():
    try:
        a = int(input("Please enter a number: "))
        b=2
        c= b/a # < ici !
        print(c)
    except ZeroDivisionError as e:
        print("ZeroDivisionError",e)
    except Exception as e:
        print("Exception",e)


if __name__ == '__main__':
    main()