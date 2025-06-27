# This script implements a simple calculator using match case statements.

def simple_calculator():
    """
    Prompts the user for two numbers and an operation (+, -, *, /),
    then performs the calculation using a match case statement.
    Handles division by zero gracefully.
    """
    try:
        # Prompt for the first number
        num1 = float(input("Enter the first number: "))
        # Prompt for the second number
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    # Prompt for the operation
    operation = input("Choose the operation (+, -, *, /): ")

    result = None

    # Use match case statement to perform the selected operation
    match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {result}.")
        case '-':
            result = num1 - num2
            print(f"The result is {result}.")
        case '*':
            result = num1 * num2
            print(f"The result is {result}.")
        case '/':
            if num2 == 0:
                # Handle division by zero case
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}.")
        case _:
            # Handle unexpected or invalid operation input
            print("Invalid operation. Please choose from +, -, *, /.")

# Call the function to run the calculator program
if __name__ == "__main__":
    simple_calculator()
