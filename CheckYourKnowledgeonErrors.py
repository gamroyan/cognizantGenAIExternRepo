# Assignment: Check your Knowledge on Errors
# note that you'd need to comment out each task one at a time for
# them to work as needed

# Task 1 - Understanding Python Exceptions
# handles specific exceptions
def understandingPythonExceptions():
    while True:
        num = input("Enter a number: ")

        try:
            number = float(num)
            result = 100 / number
        except ZeroDivisionError:
            print("Oops! You can't divide by zero")
            continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        else: 
            print("100 divided by " + str(num) + " is " + str(result))
            break

understandingPythonExceptions()


# Task 2 - Types of Exceptions
# intentionally raises and handles exceptions
def typesOfExceptions():
    # raises an IndexError when accessing an invalid list index
    try:
        list = [1, 2, 3]
        list[5]
    except IndexError:
        print("IndexError occurred! List index out of range.")

    # raises a KeyError when trying to access a non-existent key in dictionary
    try:
        dict = {"exceptions learned": 6, "excitement level": 10}
        dict["errors learned"]
    except KeyError:
        print("KeyError occurred! Key not found in dictionary.")

    # raises a TypeError when adding a string and integer
    try: 
        string = "Hello! I'm " + 20 + " years old."
    except TypeError:
        print("TypeError occurred! Unsupported operand types.")

typesOfExceptions()


# Task 3 - Using try...except...else...finally
def task3():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    try: 
        divided = float(num1) / float(num2)
    except ZeroDivisionError:
        print("Oops! You can't divide by zero")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    else: 
        print("The result is", divided)
    finally:
        print("This block always executes")

task3()