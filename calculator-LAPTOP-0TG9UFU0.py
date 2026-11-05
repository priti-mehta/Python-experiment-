print("----- Calculator -----")

while True:
    print("\n1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus")
    print("6.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 6:
        print("\nThank You for using Calculator")
        break

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    match choice:
        case 1:
            print("--------------------")
            print(f"Sum: {num1 + num2}")

        case 2:
            print("--------------------")
            print(f"Difference: {num1 - num2}")

        case 3:
            print("--------------------")
            print(f"Product: {num1 * num2}")

        case 4:
            print("--------------------")
            if num2 != 0:
                print(f"Division: {num1 / num2}")
            else:
                print("Error: Divisor cannot be zero")

        case 5:
            print("--------------------")
            if num2 != 0:
                print(f"Modulus: {num1 % num2}")
            else:
                print("Error: Divisor cannot be zero")

        case _:
            print("Invalid choice. Please try again.")1