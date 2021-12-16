bal = 340000
password = 6979
i = 1

while i>0:
    print("Welcome to SAITM bank!!! ")
    print("Choose anyone option: ")
    print("1.Withdraw Money")
    print("2.Update Password")
    print("3.Exit")
    opt = int(input("Enter your option: "))

    if opt == 1:
        print(f"Available Balance:{bal}")
      
        withdraw = int(input("How much money do you want to withdraw??: "))
        if withdraw <= 340000:
            print("Please collect your money")
            bal = bal - withdraw
        else:
            print("Insufficient Amount!!!")
        
       
        ques = input("Do you want to see your balance(y/n): ")
        
        if ques == "y" :
           print(bal)
        elif ques == "n":
            print("Have a Good Day!!!")
        

    elif opt == 2:
        a = int(input("Enter your current password:"))
        if a == password:
            new = int(input("Enter your new password: "))
            confirm = int(input("Re-confirm your password: "))
            password = confirm
            print(f"Your new updated password is {password} ")
        else:
            print("Invalid Password!!!")
                

    elif opt == 3 :
        print("Have a nice day!!!")
        break
         
        


    


