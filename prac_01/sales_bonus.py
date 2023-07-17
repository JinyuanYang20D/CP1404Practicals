"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BONUS_LEVEL = 1000
BONUS_RATE_ONE = 0.1
BONUS_RATE_TWO = 0.15
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < BONUS_LEVEL:
        bonus = BONUS_RATE_ONE * sales
        print(bonus)
    else:
        bonus = BONUS_RATE_TWO * sales
        print(bonus)
    sales = float(input("Enter sales: $"))