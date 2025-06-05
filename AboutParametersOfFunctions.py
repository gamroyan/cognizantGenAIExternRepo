# Assignment: About Parameters of Functions
# note that you'd need to comment out each task one at a time for
# them to work as needed

# Task 1 - Writing Functions
def greet_user(name):
    print("Hello, " + str(name) +"! Welcome aboard.")

def odd_numbers(num1, num2):
    sum = num1 + num2
    print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(sum))

# decided to have the user input the numbers rather than randomly choosing two
name = input("What's your name? ")
num1 = int(input("Give me a number: "))
num2 = int(input("Give me another number: "))

greet_user(name)
odd_numbers(num1, num2)


# Task 2 - Using Default Parameters
def define_pet(pet_name, animal_type):
    print("I have a " + animal_type + " named " + pet_name + ".")

define_pet("Frank", "cat")


# Task 3 - Functions with Variable Arguments
def make_sandwich(*ingredients):
    print("making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwich("Lettuce", "Tomato", "Cheese")


# Task 4 - Understanding Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print("The factorial of 5 is", factorial(5))
print("The factorial of 15 is", factorial(15))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fibonacci(n - 2) + fibonacci(n - 1)
    
print("The 6th Fibonacci number is", fibonacci(6))
print("The 15th Fibonacci number is", fibonacci(15))
