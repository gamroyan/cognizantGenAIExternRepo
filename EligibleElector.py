# Project: Eligible Elector
# Ask the user's age, then decides the eligibility based on that

def EligibleElector():
    age = int(input("How old are you? "))

    if age < 0:
        print("Don't lie!")
    elif age > 70:
        print("Uhh you haven't been voting this whole time? You're eligible!")
    elif age >= 18:
        print("Congratulations! You are eligible to vote. Go make a difference!")
    else:
        yrs = 18 - age
        print("Oops! You’re not eligible yet. But hey, only " + str(yrs) + " more years to go!")
    return

EligibleElector()