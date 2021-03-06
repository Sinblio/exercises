# Programming Exercise 5-6
#
# Program to compute calories from fat and carbohydrate.
# This program accepts fat grams and carbohydrate grams consumed from a user,
# uses global constants to calculate the fat calories and carb calories,
# then passes them to a function for formatted display on the screen.

# Global constants for fat calories per gram and carb calories per gram

# define the main function

    # Define local float variables for grams of fat, grams of carbs, calories from fat,
    # and calories from carbs
    
    # Get grams of fat from the user.

    # Get grams of carbs from the user.

    # Calculate calories from fat.

    # Calculate calories from carbs.

    # Call the display calorie detail function, passing grams of fat, grams of carbs,
    # calories from fat and calories from carbs as arguments

# Define a function to display calorie detail.
# This function accepts grams of fat, grams of carbs, calories from fat,
# and calories from carbs as parameters,
# performs no calculations,
# but displays this information formatted for the user.

	# print each piece of information with floats formatted to 2 decimal places.

# Call the main function to start the program

FAT_CALORIES_PER_GRAM = 9
CARB_CALORIES_PER_GRAM = 4

def  main() :
    grams_of_fat = int(input("Enter the number of carbs in grams : "))
    grams_of_carbs = int(input("Enter the number of carbs in grams : "))
    
    calories_from_fat = FAT_CALORIES_PER_GRAM * grams_of_fat
    calories_from_carbs = CARB_CALORIES_PER_GRAM * grams_of_carbs
    
    display_calories(calories_from_fat, calories_from_carbs)
    
def display_calories(fat_calories, carb_calories) :
    print(str(fat_calories) + " calories from fat")
    print(str(carb_calories) + " calories from carbs")
    
main()