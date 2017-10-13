# Programming Exercise 3-6
#
# Program to check if a date is 'magic' (day * month = year).
# This program takes a month, day and year from the user as integers,
# Checks to see if each is in range, then checks whether month * day = year,
# then displays an appropriate message depending on the result

# Variables for month, day, year and message
# initialize month, day and year as integers, message as a string
# Get month and cast it to int
# Get day and cast it to int
# Get year and cast it to int

# This problem can be solved with if-else logic by the reducing the problem domain
# if month input is out of range
	# set message to hold "invalid month" message

# else if day input is out of range
    # set message to hold "invalid day" message
# else if  year input is out of range (greater than 99 or less than 0)
    # set message to hold "invalid year" message
# else 
    # set message to hold the date in 00/00/00 form
    # if day * month equals year, add " is a magic date" to message
    # else add " is not a magic date" to message

# print message for the user

message = ""

month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
year = int(input("Enter the year: "))

if month < 1 or month > 12 :
    message = "invalid day"
elif day < 1 or day > 31 :
    message = "invalid day"
elif year < 0 or year > 99 :
    message - "Invalid year"
else :
    message = str(month) + "/" + str(day) + "/" + str(year)
    if month * day == year :
        message += " is a magic date"
    else : 
        message += " is not a magic date"

print(message)