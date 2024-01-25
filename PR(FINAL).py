# The function for adding new house to the database!
def add():
    hcode = input("Enter the Code of the House That you want to Register in System: ")
    f = open('house.txt', 'r')
    for line in f:
        cs = line.rstrip().split("-")
        if cs[0] == hcode:
            print("This House is already Exists in our DataBase !")
            f.close()
            return
        cs[2]=int(cs[2])
        if cs[2]<=0:
            print("The Meterage of the House Should be More than 0!!!")
            f.close()
        
            return
    f.close()

    address = input("Enter the Address of this House: ")
    meter = input("Enter the Meterage of the House: ")
    price = input("Enter the Price of the House: ")
    f = open('house.txt', 'a')
    f.write(hcode + '-')
    f.write(address + '-')
    f.write(meter + '-')
    f.write(price + '\n')
    f.close()


# The function for adding new person(buyer) to database!
def reg():
    ncode = input("Enter the National code of the person to Add: ")
    k = open('purchaser.txt', 'r')
    for line in k:
        cs= line.rstrip().split('-')
        if cs[0]==ncode:
            print("This person is Already in the DataBase!!!")
            k.close()
            return
    ncode = input("Enter the National Code of the person: ")
    name = input("Enter the Name of the person: ")
    lname = input("Enter the Last Name of the person: ")
    k = open('purchaser.txt', 'a')
    k.write(ncode+ '-')
    k.write(name+ '-')
    k.write(lname + '\n')
    k.close()

#Buying a new house use the national code of the person on the database!
    
def buy_new_hosue():

    ncode = int(input("Enter Your National Code: "))
    f = open('purchaser.txt', 'r')
    max= 0
    flg = 0
    for line in f:
        cs = line.rstrip().split('-')
        if int(cs[0]) == ncode:
            flg = 1
            max = int(input("Enter the Maximum Meter of The House You Are Searching for: "))
            break
    f.close() 

    if flg == 0:
        print("This National Code does not Exist in the Database!")
        return

    k = open('house.txt', 'r')
    for line in k:
        cs = line.rstrip().split('-')
        if int(cs[2]) <= max:
            print(f'{cs[0]}-{cs[1]}-{cs[2]}-{cs[3]}')
    k.close()

    selected_house_code = int(input('Enter the Code of the house which you selected: '))

    k = open('house.txt', 'r')
    tmp = open('tmp.txt', 'w')
    flg = 0
    for line in k:
        cs = line.rstrip().split('-')
        if int(cs[0]) == selected_house_code:
            flg = 1
            pass
        else:
            tmp.write(line)
    k.close()
    tmp.close()

    if flg == 0:
        print("Does not exist")
        return


    k = open('house.txt', 'w')
    tmp = open('tmp.txt', 'r')

    for line in tmp:
        k.write(line)
    
    tmp.close()
    k.close()



while True:
    print("1- ADD A NEW HOUSE")
    print("2- REGISTER NEW PERSON")
    print("3- BUY A NEW HOUSE")
    print("4- OTHER NUMBERS TO EXIT")
    op = int(input())

    if op==1:
        add()
    elif op==2:
        reg()
    elif op==3:
        buy_new_hosue()
    else:
        break
