# Project: Password Strength Checker

def passwordStrengthChecker():
    password = input("Enter a password: ")

    pass_length = False
    has_upper = False
    has_lower = False
    has_digit = False
    has_special_char = False

    # checking password length first
    if (len(password) >= 8):
        pass_length = True
    else: 
        print("Password should be at least 8 characters long")
        return

    # checking all of the criteria
    for char in password:
        if (char.isupper()):
            has_upper = True
        elif (char.islower()):
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in "@#$":
            has_special_char = True

    # messages for each missing case saved in array named "missing", to handle all possibilites
    missing = []
    if not has_upper:
        missing.append("an uppercase character")
    if not has_lower:
        missing.append("a lowercase character")
    if not has_digit:
        missing.append("a digit")
    if not has_special_char:
        missing.append("a special character")

    # printing final message
    if not missing:
        print("Your password is strong! 💪")
    else: 
        # if one criteria is missed
        if len(missing) == 1:
            missed = missing[0]
        else:
            # if more than one criteria is missed, join all but the last with commmas
            # then add "and" before the final one in the final message
            missed = ", ".join(missing[:-1]) + " and " + missing[-1]

    print("Your password is missing " + missed)

    return

passwordStrengthChecker()