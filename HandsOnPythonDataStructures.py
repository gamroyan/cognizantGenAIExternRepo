# Assignment: Hands on Python Data Structures
# note that you'd need to comment out each task one at a time for
# them to work as needed

# Task 1 - Working with Lists
def fruitList():
    fruit_list = ['banana', 'kiwi', 'orange', 'strawberry', 'apple']
    print("Original list: " + str(fruit_list))

    fruit_list.append('blueberry')
    print("After adding a fruit: " + str(fruit_list))

    fruit_list.remove('apple')
    print("After removing a fruit: " + str(fruit_list))

    reversed = fruit_list[::-1]
    print("Reversed list: " + str(reversed))
    return

fruitList()


# Task 2 - Exploring Dictionaries
def exploringDictionaries():
    me = {"name": "Gayane", "age": 20, "city": "San Diego"}
    me["favorite color"] = "green"
    me["city"] = "La Jolla"
    key_list = []
    value_list = []

    for item in me:
        key_list.append(item)
        value_list.append(me[item])

    print("Keys: " + str(key_list))
    print("Values: " + str(value_list))
    return

exploringDictionaries()


# Task 3 - Using Tuples
def usingTuples():
    fav_things = ('Little Women', 'Walk in the Park', 'Everything I Know About Love')
    print("Favorite things: " + str(fav_things))
    # fav_things[2] = 'Circe'
    print("Oops! Tuples cannot be changed.")
    print("Length of Tuple: " + str(len(fav_things)))
    return

usingTuples()
