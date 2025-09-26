#Arithmetic Operations Function
# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation on num1 and num2.

    Parameters:
        num1 (float): first number
        num2 (float): second number
        operation (str): 'add', 'subtract', 'multiply', or 'divide'

    Returns:
        float or str: numeric result for successful operations, or an error message string
    """
    # Normalize the operation string so input is flexible (case and spacing)
    op = operation.strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        # Handle division by zero gracefully
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation. Choose 'add', 'subtract', 'multiply', or 'divide'."

 