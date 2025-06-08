# Project: Calculator with Exception Handling

# Notes:
# - If exception is raised, goes back to beginning of loop, asking for new user_input
# - Checks for valid initial input and valid input for the two numbers for calculation
# - Only breaks out of loop if user inputs "5"
# - Use of newline characters is for readability in the terminal

def main():
    print("Welcome to the Error-Free Calculator!")
    menu = (
        "\nChoose an operation:\n"
        "1. Addition\n"
        "2. Subtraction\n"
        "3. Multiplication\n"
        "4. Division\n"
        "5. Exit"
    )

    while True:
        print(menu)
        user_input = input(" > ")

        # checks for valid initial input - only integers from 1 to 5
        try: 
            choice = int(user_input)
            if choice < 1 or choice > 5:
                print("\nNumber out of range.")
                continue
        except ValueError:
            print("\nPlease enter an integer from 1 to 5.")
            continue
        
        if choice == 5:
            print("\nGoodbye!")
            break
        
        # handles addition
        # types of exceptions it should handle: ValueError
        elif choice == 1:
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")
            try: 
                added = float(num1) + float(num2)
            except ValueError: 
                print("\nPlease enter two valid numbers.")
            else:
                print(f"\n{num1} + {num2} = {added}")

        # handles subtraction
        # types of exceptions it should handle: ValueError
        elif choice == 2:
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")
            try:
                subtracted = float(num1) - float(num2)
            except ValueError:
                print("\nPlease enter two valid numbers.")
                continue
            else: 
                print(f"\n{num1} - {num2} = {subtracted}")
                continue

        # handles multiplication
        # types of exceptions it should handle: ValueError
        elif choice == 3:
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")
            try:
                multiplied = float(num1) * float(num2)
            except ValueError:
                print("\nPlease enter two valid numbers.")
                continue
            else:
                print(f"\n{num1} x {num2} = {multiplied}")
                continue
        
        # handles division
        # types of exceptions it should handle: ValueError, ZeroDivisionError
        elif choice == 4:
            num1 = input("Enter the first number: ")
            num2 = input("Enter the second number: ")
            try: 
                divided = float(num1) / float(num2)
            except ZeroDivisionError:
                print("\nOops! You can't divide by zero.")
                continue
            except ValueError:
                print("\nPlease enter two valid numbers.")
                continue
            else: 
                print(f"\n{num1} / {num2} = {divided}")
                continue

main()
    