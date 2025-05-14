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