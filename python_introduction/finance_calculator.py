monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
#calculate monthly savings
monthly_savings = monthly_income - monthly_expenses
#display monthly savings
print(f"Your monthly savings are: {monthly_savings}")
# project annual savings
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
# output results
print(f"Projected savings after one year, with interest, is: {Projected_Savings}")
