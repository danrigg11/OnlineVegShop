items = {
    "Bananna":[3,20],
    "Orange":[5,10],
    "Apple":[5,20],
    "Grapes":[8,10],
    }
accountBalance = 20
while True:
    print("Bananna = £3 / Orange = £5 / Apple = £5 / Grapes = £8")
    print("Account Balance £",accountBalance)
    choice = input("What would you like to buy?: ").strip().title()
    if choice in items:
        if items[choice][1]>0:
            if accountBalance>=items[choice][0]:
                items[choice][1]=items[choice][1]-1
                accountBalance= accountBalance-items[choice][0]
                print("Thank you..!")
                print("")
            else:
                print("Sorry you dont enough money...")
                print("")
        else:
            print("sorry sold out")
            print("")
    else:
        print("Sorry we dont have that item...")
        print("")
