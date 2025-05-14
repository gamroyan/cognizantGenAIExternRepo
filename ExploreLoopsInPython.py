# Assignment: Explore Loops in Python
# note that you'd need to comment out each task one at a time for
# them to work as needed

# Task 1 - Counting Down with Loops
def countDown():
    num = int(input("Enter the starting number: "))
    while num > 0:
        print(num, end=" ")        
        num -= 1
    print("...Blast off!")
    return

countDown()


# Task 2 - Multiplication Table with for Loops
def multiplicationTable():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print (str(num) + " x " + str(i) + " =", num * i)
        i += 1
    return

multiplicationTable()

# Task 3 - Find the Factorial
def factorial():
    num = int(input("Enter a number: "))
    result = 1

    for i in range(1, num + 1):
        result *= i

    print("The factorial of " + str(num) + " is " + str(result))
    return 

factorial()