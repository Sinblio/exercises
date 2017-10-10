# Programming Exercise 3-4
#
# Program to convert a number from 1 to 10 to a Roman numeral.
# This program will accept an integer from 1 to 10 from the user
# and use it to choose an appropriate Roman numeral
# to display on the screen.

# Variables to hold a number and a numeral.
# initialize the number as an int and the numeral as a string.

# Get number from user and convert it to an int

# Set numeral to a Roman numeral value based on the value of number
# use a set of if ... elif .... etc. statements.

# use a final else to display an error if number is out of range.

# display the numeral on the screen.

number = 0
numeral = ""

number = int(input("Enter the number : "))

def num_to_numeral(argument):
    switcher = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
    }
    return switcher.get(argument,"Number not in range")
    
numeral = num_to_numeral(number)

print(numeral)