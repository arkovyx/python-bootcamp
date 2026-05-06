def calc():
    try:
        i = True
        while i == True:
            print("===Welcome to πthon Calculator===")
            print("1. Sum")
            print("2. Difference")
            print("3. Product")
            print("4. Quotient")
            
            choice = input("Enter your choice(1-4)[q to quit]: ")

            invalid = ['w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'L', 'K', 'J', 'H', 'G', 'F', 'D', 'S', 'A', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

            valid = ['1', '2', '3', '4', 'q', 'Q']

            if choice in invalid:
                print("try again...")
                calc()

            if choice in valid:
                if choice == '1':
                    print("The sum is: ",num1 + num2)
                elif choice == '2':
                    print("The difference is: ",num1 - num2)
                elif choice == '3':
                    print("The product is: ",num1 * num2)
                elif choice == '4':
                    print("The Quotient is: ",num1/num2)
                elif choice == 'q':
                    print("Visit again!")
                    break
                elif choice == 'Q':
                    print("Visit again!")
                    break

            num1 = int(input("Enter your number: "))
            num2 = int(input("Enter your number: "))

    except ValueError:
        print("Please try again by entering a valid input...")
        calc()
    
    except KeyboardInterrupt:
        i == False

calc()
