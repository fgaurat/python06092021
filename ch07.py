def main():
    name="GAURAT"
    first_name="Fred"

    say_hello_1 = "Hello "+name+" "+first_name
    say_hello_2 = "Hello {0} {1}".format(name,first_name)
    # s = r"c:\newdir" #raw
    say_hello_3 = f"Hello {name} {first_name}"
    print(say_hello_1)
    print(say_hello_2)
    print(say_hello_3)


if __name__ == '__main__':
    main()