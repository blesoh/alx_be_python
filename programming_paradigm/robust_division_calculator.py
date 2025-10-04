#Objective: Implement a division calculator that robustly handles errors like division by zero
#and non-numeric inputs using command line arguments.
#Task Description:
#Create two Python scripts: robust_division_calculator.py,
# which contains the division logic including error handling, and main.py, 
# which interfaces with the user through the command line.

def safe_divide(numerator, denominator):
    try:
        num = float(str(numerator).strip())
        den = float(str(denominator).strip())
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"
    