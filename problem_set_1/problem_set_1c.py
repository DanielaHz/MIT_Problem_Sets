import math

#  PROBLEM SET 1.

# PART C: Finding the right amount to save away.

# SOLUTION

# starting_salary =  The user's starting salary.
starting_salary = float(input("Enter your starting salary: "))

# TOTAL_COST =  Total cost of the house.
TOTAL_COST = 1000000

# SEMI_ANNUAL_RAISE = salary raises any six months
SEMI_ANNUAL_RAISE = 0.07
# down_payment = Cost needed for a down payment. The 25% was assumed.
DOWN_PAYMENT = 0.25*TOTAL_COST

# MONTLY_SALARY = The user's montly salary
montly_salary = starting_salary/12

# r = annual return from user's investments
R = 0.04

# BISECTION RESEARCH IMPLEMENTATION

STEP_SIZE = 10000
MONTHS = 36
TOLERANCE = 100

low = 0
high = 10000
counter = 0


def compute_savings_at_month(starting_salary, SEMI_ANNUAL_RAISE, montly_salary, R, portion_saved):
    """ This function computes the current savings necessary to achieve your down payment 
        in a specific time <MONTHS> """

    current_savings = 0
    for months in range(0, MONTHS + 1, 1):
        montly_portion_saved = montly_salary * portion_saved
        r_current_savings = current_savings * R/12
        current_savings = montly_portion_saved + r_current_savings + current_savings
        if months % 6 == 0:
            starting_salary = starting_salary + starting_salary * SEMI_ANNUAL_RAISE
            montly_salary = starting_salary/12
            montly_portion_saved = montly_salary*portion_saved
    return current_savings


while True:
    guess = math.trunc((low+high)/2)/STEP_SIZE

    current_savings = compute_savings_at_month(
        starting_salary, SEMI_ANNUAL_RAISE, montly_salary, R, guess)

    print(
        f"current savings: {current_savings}, downpayment: {DOWN_PAYMENT}, difference is: {abs(current_savings - DOWN_PAYMENT)}")

    if abs(current_savings - DOWN_PAYMENT) <= TOLERANCE:
        print("Result", guess)
        print('Number of attemps', counter)
        break

    if current_savings - DOWN_PAYMENT < 0:
        low = guess * STEP_SIZE
    elif current_savings - DOWN_PAYMENT > 0:
        high = guess * STEP_SIZE

    counter += 1
