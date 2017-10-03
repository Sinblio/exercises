# Programming Exercise 2-6
#
# Program to calculate a total sale price using state and local sales tax.
# This program prompts a user for an amount of purchase,
# uses constants to calculate state, county and total sales tax, and a purchase total
# then displays the details of these calculations for the user.

# Variables for purchase amount, state tax, county tax, total tax and total sale
# all initialized as floats


# Constants for the state and county tax rates
STATE_TAX_RATE = 0.06
COUNTRY_TAX_RATE = 0.02

# Get the amount of purchase from the user, casting it to a float.
sales_total = float(input("Enter sales total: "))

# Calculate the state sales tax.
state_tax = sales_total * STATE_TAX_RATE

# Calculate the county sales tax.
country_tax = sales_total * COUNTRY_TAX_RATE

# Sum the total tax.
total_tax = country_tax + state_tax

# Calculate the total of the sale.
total = total_tax + sales_total

# Print detailed information about the sale, formatting all values to two decimal places.
print('The total is $ %.2f' %total)




