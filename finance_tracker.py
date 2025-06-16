# Capstone Project: Personal Finance Tracker
# Simple command-line personal finance tracker that allows users to 
# log expenses, categorize them, and view summaries

print("Welcome to the Personal Finance Tracker!")

data = {}

def add_expense():
    try: 
        while True:
        # Checks if the desciption is a valid string
            item_description = input("Enter expense description: ").strip()
            if item_description:
                break
            print("Description can't be empty. Please enter a valid string.")
        
        while True:
        # Checks if the category is a valid string
            item_category = input("Enter category: ").strip()
            if item_category:
                break
            print("Category can't be empty. Please enter a valid string.")

        while True:
        # Checks for valid number for input
            amount_input = input("Enter amount: $").strip()
            try: 
                item_amount = float(amount_input)
                break
            except ValueError:
                print("Please enter a valid number for amount")

        expense = (item_description, item_amount)
    
        if item_category in data:
            data[item_category].append(expense)
        else:
            data[item_category] = [expense]

        print("Expense added successfully.")

    except Exception as e:
        print(f"Something went wrong: {e}")


def view_expenses(data):
    if not data:
        print("\nNo expenses recorded yet.")
        return

    # Loops over the category in dict, printing each item disc and amount
    for item_category, items in data.items():
        print(f"\nCategory: {item_category}")
        for item_description, item_amount in items:
            print(f" - {item_description}: ${item_amount}")


def view_summary(data):
    if not data:
        print("\nNo expenses recorded yet.")
        return
    
    # Loops over the category in dict, summing the amounts for each item
    for item_category, items in data.items():
        total = 0
        
        for _, item_amount in items: # "_," because we're accessing a tuple
            total += item_amount
            
        # Prints total for every category
        print(f"{item_category}: ${total}")


# Main function
# - prints out menu of options
# - ensures user input is valid
# - runs functions depending on user input
def main():
    menu = (
        "\nWhat would you like to do?\n"
        "1. Add Expense\n"
        "2. View all Expenses\n"
        "3. View Summary\n"
        "4. Exit"
    )

    while True: 
        print(menu)
        user_input = input(" > ")

        # Checks for valid user input
        try:
            choice = int(user_input)
            if choice < 1 or choice > 4:
                print("\nNumber out of range.")
                continue
        except ValueError:
            print("\nPlease enter an integer from 1 to 5.")
            continue
        
        if choice == 4:
            print("\nGoodbye!")
            break

        elif choice == 1:
            add_expense()
            continue

        elif choice == 2:
            view_expenses(data)
            continue

        elif choice == 3:
            view_summary(data)
            continue

main()