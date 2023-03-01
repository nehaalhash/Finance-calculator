# Create finance calculator for investment and home loan repayment.
# Can choose between Simple and compound interest for both finance options
# For Investment: Need to know $ amount, interest rate, length of term and whether simple/compound interest
# For home loan repayments: Need to know value, interest rate and term. Then use repayment formula

import math

print("Here's a finance calculator to project your outlook depending on your finance product\n")
finance_product = input("Which finance product are you interested in: \n "
                        "Investment - To calculate the amount of interest you'll earn on your investment\n "
                        "Bond - To calculate the amount you'll have to pay on a home loan\n"
                        "Please enter your choice: ")
if finance_product.lower() == "investment" or finance_product.upper() == "INVESTMENT":
    amount = int(input("How much do you want to deposit? "))
    rate = float(input("What is the interest rate? "))
    term = int(input("How many years do you plan on investing? "))
    interest = input("Do you want simple or compound interest? ")
    if interest.lower() == "simple" or interest.upper() == "SIMPLE":
        simple = round(amount * (1 + (rate / 100) * term), 1)
        print(f"You could receive {simple}")
    elif interest.lower() == "compound" or interest.upper() == "COMPOUND":
        compound = round(amount * math.pow((1 + (rate / 100)), term), 1)
        print(f"You could receive £{compound}")

if finance_product.lower() == "bond" or finance_product.upper() == "BOND":
    principle = float(input("What is the present value of your house? "))
    rate = float(input("What is the interest rate? "))
    term = int(input("How many months will it take you to repay the bond? "))
    monthly_interest = (rate/100) / 12.0
    repayment = round(principle * (monthly_interest / (1-(1+monthly_interest)**(-term))), 2)
    print(f"You monthly repayments will be £{repayment} per month ")

else:
    print("Please enter a value")
