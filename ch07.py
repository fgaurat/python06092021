def main():
    name="GAURAT"
    first_name="Fred"

    say_hello_1 = "Hello "+name+" "+first_name
    say_hello_2 = "Hello {0} {1}".format(name,first_name)
    # s = r"c:\newdir" #raw
    say_hello_3 = f"Hello {name[0]} {first_name[0]}"
    print(say_hello_1)
    print(say_hello_2)
    print(say_hello_3)


    a= 1
    b= 3
    c = 0.339
    print(f"Valeur de c : {c:.2%}")


    h = "toto"
    # print(f"-{h:<10}-")
    # print(f"-{h:>10}-")
    print(f"-{h:10}-")

    h = "123"
    # print(f"-{h:<10}-")
    # print(f"-{h:>10}-")
    print(f"-{h:10}-")
    print("-{0:10}-".format(h))
    print("-{value_h:10}-".format(value_h=h))

    dict_info = {'name':"GAURAT",'first_name':"Fred"}
    print("Hello {name} {first_name}".format(name=dict_info['name'],first_name=dict_info['first_name']))
    print("Hello {name} {first_name}".format(**dict_info))

    i = 99.1
    print(f"{i:3.2f} €")


if __name__ == '__main__':
    main()