# Programming Exercise 2-3
#
# Program to convert area in square feet to acres.
# This program will prompt a user for the size of a tract in square feet,
# then use a constant ratio value to calculate it value in acres
# and display the result to the user.

# Variables to hold the size of the tract and number of acres.
# be sure to initialize these as floats
sq_feet = 1.0
acres = 1.0

# Constant for the number of square feet in an acre.
SQUARE_TO_ACRE = 43560.0

# Get the square feet in the tract from the user.
# you will need to convert this input to a float
sq_feet = float(input("Enter Square Feet :"))

# Calculate the number of acres.
acres = sq_feet / SQUARE_TO_ACRE

# Print the number of acres.
# remember to format the acres to two decimal places
print("$ %.2f acres" %acres)




