# Assignment: Exploring String Methods
# note that you'd need to comment out each task one at a time for
# them to work as needed

# Task 1 - String Slicing and Indexing
def stringSlicingAndIndexing():
    og_string = "Python is amazing!"
    first_word = og_string[0:6]
    amazing_part = og_string[10:17]
    reversed_string = og_string[::-1]

    print("First word: " + first_word)
    print("Amazing part: " + amazing_part)
    print("Reversed string: " + reversed_string)
    
stringSlicingAndIndexing()


# Task 2 - String Methods
def stringMethods():
    og_string = " hello, python world! "

    # since python strings are immutable, we can't directly edit og_string,
    # which is why I created a new string called result that I keep storing new values in
    result = og_string.strip()
    result = result.capitalize()
    result = result.replace("world", "universe")
    result = result.upper()

    print(result)

stringMethods()


# Task 3 - Check for Palindromes
def palindromeChecker():
    string = input("Enter a word: ")
    string_reversed = string[::-1]

    if (string == string_reversed):
        print("Yes, '" + string + "' is a palindrome!") 
    else:
        print("Sorry, '" + string + "' is not a palindrome!")
    
    return

palindromeChecker()