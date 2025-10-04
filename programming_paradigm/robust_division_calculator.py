#Objective: Implement a division calculator that robustly handles errors like division by zero
#and non-numeric inputs using command line arguments.
#Task Description:
#Create two Python scripts: robust_division_calculator.py,
# which contains the division logic including error handling, and main.py, 
# which interfaces with the user through the command line.

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            return "Error: Division by zero is not allowed."
        return f"Result: {num / denom}"
    except ValueError:
        return "Error: Both numerator and denominator must be numeric values."
    