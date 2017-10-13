# Programming Exercise 4-1
#
# Program to total the values of five integers.
# This program the user for an integer five times,
# and totals them up,
# then displays the total entered on the screen.

# Initialize variables for bugs collected and total bugs.
# be sure to initialize them as integers

# Get the number of bugs collected from the user
# use a for loop to get the number of bugs exactly five times, once for each day

	# input bugs collected on this day and convert it to an int

    # add bugs collected to total bugs

# Display the total number of bugs collected for all five days.

total_bugs = 0

for j in range(5) :
    total_bugs += int(input("Enter the number of bugs collected on day " + str(j + 1) + " : "))

print("Total nimber of bugs collected : " + str(total_bugs))