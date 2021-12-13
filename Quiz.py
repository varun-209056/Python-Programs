print("Welcome to our Quiz")

n = input("Do you want to play the quiz?: ")
print("***************************************")
if n == "Yes" or n == "yes":
    print("Choose anyone Topic on the screen: ")
    print("1.Entertainment")
    print("2.Science")
    print("3.Sports")
    print("*************************")
    topic = int(input("The choosen topic is: "))

    if topic == 1:
        score = 0
        print("The Choosen topic is Entertainment!!!!")
        for i in range(0,5):
            if i == 0:
                print("Q1.Cannes Film Festival is held in which country?")
                print("A.Italy")
                print("B.France")
                print("C.Germany")
                print("D.England")

                opt = input("Choose anyone of the above options: ")
                print("***************************************")
                if opt == "B" or opt == "b":
                    print("Correct Answer")
                    print("Points Gained = +10")
                    print("***************************************")
                    score = score + 10
                else:
                    print("Wrong Answer")
                    print("Penalty = -10")
                    print("***************************************")
                    score = score - 10

            elif i == 1:

                print("Q2.Who among the following won the Oscar 2021 for 'Best Actor in a leading"\
                      " role?")
                print("A.Gary Oldman")
                print("B.Riz Ahmed")
                print("C.Anthony Hopkins")
                print("D.Chadwick Boseman")

                opt = input("Choose anyone of the above options: ")
                print("***************************************")
                if opt == "C" or opt == "c":
                    print("Correct Answer")
                    print("Points Gained = +10")
                    print("***************************************")
                    score = score + 10
                else:
                    print("Wrong Answer")
                    print("Penalty = -10")
                    print("***************************************")
                    score = score - 10

            elif i == 2:
                print("Q3.Which actor won the Best actor award at the 66th National Film Awards"\
                      "for 2018")
                print("A.Ayushmann Khurrana")
                print("B.Akshay Kumar")
                print("C.Amitabh Bachann")
                print("D.Riddhi Sen")

                opt = input("Choose anyone of the above options: ")
                print("***************************************")
                if opt == "A" or opt == "a":
                    print("Correct Answer")
                    print("points gained = +10")
                    print("***************************************")
                    score = score + 10
                else:
                    print("Wrong Answer")
                    print("Penalty = -10")
                    print("***************************************")
                    score = score - 10
            elif i == 3:
                print("Q4.Who was the director of 'Bahubali-2' which was released in the year 2017?")
                print("A.Rajkumar Hirani")
                print("B.Rajmouli")
                print("C.K. Vishwanath")
                print("D.Sanjay Leela Bansali")

                opt = input("Choose anyone of the above options: ")
                print("***************************************")
                if opt == "B" or opt == "b":
                    print("Correct Answer")
                    print("points gained = +10")
                    print("***************************************")
                    score = score + 10
                else:
                    print("Wrong Answer")
                    print("Penalty = -10")
                    print("***************************************")
                    score = score - 10

            elif i == 4:
                print("Q5.Which movie won the National award for the Best Film on social issues"\
                      "at the 64th National Film Awards,2017")
                print("A.Dangal")
                print("B.Pink")
                print("C.Sultan")
                print("D.Airlift")

                opt = input("Choose anyone of the above options: ")
                print("***************************************")
                if opt == "B" or opt == "b":
                    print("Correct Answer")
                    print("points gained = +10")
                    print("***************************************")
                    score = score + 10
                else:
                    print("Wrong Answer")
                    print("Penalty = -10")
                    print("***************************************")
                    score = score - 10

        if score>=10:
             print(f"Total Score: {score}")
             print("You Won")
             print("***************************************")
        else:
            print(f"Total Score: {score}")
            print("You Lose")
            print("***************************************")

    elif topic == 2:
        score = 0
        print("The choosen topic is Science!!!!")
        for i in range(0,5):
            if i == 0:
                print("Q1.Which Blood cells of the body are called 'Soldiers' of the body?")
                print("A.WBC")
                print("B.Platelets")
                print("C.RBC")
                print("D.All of the above")

                opt = input("Choose anyone of the above options: ")
                print("***************************************")
                if opt == "A" or opt == "a":
                    print("Correct Answer")
                    print("points gained = +10")
                    print("***************************************")
                    score = score + 10
                else:
                    print("Wrong Answer")
                    print("Penalty = -10")
                    print("***************************************")
                    score = score - 10

            elif i == 1:
                print("Q2.What is the chemical symbol for Oxygen?")
                print("A.On")
                print("B.Ox")
                print("C.O")
                print("D.N")

                opt = input("Choose anyone of the above options: ")
                print("***************************************")
                if opt == "C" or opt == "c":
                    print("Correct Answer")
                    print("points gained = +10")
                    print("***************************************")
                    score = score + 10
                else:
                    print("Wrong Answer")
                    print("Penalty = -10")
                    print("***************************************")
                    score = score - 10

            elif i == 2:
                print("Q3.Which of these elements is a non-metal?")
                print("A.Sulphur")
                print("B.Aluminium")
                print("C.Manganese")
                print("D.Iron")

                opt = input("Choose anyone of the above options: ")
                print("***************************************")
                if opt == "A" or opt == "a":
                    print("Correct Answer")
                    print("points gained = +10")
                    print("***************************************")
                    score = score + 10
                else:
                    print("Wrong Answer")
                    print("Penalty = -10")
                    print("***************************************")
                    score = score - 10

            elif i == 3:
                print("Q4.Which of the following travels at the fastest speed possible?")
                print("A.Space Ships")
                print("B.Asteroids")
                print("C.Light")
                print("D.Sound")

                opt = input("Choose anyone of the above options: ")
                print("***************************************")
                if opt == "C" or opt == "c":
                    print("Correct Answer")
                    print("points gained = +10")
                    print("***************************************")
                    score = score + 10
                else:
                    print("Wrong Answer")
                    print("Penalty = -10")
                    print("***************************************")
                    score = score - 10

            elif i == 4:
                print("Q5.Which of the following materials will be attached to a magnet?")
                print("A.Diamond")
                print("B.Iron")
                print("C.Plastics")
                print("D.Cotton")

                opt = input("Choose anyone of the above options: ")
                print("***************************************")
                if opt == "B" or opt == "b":
                    print("Correct Answer")
                    print("points gained = +10")
                    print("***************************************")
                    score = score + 10
                else:
                    print("Wrong Answer")
                    print("Penalty = -10")
                    print("***************************************")
                    score = score - 10

        if score>=10:
             print(f"Total Score: {score}")
             print("You Won")
             print("***************************************")
        else:
            print(f"Total Score: {score}")
            print("You Lose")
            print("***************************************")
    
    elif topic == 3:
         score = 0
         print("The choosen topic is Sports!!!!")
         for i in range(0,5):
            if i == 0:
                print("Q1.Who was the first Indian in independent India to have won a"\
                      "medal in an individual Olympic event ??")
                print("A.Dhyanchand")
                print("B.K D Jadhav")
                print("C.Prithipal Singh")
                print("D.Harishchandra Birajdar")

                opt = input("Choose anyone of the above options: ")
                print("***************************************")
                if opt == "B" or opt == "b":
                    print("Correct Answer")
                    print("points gained = +10")
                    print("***************************************")
                    score = score + 10
                else:
                    print("Wrong Answer")
                    print("Penalty = -10")
                    print("***************************************")
                    score = score - 10
    
            elif i == 1:
                print("Q2.Which Football Club was designated as the FIFA Club of \
                        the Century in 2000?")
                print("A.Manchestar United")
                print("B.Liverpool")
                print("C.Real Madrid")
                print("D.Arsenal")
    
                opt = input("Choose anyone of the above options: ")
                print("***************************************")
                if opt == "C" or opt == "c":
                    print("Correct Answer")
                    print("points gained = +10")
                    print("***************************************")
                    score = score + 10
                else:
                    print("Wrong Answer")
                    print("Penalty = -10")
                    print("***************************************")
                    score = score - 10

            elif i == 2:
                print("Q3.Which Commonwealth Games were hosted in India.?")
                print("A.2006")
                print("B.2002")
                print("C.2010")
                print("D.2014")

                opt = input("Choose anyone of the above options: ")
                print("***************************************")
                if opt == "C" or opt == "c":
                    print("Correct Answer")
                    print("points gained = +10")
                    print("***************************************")
                    score = score + 10
                else:
                    print("Wrong Answer")
                    print("Penalty = -10")
                    print("***************************************")
                    score = score - 10
    
            elif i == 3:
                print("Q4.Who is the only female athlete to win 6 Olympic gold medals?")
                print("A.Merlene Ottey")
                print("B.Allyson Felix")
                print("C.Marita Koch")
                print("D.Bobby Kersee")

                opt = input("Choose anyone of the above options: ")
                print("***************************************")
                if opt == "B" or opt == "b":
                    print("Correct Answer")
                    print("points gained = +10")
                    print("***************************************")
                    score = score + 10
                else:
                    print("Wrong Answer")
                    print("Penalty = -10")
                    print("***************************************")
                    score = score - 10

            elif i == 4:
                print("Q5.Where are the headquarters of World Chess Federation?")
                print("A.Switzerland")
                print("B.Russia")
                print("C.Greece")
                print("D.Turkey")
    
                opt = input("Choose anyone of the above options: ")
                print("***************************************")
                if opt == "C" or opt == "c":
                    print("Correct Answer")
                    print("points gained = +10")
                    print("***************************************")
                    score = score + 10
                else:
                    print("Wrong Answer")
                    print("Penalty = -10")
                    print("***************************************")
                    score = score - 10
    
         if score>=10:
                 print(f"Total Score: {score}")
                 print("You Won")
                 print("***************************************")
         else:
                print(f"Total Score: {score}")
                print("You Lose")
                print("***************************************")
else:
    print("Thank You For Coming!!!!")
    

                


            

            
                





























































    
    
