# Programming Exercise 5-5
#
# Program to compute assessed value and property tax.
# This program accepts a property value from a user,
# uses global constants to calculate an assessed value and property tax,
# then passes them to a function to display the results for the user.



# Global constants for assessment percentage and property tax rate

# define the main function

    # Define local float variables for property value, assessed value and property tax

    # Get the property value from the user.

    # Calculate the assessed value using the global constant

    # Calculate the property tax using the global constant

    # Call the function to display property tax information, 
    # passing assessed value and property tax as arguments

# Define a function to display property tax information.
# This function accepts the assessed value and property tax as parameters,
# performs no calculations,
# but displays the information with float variables formatted to 2 decimal places.

	# display the assessed value
	
	# display the property tax

# Call the main function to begin the program.

ASSESMENT_PERCENT = .54
PROPERTY_TAX_RATE = .65

def main() :
    property_value = int(input("Enter the property value : "))
    
    assessed_value = property_value * ASSESMENT_PERCENT
    property_tax = property_value * PROPERTY_TAX_RATE
    
    display_calc(assessed_value, property_tax)
    
def display_calc(assessed_value, property_tax) :
    assessed_value = format(assessed_value, ".2f")
    property_tax = format(property_tax, ".2f")
    
    print("Your assesed value is : " + assessed_value)
    print("Your property tax is : " + property_tax)

main()
