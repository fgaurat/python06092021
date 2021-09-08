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
    users_from_file=[]
    with open('users.csv','w') as f:
        for u in users:
            line = f"'{u['login']}';'{u['password']}'"
            print(line,file=f)

    with open('users.csv','r') as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            user = line.split(";")
            # d = {"login":user[0][1:-1],"password":user[1][1:-1]}
            d = {"login":user[0].strip("'"),"password":user[1].strip("'")}
            users_from_file.append(d)
    
    print(users)
    print(users_from_file)


if __name__ == '__main__':
    main()