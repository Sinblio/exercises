# Programming Exercise 2-4
#
# Program to compute a final price for five items with tax.
# This program will prompt a user for a set of five prices,
# sum them to a subtotal and calculate sales tax with tax rate stored in a constant,
# then display the results on the screen.

# Variables to hold the prices of five items, the subtotal, and the total.
# All should be initialized as floats.


# Constant for the sales tax rate.
TAX_RATE = 0.07

# Get the price of each item by prompting the user.
# You will need to convert each input to a float.
ary = [None]*5
for x in range(0, 5):
    ary[x] = float(input("Enter item price : "))

# Calculate the subtotal by adding up the item prices.
sub_total = 0.0
for x in ary:
    sub_total += x

# Calculate the sales tax by multiplying the subtotal by the tax rate.
sales_tax = TAX_RATE * sub_total

# Calculate the total by adding the subtotal and tax.
total = sales_tax + sub_total

# Print the values for the subtotal, tax and total.
# Label each value, and format them to display with two decimal places. 
print("subtotal : $ %.2f" % sub_total)
print("tax : $ %.2f" % sales_tax)
print("total : $ %.2f" % total)




