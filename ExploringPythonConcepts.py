# Assignment: Exploring Python Concepts
# Task 1 - Variables: Your First Python Intro

def Assignment1part1():
    name = "Gayane"
    age = 20
    height = 5.8

    result = ("Hi! My name is " + str(name) + ". " +
              str(age) + " years young, standing tall (" + str(height) + 
              " feet tall to be exact), and ready to take on this externship!" )

    return result

print(Assignment1part1())


# Assignment: Exploring Python Concepts
# Task 2 - Operators: Playing with Numbers

def Assignment1part2():
    num1 = 26 
    num2 = 3

    print("The sum of " + str(num1) + " and " + str(num2) + " is", num1 + num2)
    print("The difference of " + str(num1) + " and " + str(num2) + " is", num1 - num2)
    print("The product of " + str(num1) + " and " + str(num2) + " is", num1 * num2)
    print(str(num1) + " divided by " + str(num2) + " is", num1 / num2)

    return

Assignment1part2()


# Assignment: Exploring Python Concepts
# Task 3 - Conditional Statements: The Number Checker

def Assignment1part3():
    userinput = input("Input a number: ")
    num = int(userinput) # type cast input into integer

    if num > 0:
        print("This number is positive. Awesome!")
    elif num < 0:
        print("This number is negative. Better luck next time!")
    elif num == 0:
        print("Zero it is. A perfect balance!")

    return

Assignment1part3()