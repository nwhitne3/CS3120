    # imports
    # random number generator
    import random
    # system modules
    import sys
    # operating system stuff
    import os
     
    # Single line comment
     
    ''' Multi-line
    comments
    '''
     
    print("Hello World")
     
    '''variables
    A variable has to start with a letter.
    After can have letters or _ underscores.
     
    Data Types:
    Python has 5 main data types.
    1) Numbers
    2) Strings
    3) Lists
    4) Tuples
    5) Dictionaries
    '''
    print("Data Types:")
     
    # number
    print("Data Types: 1) Numbers")
    name = 15
    print(name)
     
    '''
    python has 7 different arithmetic operators:
    1) + addition
    2) - subtraction
    3) * multiplicatin
    4) / division
    5) % modulus
    6) ** exponential calculations
    7) // floor division (performs division then discards the remainder)
    '''
     
    print("Arithmetic:")
    print("Python has 7 different arithmetic operators:")
    print("5 + 2 =", 5+2, "Addition")
    print("5 - 2 =", 5-2, "Subtraction")
    print("5 * 2 =", 5*2, "Multiplication")
    print("5 / 2 =", 5/2, "Division")
    print("5 % 2 =", 5%2, "Modulo")
    print("5 ** 2 =", 5**2, "Exponential calculations")
    print("5 // 2 =", 5//2, "Floor division")
     
    #Python does not have ++
     
    #Order of operation precedence in python
    print("Order of operations preference")
    print("1 + 2 - 3 * 2 = 3 - 6 =", 1 + 2 - 3 * 2)
    print("(1 + 2 - 3) * 2 = 0 * 2 =", (1 + 2 - 3) * 2)
     
    # a string, single or double quotes is fine
    print("Data Types: 2) Strings")
    name = "Derek"
    print(name)
    name = 'Brenda'
    print(name)
     
    # escape characters
    quote = "\"Always remember you are unique\""
     
    # multi-line strings
    # Python's normal naming convention for variables is underscore_separation
    multi_line_quote = ''' just
    like everyone else'''
     
    # concatenation
    # join two strings together
    new_string = quote + multi_line_quote
     
    # print formatting
    # There are 2 types of strings
    print("%s %s %s" % ('I like the quote', quote, multi_line_quote))
     
    # printing without the automatic newline character
    print("These two lines do not have ", end="")
    print("newlines")
     
    # printing a multiple of newlines
    print("printing 5 new lines:")
    print('\n' * 5)
    print("End of 5 new lines")
     
    # printing the same thing 5 times
    print("\n Printing the same thing 5 times" * 5)
     
    # Data Types: 3) Lists
    print("Data Types: 3) Lists")
     
    # Lists can be mixed types. Don't have to all be strings.
    grocery_list = ['Juice', 'Tomatoes', 'Potatoes',
                    'Bananas']
     
    # Python indices start at 0. The first item is index 0, not one.
    print('First Item', grocery_list[0])
     
    # changing the value of that item using its index value
    grocery_list[0] = "Green Juice"
    print('First Item', grocery_list[0])
     
    # printing a subset of a list
    # This is a little strange, only prints Tomatoes and Potatoes.
    # Prints up to (not including) index 3
    print(grocery_list[1:3])
    print(grocery_list[1:4])
     
    # other things can be in a list, including lists of lists
    other_events = ['Wash Car', 'Pick Up Kids',
                    'Cash Check']
    print("other_events:\n", other_events)
     
    print("Other things can be in a list, inluding lists of lists:")
    to_do_list = [other_events, grocery_list]
    print("to_do_list:\n", to_do_list)
     
    # lists are basically boxes inside of boxes
    # The first 1 here represents the second grouping (grocery_list)
    # The second 1 here represents the second item within grocery_list (Tomatoes)
    print((to_do_list[1][1]))
     
    # appending items to lists
    print("Appending an item to the list grocery_list")
    grocery_list.append('Onions')
    print(to_do_list)
     
    print("inserting an item at the 2nd position in grocery_list")
    grocery_list.insert(1, "Pickle")
    print(grocery_list)
    print("removing it")
    # doesn't work:
    # grocery_list.remove(1)
    grocery_list.remove("Pickle")
    print(grocery_list)
     
    # List sorting
    print("List sorting:")
    grocery_list.sort()
    print(grocery_list)
     
    print("List reverse sorting:")
    grocery_list.reverse()
    print(grocery_list)
     
    print("List deleting the 5th item in grocery_list")
    del grocery_list[4]
    print(to_do_list)
     
    # Concatenating lists
    print("Concatenating Lists:")
     
    to_do_list2 = other_events + grocery_list
    print("to_do_list2 =", to_do_list2)
     
    # Length of lists
    print("Length of to_do_list2 =", len(to_do_list2))
     
    # Maximum of a list (in this case, what's highest alphabetically)
    print("Maximum of to_do_list2 =", max( to_do_list2))
     
    # Minimum of a list (in this case, what's lowest alphabetically
    print("Minimum of to_do_list2 =", min( to_do_list2))
     
    # Tuples
    print("Data Types: 5) Tuples")

