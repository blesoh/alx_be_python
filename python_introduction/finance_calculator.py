# users financial details
monthly_income =int(input("Enter your monthly income: "))
monthly_expense = int(input("Enter your total monthly expense: "))
# Calculaate monthly savings
monthly_savings = monthly_income - monthly_expense
print(f"Your monthly savings are ${monthly_savings}")
# project savings after 1 year
project_annual_savings = (monthly_savings * 12 ) + (monthly_savings * 12 * 0.05)
# display projected savings after including interest
print(f"Projected annual savings after 1 year,with interest, is: ${project_annual_savings}") 