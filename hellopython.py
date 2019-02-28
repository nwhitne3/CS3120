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

# Tuples are similar to lists, but cannot be changed after they are created. (Immutable.)
print("Data Types: 4) Tuples")

'''
 One way could change a tuple is to copy it to a list, change the list, and
 then copy that list to a new tuple. But that is not ordinarily done.
'''

#Python does not like this because the lack of whitespace is not Pythonic.
# pi_tuple = (3,1,4,1,5,9)
pi_tuple = (3, 1, 4, 1, 5, 9)
print("pi_tuple =", pi_tuple)

# converting a tuple into a list
new_tuple = list(pi_tuple)
print("Converting a tuple into a list:")
print("new_tuple =", new_tuple)

# making some changes to the list, maybe
print("Making changes to that list by sorting it:")
new_tuple.sort()
print("new_tuple=", new_tuple)

# after hypothetical changes have been made to the list:
print("Turning that changed list into a new tuple:")
new_list = tuple(new_tuple)
print("new_list =", new_tuple)

# can get the length of a tuple
len(new_list)
print("The length of a tuple:")
print("len(new_list) =", len(new_list))
print("The minimum value in a tuple:")
print("min(new_list) =", min(new_list))
print("The maximum value in a tuple:")
print("max(new_list) =", max(new_list))

print("Data Types: 5) Dictionaries")
'''
Dictionaries are hash tables/hash maps, basically. Sometimes called Maps.
They are made up of values with a unique key for each key of the value
they are storing. Similar to lists, but, unlike lists, dictionaries cannot
be joined together using the + sign.
'''

'''
Creating a dictionary of supervillains:
Dictionaries use curly braces { }.
Each is a pair separated by a ":". First part is the supervillain name,
second part is the secret/actual identity.
'''

super_villains = {'Fiddler' : 'Isaac Bowin',
                  'Captain Cold' : 'Leonard Snart',
                  'Weather Wizard' : 'Mark Mardon',
                  'Mirror Master' : 'Sam Scudder',
                  'Pied Piper' : 'Thomas Peterson'}
print(super_villains)

# getting the secret identity for one of the super villains
# note that the lookup uses square brackets [ ]:
print("Captain Cold's secret identity =", super_villains['Captain Cold'])

# removing a pair from the dictionary
print("Removing Fiddler from the dictionary:")
del super_villains['Fiddler']
print(super_villains)

# replacing a pair in the dictionary
print("Changing the secret identity of Pied Piper:")
super_villains['Pied Piper'] = 'Hartley Rathaway'
print(super_villains)

# find the number of super_villians, using the length function:
print("Finding the number of super villains using the length function:")
print("len(super_villains) =", len(super_villains))

# .get() is rather commonly used
print("Getting the value by passing in a key:")
print("super_villains.get(\"Pied Piper\") =", super_villains.get("Pied Piper"))

print("Getting a list of super villain keys:")
print("super_villains.keys() =", super_villains.keys())

print("Getting a list of dictionary values:")
print("super_villains.values() =", super_villains.values())

# Conditionals: Execute the code if the condition is met
print("Conditionals:")
'''
if, else, and elif are used to perform different actions based on conditions
elif = else-if
conditionals include the standards:
==
!=
>
<
>=
<=
'''

# example:
age = 21
# Python will accept this with the extra space before the :, but it is not Pythonic
#if age > 16 :
# note the colon ":"
if age > 16:
    '''
    Note the required whitespace indentation. Can be whatever you want, but
    has to be consistent.
    '''
    print('You are old enough to drive.')
else:
    # again, single or double quotes is fine for prints
    print("You are not old enough to drive.")

# elif is for checking for multiple conditions
if age >= 21:
    print('You are old enough to drive a tractor trailer.')
elif age >= 16:
    print('You are old enough to drive a car.')
else:
    print('You are not old enough to drive.')

# Logical operators, matching multiple conditions
if ((age >= 1) and (age <= 18)):
    print("You get a birthday.")
elif ((age == 21) or (age >=65)):
    print("You get a birthday.")
# The NOT operator does the opposite of whatever is to the right of it.
# So if age is not 30 it will return FALSE.
elif not(age == 30):
    print("You don't get a birthday.")
else:
    print("You get a birtday party, yay.")

# Once a condition is met, no further conditions are checked.

# Looping
print("Looping:")

print("For loops:")
# works up to 10 but does not include 10
for x in range(0, 10):
    print(x, ' ', end="")

# printing a newline:
print('\n')

# changing the grocery list to match this part of the tutorial
print(grocery_list)
grocery_list[3] = 'Bananas'
print(grocery_list)

print("For Loop: looping through grocery_list")
for y in grocery_list:
    print("y =", y)

