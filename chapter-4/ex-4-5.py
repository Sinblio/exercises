# Programming Exercise 4-5
#
# Program to compute total and average monthly rainfall over a span of years.
# This program gets a number of years from a user,
# then uses nested loops to prompt for rainfall for each month in each year
#	and calculate the total and the average monthly rainfall,
# then displays the number of months, total rainfall and average monthly rainfall

# Create float variables for total rainfall, monthly rainfall, average monthly rainfall

# Create int variables for number of years and number of months.

# Get number of years from the user

# Nested loop logic to loop through the years and their months
#
# Outer for loop for the number of years

	# Print the current year message

	# Inner loop for 12 months 

		# Get monthly rainfall for current month from the user
		
		# add monthly rainfall to total rainfall
		
		# increment number of months
		
			
# Calculate the average rainfall using total rainfall and number of months

# print the results on the screen, including details for total months, total rainfall,
#	and average monthly rainfall, formatting any floats to 2 decimal places.

total_rainfall = 0

years = int(input("Enter the number of years : "))

for j in range(years) :
	print("Year " + str((j + 1)))
	for k in range(12) :
		total_rainfall += int(input("Enter the average rainfall : "))
		
average_rainfall = total_rainfall / (years * 12)

average_rainfall = "{0:.2f}".format(average_rainfall)

print("Total rainfall : " + str(total_rainfall))
print("Average rainfall : " + average_rainfall)