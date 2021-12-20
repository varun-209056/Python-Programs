while True:
    print("Main Menu: ")
    print("1.Calculator")
    print("2.Area Finder")
    print("3.Volume Finder")
    print("4.Exit")
    opt = int(input("The choosen option is: "))
    print("*****************************************")

    if opt == 1:
        while True:
            print("Calculator")
            print("1.Add: + ")
            print("2.Multiply: * ")
            print("3.Divide: / ")
            print("4.Subtract: - ")
            opt_2 = int(input("Choose which operator you want to use: "))
            print("********************************************************")
                        
            if opt_2 == 1:
                 print("Addition:-")         
                 num1 = int(input("Enter any numeric value: "))
                 num2 = int(input("Enter any numeric value: "))
                 num3 = num1 + num2
                 print(f"{num1} + {num2} = {num3} ")
                 print("********************************************************")
                      
            
            elif opt_2 == 2:
                    print("Multiplication:-")
                    a = int(input("Enter any numeric value: "))
                    b = int(input("Enter any numeric value: "))
                    c = a * b
                    print(f"{a} * {b} = {c} ")
                    print("********************************************************")

            elif opt_2 == 3:
                    print("Division:- ")
                    a = int(input("Enter any numeric value: "))
                    b = int(input("Enter any numeric value: "))
                    c = a / b
                    print(f"{a} / {b} = {c}")
                    print("********************************************************")

            elif opt_2 == 4:
                    print("Subtraction:- ")
                    a = int(input("Enter any numeric value: "))
                    b = int(input("Enter any numeric value: "))
                    c = a - b
                    print(f"{a} - {b} = {c}")
                    print("********************************************************")

            choice = input("Do you want to return to main menu?(y/n): ")
            if choice == "y":
                    break
                    
            elif choice == "n":
                    continue
                    print("********************************************************")
                  
        
        

    if opt == 2:
        while True:
            print("Area Finder")
            print("1.Area Of Square")
            print("2.Area Of Rectangle")
            print("3.Area Of Triangle")
            print("4.Area Of Circle")
            opt_3 = int(input("Choose which area of shape you want to find:  "))
            print("********************************************************")

            if opt_3 == 1:
                print("Area Of Square")
                a = int(input("Enter the side of square: "))
                print(f"Area of the Square is {a**2}sq.cm")
                print("********************************************************")
                

            elif opt_3 == 2:
                print("Area Of Rectangle")
                l = int(input("Enter the length of the rectangle: "))
                b = int(input("Enter the breadth of the rectangle: "))
                print(f"Area of the Rectangle is {l*b}sq.cm")
                print("********************************************************")
                

            elif opt_3 == 3:
                print("Area Of Triangle")
                h = int(input("Enter the height of the triangle: "))
                b = int(input("Enter the base of the triangle: "))
                area_triangle = (0.5)*(b*h)
                print(f"The Area of triangle is {area_triangle}")
                print("********************************************************")

            

            elif opt_3 == 4:
                print("Area Of Circle")
                r = int(input("Enter the radius of the Circle: "))
                area_circle = (3.141592653589793)*(r**2)
                print(f"Area of the Circle is {area_circle}sq.cm")
                print("********************************************************")

            choice = input("Do you want to return to main menu?(y/n): ")
            if choice == "y":
                break
            elif choice == "n":
                continue
                print("********************************************************")
                
                
    if opt ==  3:
        while True:
            print("Volume Finder")
            print("1.Volume Of Sphere")
            print("2.Volume Of Cylinder")
            print("3.Volume Of cone")
            opt_4 = int(input("Choose which volume of shape you want to find: "))
            print("********************************************************")

            if opt_4 == 1:
                 print("Volume of Sphere")
                 r = int(input("Enter the radius of sphere: "))
                 volume_sphere = (4.0/3.0)*(3.141592653589793)*(r**3)
                 print(f"Volume of Sphere is {volume_sphere}")
                 print("********************************************************")

            elif opt_4 == 2:
                print("Volume Of Cylinder")
                r = int(input("Enter the radius of the cylinder: "))
                h = int(input("Enter the height of the cylinder: "))
                volume_cylinder = (3.141592653589793)*(r**2)*(h)
                print(f"Volume of Cylinder is {volume_cylinder}")
                print("********************************************************")
    
            elif opt_4 == 3:
                print("Volume Of Cone")
                r = int(input("Enter the radius of the cone: "))
                h = int(input("Enter the height of the cone: "))
                volume_cone = (3.141592653589793)*(r**2)*(h/3)
                print(f"Volume Of Cone is {volume_cone}")
                print("********************************************************")

            choice = input("Do you want to return to main menu?(y/n): ")
            if choice == "y":
                break                        
                
            elif choice == "n":
                continue
                print("********************************************************")

    elif opt == 4:
        print("Bye-Bye!!!")
        break
                 
            
        

         






















            
            