print("Defining a list of numbers to cycle through in a loop. "
      "Works pretty much like looping through an already-defined list.")
for x in [2, 4, 6, 8, 10]:
    print(x)

# a list inside of lists
num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 330]]

print("cycling through a list of lists with nested for loops:")
for x in range(0, 3):
    for y in range(0, 3):
        print("num_list[x][y] =", num_list[x][y])


print("While loops:")
'''
It is a good idea to use while loops when you have no idea ahead of time
how many times you will have to loop.
'''

#requires:
# import random
# using the random range function to generate random numbers from 0 to 99
random_num = random.randrange(0, 100)

# cycle through until get 15
print("Cycle through random numbers between 0 and 99 until get a 15:")
while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0, 100)
print(random_num)

print("Using a while loop more like a for loop:")
j = 0
while(j <= 20):
    # if the number is even it will have no remainder
    if(j % 2 == 0):
        print("The number is even:", j)
    elif(j ==9):
        #forcing out of the loop completely
        print("Demonstrating break:")
        break;
    else:
        #exactly the same as j = j + 1
        print("Incrementing j because j =", j, "is odd")
        j += 1
        # it's an odd number so continue
        continue
    j += 1

# Functions
'''
Functions allow you to reuse code.
Functions must be defined before they can be called.
'''

# first number + last number
def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum
print("addNumber(1, 4) =", addNumber(1, 4))

string = addNumber(1, 4)
print("It works with strings too: "
      "string = addNumber(1, 4) =", string)

#print("Demonstrating that sumNum is not available outside the function:"
#      "(Because it is out of scope.)")
# print(sumNum)

print("Getting input from the user:")
print('What is your name')

# name = sys.stdin.readline()

# print("Hello", name)

print("Strings - part 2:")
print("Printing out the first four characters of a string:")
long_string = "I'll catch you if you fall - The Floor"
print(long_string[0:4])
print("Printing out the last 5 characters of a string:")
print(long_string[-5:])

print("Printing all b ut the last 5 characters of a string:")
print(long_string[:-5])

print("Concatenating strings together using a substring:")
# error because of the brackets that crept in:
# print(long_string[:4] + [" be there"])
# TypeError: Can't convert 'list' object to str implicitly
print(long_string[:4] + " be there")

print("Formatting strings using the print command:")
'''
%c = character
%s = string
%d = integer
%5f = floating point number with at least 5 decimal places'''

# all inputs go on the second line of the print in this case:
print("%c is my %s letter and my number %d number is %.5f" %
      ('X', 'favorite', 1, .14))

print("Capitalizing the first letter of a string")
# note that 'Floor' is no longer capitalized. Interesting.
print(long_string.capitalize())

print("Returning the index value of a string, looking for the word 'Floor':")
print(long_string.find("Floor"))

print("Checking if a string is all alphabet characters:")
print(long_string.isalpha())

print("Checking if a string is all alphanumeric characters:")
print(long_string.isalnum())

print("Getting the length of a string:")
print(len(long_string))

print("Replacing a specific substring 'Floor' in a string with another word:")
print(long_string.replace("Floor", "Ground"))

# Not quite behaving like I expect, but ok
print("Removing whitespace from a string:")
long_string2 = " " + long_string + "     " + "1" + "  "
print(long_string2)
print(long_string2.strip())

print("Putting a string into a list, and specifying how the words should be "
      "separated:")
quote_list = long_string.split(" ")
print(quote_list)
# not behaving how I expect:
# quote_list = long_string.split(" | ")
# print(quote_list)

print("File I/O - part 2:")
print("Test writing a new file test.txt")
# the wb command specifies the file mode.
# wb = want to write the file
# ab+ = want to read AND append the file
test_file = open("test.txt", "wb")
print("If need to know what what mode you are in:")
print("test_file.mode =", test_file.mode)
print("If need to know the filename you specified:")
print("test_file.name =", test_file.name)
print("writing text to a screen or to a text file")
test_file.write(bytes("Write me to the file\n", 'UTF-8'))
print("Closing a file:")
test_file.close()

print("Reading information from a file:")

print("Reopening the file since closed it:")
# r+ = reading and writing mode
test_file = open("test.txt", "r+")
text_in_file = test_file.read()
print("Text in the file: \n", text_in_file)

# using the "os" module
print("Deleting the file:")
os.remove("test.txt")

# Objects
print("Python Objects:")
print("defining an Animal object using a class:")

