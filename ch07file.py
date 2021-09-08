def main():

    # f = open("lefichier.txt","w")

    # f.close()

    with open("lefichier.txt","w") as f:
        f.write("Bonjour\n")
        print("Bonjour",file=f)
        print(f.closed)
    print(f.closed)


if __name__ == '__main__':
    main()