# Programming Exercise 3-2
#
# Program to find which of two rectangles has the greater area.
# This program will get two sets of lengths and widths from a user,
# use them to calculate and compare two area values,
# and display a message comparing those areas

# Local variables
# you need length, width and area for A and for B
# initialize these as floats


# Get length A from the user and convert it to a float


# Get width A from the user and convert it to a float


# Get length B from the user and convert it to a float


# Get width B from the user and convert it to a float


# Calculate area A


# Calculate area B


# Print each area, formatting the values to 2 decimal places

# if area A is greater, print "A is greater" message.

# else if area B is greater, print "B is greater" message.

# else print "A and B are equal" message.

length_A = float(input("Enter rectangle A's length: "))
width_A = float(input("Enter rectangle A's width: "))
length_B = float(input("Enter rectangle B's length: "))
width_B = float(input("Enter rectangle B's width: "))

area_a = length_A * width_A
area_b = length_B * width_B

if area_a > area_b :
    out = "The Area of A is greater than the Area of B"
elif area_b > area_a :
    out = "The Ares of B is greater than the Area of A"
else :
    out = "The Areas of both A and B are equal"

area_a = "{0:.2f}".format(area_a)
area_b = "{0:.2f}".format(area_b)

print("Area A : " + area_a)
print("Area B : " + area_b)
print(out)