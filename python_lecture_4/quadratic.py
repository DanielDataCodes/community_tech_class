import math
def morgage_calculator(principal, annual_interest_rate, years):
    r = annual_interest_rate / 100 / 12
    n =years * 12
    if r == 0:
        return principal / n
    else:
        monthly_payment = principal * (r * math.pow(1 + r, n)) / (math.pow(1 + r, n) - 1)
    
    return monthly_payment

loan_amount = float(input("Enter the loan amount: "))
interest_rate = float(input("Enter the annual interest rate (in %): "))
loan_term_years = int(input("Enter the loan term (in years): "))

monthly_payment = morgage_calculator(loan_amount, interest_rate, loan_term_years)
print(f"Your monthly payment is: ${monthly_payment:.2f}")