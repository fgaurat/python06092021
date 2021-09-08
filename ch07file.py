def main():

    # f = open("lefichier.txt","w")

    # f.close()

    # mode a : append
    # mode w : write
    # mode r : read (default)
    # with open("lefichier.txt","a") as f:
    #     f.write("Bonjour\n")
    #     print("Bonjour",file=f)
    #     print(f.closed)
    # print(f.closed)

    # with open("lefichier.txt") as f:
    # with open("lefichier.txt","r") as f:
    #     # lines = f.readlines()
    #     # print(lines)
    #     for line in f:
    #         # print(line.strip())
    #         print(line,end="")


    users = [
        {"login":"admin","password":"12345"},
        {"login":"user1","password":"34989"},
        {"login":"user2","password":"345"},
        {"login":"user3","password":"123"},
    ]
    with open('users.csv','a') as f:
        for u in users:
            line = f"'{u['login']}';'{u['password']}'"
            print(line,file=f)

if __name__ == '__main__':
    main()