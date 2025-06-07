# Project: About Menu

def main():

    print("Welcome to the Recursive Artistry Program!")
    print("1. Calculate Factorial")
    print("2. Find Fibonacci")
    print("3. Exit")
    user_input = int(input("Choose an option: "))

    if user_input == 1:
        num = int(input("Enter a number to find its factorial: "))
        print("The factorial of " + str(num) + " is", factorial(num))
        
    elif user_input == 2:
        num = int(input("Enter the position of the Fibonacci number: "))
        print("The " + str(num) + "th Fibonacci number is", fibonacci(num))

    else:
        print("Thank you!")
        return
    
# user_input = 1
# recursive function to calculate the factorial of a number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# user_input = 2
# recursive function to calculate the nth Fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fibonacci(n - 2) + fibonacci(n - 1)
    
main()