#  PROBLEM SET 1

# PART B: Saving, with a raise.

# SOLUTION

# annual_salary = The user's annual salary.
annual_salary = float(input("Enter your annual salary: "))

# portion_saved =  The user's portion to be saved each month.
portion_saved = float(input("Enter your portion of salary to be saved: "))

# total_cost =  Total cost of the house.
total_cost = float(input("Enter the total cost of your dream house: "))

# semi_annual_raise = salary raises any six months.
semi_annual_raise = float(input("Enter semi-annual raise, as a decimal: "))

# portion_down_payment = Cost needed for a down payment. The 25% was assumed.
down_payment = 0.25*total_cost

# montly_salary = The user's montly salary.
montly_salary = annual_salary/12

# current_savings= amount that you have saved thus far.
current_savings = 0

# r = annual return from user's investments
R = 0.04

# reset the month counter to zero
months = 0

while current_savings < down_payment:
    montly_portion_saved = montly_salary * portion_saved
    r_current_savings = current_savings * R/12
    current_savings = montly_portion_saved + r_current_savings + current_savings
    months += 1
    if months % 6 == 0:
        annual_salary = annual_salary + annual_salary*semi_annual_raise
        montly_salary = annual_salary/12
        montly_portion_saved = montly_salary*portion_saved

print("The number of months to success in your goal is: ", months, "months")
