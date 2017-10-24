# Programming Exercise 5-4
#
# Program to compute monthly and annual auto expenses.
# This program prompts a user for several auto monthly expense amounts,
# then passes them to a function to total the values, annualize them,
# and display the details and totals on the screen.

# define the main function
    # Define local float variables for loan, insurance, gas, oil, tires and maintenance
    # Get the amount of the monthly loan payment from the user.
    # Get the amount of the monthly insurance from the user.
    # Get the amount of the monthly gas from the user.
    # Get the amount of the monthly oil from the user.
    # Get the amount for monthly tire wear from the users.
    # Get the amount for monthly maintenance from the user.
    # Call the function to summarize car expenses,
    # passing the loan, insurance, gas, oil, tires and maintenance as arguments

# Define a function to summarize car expenses,
# it accepts loan, insurance, gas, oil, tires, and maintenance as arguments,
# calculates a monthly total and an annual total,
# and displays these totals.
    # Define local float variables for monthly total and annual total
    # calculate the monthly total
    # calculate the annual total
    # Print monthly and annual information, formatting float value to 2 decimal places.

# Call the main function to start the program

def main() :
    monthly_loan_payments = int(input("Enter your monthly loan payments : "))
    monthly_insurance = int(input("Enter your monthy insurance : "))
    monthly_gas = int(input("Enter your monthly gas : "))
    monthly_oil = int(input("Enter you monthly oil : "))
    monthly_tire_wear = int(input("Enter your monthly tire wear : "))
    monthly_maintenance = int(input("Enter your monthly maintenance : "))
    
    summerize_car_expences(monthly_loan_payments, monthly_insurance, monthly_gas, monthly_oil, monthly_tire_wear, monthly_maintenance)
    
def summerize_car_expences(loan, insurance, gas, oil, tires, maintenance) :
    monthly_total = loan + insurance + gas + oil + tires + maintenance
    annual_total = monthly_total * 12
    
    monthly_total = format(monthly_total, ".2f")
    annual_total = format(annual_total, ".2f")
    
    print("Your monthly total is : " + monthly_total)
    print("Your annual total is : " + annual_total)

main()