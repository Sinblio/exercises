# Programming Exercise 5-1
#
# Program to convert kilometers to miles.
# This program accepts a distance in kilometers from the user,
# passes it to a function, which calculates its value in miles
# and displays the result for the user.


# Global constant for the ratio of kilometers to miles


# define the main function

    # Define a local float variable to hold the distance in kilometers

    # Get distance in kilometers from the user

    # pass the distance in kilometers to a function to convert to miles

# define the function to convert to miles
# the function takes kilometers as an argument
# calculates the equivalent number of miles
# and prints the result

    # Define a local float variable for miles

	# use the global conversion constant to compute miles    
    
    # print the results, formatting float values to 2 decimal places

# Call the main function to start the program

KM_TO_MILES = 0.621

def main() :
    kilometers = int(input("Enter the Kilometers : "))
    miles = convert_to_miles(kilometers)
    miles = format(miles, ".2f")
    print(str(miles) + " miles")

def convert_to_miles(kilometers) :
    miles = kilometers * KM_TO_MILES
    return miles;
    
main()