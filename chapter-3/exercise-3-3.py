# Programming Exercise 3-3
#
# Program to assign an age category to an numerical age.
# This program will prompt the user for an integer age value,
# and use it to choose an age category,
# then display that category on the screen.

# Variables to hold an age and a category.
# initialize age as an int and category as a string.

# Get the person's age.
# remember to convert the input to an int.


# Determine if the person is an infant, child, teenager, or adult and set the category.
# Use a series of if ... elif ... etc. statements.

# display a message with the age category.

age = 0
category = ""

age = int(input("Enter your age : "))

if (age < 2) :
    category = "Infant"
elif (age < 12) :
    category = "Child"
elif (age < 18) :
    category = "Teenager"
else :
    category = "Adult"
    
print(category)