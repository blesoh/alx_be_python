# users financial details
Monthly_income =int(input("Enter your monthly income: "))
Monthly_expense = int(input("Enter your total monthly expense: "))
# Calculaate monthly savings
Monthly_saving = Monthly_income - Monthly_expense
print(f"Your monthly saving is: ${Monthly_saving}")
# project savings after 1 year
project_savings = (Monthly_saving * 12 + (Monthly_saving * 12 * 0.05))
# display projected savings after including interest
print(f"Your projected savings after 1 year is: ${project_savings}")