'''
   Specifying values for the object.
_ name is optional
_ specifies private scope, however I think it is only a guideline and not
   enforced?
   To access or change those values inside the class, it must be done via
   functions inside that class.
'''
class Animal:
    # None specifies the lack of a value, like NULL in other languages
    # e.g. _name = None
    # e.g. "" , which is pretty much interchangeable with None
    _name = ""
    _height = 0
    _weight = 0
    _sound = 0

    '''
    A constructor within the class for setting up (initializing) an object,
    hence the name "__init__".
    In Python, a value called "self" must be explicitly passed in. Is sort of
    like "this.whatever" in Java but more explicit. It is a way to refer to an
    object--in this case to refer to an Animal object.
    Values passed into the constructor: a reference to itself, a name, a height,
    a weight, and a sound. All those values get initialized to their default
    values, which are specified above.
    '''
    def __init__(self, name, height, weight, sound):
        self._name = name
        self._height = height
        self._weight = weight
        self._sound = sound

    # creating a function within the class that can set the name
    def set_name(self, name):
        # the existing name _name is now changed to whatever name "name" the
        # call to set_name passed in
        self._name = name

    # creating a function within the class that  can get/access/return the name
    def get_name(self):
        # This is encapsulation. Lets verify that the existing "name"
        # value is valid if build out the function more.
        return self._name

    # the rest of the setters and getters for the other values of Animal:
    def set_height(self, height):
        self._height = height

    def set_sound(self, sound):
        self._sound = sound

    def set_weight(self, weight):
        self._weight = weight

    def get_height(self):
        # return heigh as a string?
        return str(self._height)

    def get_sound(self):
        return self._sound

    def get_weight(self):
        return str(self._weight)

    # used to demonstrate polymorphism:
    def get_type(self):
        # prints out the class name
        print("We are using the Animal class")

    # so can print out all the Animal class info to the screen:
    def toString(self):
        # another way to specify string output using curly braces {}
        return "{} is {} cm tall, weighs {} kilograms, and says" \
               " {}".format(self._name, self._height, self._weight,
                            self._sound)

print("Demonstrating what this looks like with some Animal objects:")
print("A kitty object which is of type Animal with values passed to "
      "the constructor:")
cat = Animal('Whiskers', 33, 10, 'Meow')
print(cat.toString())

print("Demonstration of OO Inheritance using a new class called Dog:")


# The Dog class inherits every object from the Animal class
class Dog(Animal):
    # every dog has an owner
    _owner = ""

    '''
    Overwriting the constructor for the animal class so can be more specific:
    Now the owner name is additionally passed in along with everything that
    previously was.
    self, name, height, weight, and sound will still be handled by the parent
    Animal class.
    '''
    def __init__(self, name, height, weight, sound, owner):
        # to set owner
        self._owner = owner
        '''
        the "super" class is the class above in the hierarchy, AKA the parent
        class
        This specifies use the Dog class, and then for the following 4 values,
        pass in the values to the parent Animal class.
        '''
        super(Dog, self).__init__(name, height, weight, sound)

    # setter for the Dog class
    def set_owner(self, owner):
        #_self.owner = owner
        # change the default owner value to the value passed in
        self._owner = owner

    # getter for the Dog class
    def get_owner(self):
        return self._owner

    # for demonstration purposes
    def get_type(self):
        print("We are using a Dog object")

    '''
    Overwriting the Animal toString function, which is mostly a copy+paste
    with a few additions.
    '''
    def toString(self):
        # another way to specify string output using curly braces {}
        return "{} is {} cm tall, weighs {} kilograms, says" \
               " {}, and is owned by {}".format(self._name, self._height,
                                                self._weight, self._sound,
                                                self._owner)

    '''
    Demo of method overloading: Can perform different tasks based on the
    methods sent in.
    '''
    def multiple_sounds(self, how_many=None):
        # if the user has not specified how many times to do the Animal sound
        if how_many is None:
            print(self.get_sound())
        # if the user sent in a value for how many times to do the Animal sound
        else:
            print(self.get_sound() * how_many)

# creating a dog object outside the class
spot = Dog("Spot", 53, 27, "Ruff", "Derek")
print(spot.toString())

'''
Polymorphism
Allows the programmer to refer to classes as their super class and then
automatically have the correct functions called.
'''

print("Polymorphism")

#Polymorphism example
class AnimalTesting:
    # get_type function. Receives animal objects.
    def get_type(self, animal):
        # refers to Animal class and get_type()
        animal.get_type()

test_animals = AnimalTesting()

# test_animals.get_type(Animal)
test_animals.get_type(cat)
# test_animals.get_type(Dog)
test_animals.get_type(spot)

#multiple sounds
print("Multiple sounds:")
print("The default with nothing passed in, is to do the sound once")
spot.multiple_sounds()
print("The cat does not have the multiple_sounds function so a call to it"
      " does nothing and produces an error.")
#cat.multiple_sounds()
print("A call to repeat the animal sound 4 times:")
spot.multiple_sounds(4)