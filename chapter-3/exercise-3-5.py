# Programming Exercise 3-5
#
# Program to convert a value in kilograms to Newtons, then check whether it is in range.
# This program will prompt a user for a mass in kilograms,
# convert it to Newtons and use constants to check if the weight is within range,
# then display the weight and a range message.

# Global constants for minimum, maximum and mass multiplier values

# Variables for weight and mass initialized as floats   

# Get mass from user and convert it to a float

# Calculate weight using the mass multiplier constant

# Display the weight

# If weight > maximum or < than minimum display an appropriate message

MINIMUM = 10
MAXIMUM = 1000
GRAVITY = 9.8

weight = 0.0
mass = 0.0
out = ""

mass = float(input("Enter the mass : "))

weight = mass * GRAVITY

if (weight > MAXIMUM) :
    out = "weight is too large"
elif (weight < MINIMUM) :
    out = "weight is too low"
else :
    out = "weight is within range"
    
weight = "{0:.2f}".format(weight)

print(weight)
print(out)