# This script generates and prints the multiplication table for a given number.

def generate_multiplication_table():
    """
    Prompts the user for a number and then prints its multiplication
    table from 1 to 10 using a for loop.
    Handles invalid input gracefully.
    """
    try:
        # Prompt the user to input a number
        number = int(input("Enter a number to see its multiplication table: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    print(f"Multiplication table for {number}:")
    # Use a for loop to iterate from 1 to 10
    for i in range(1, 11):  # range(1, 11) includes 1 and goes up to (but not including) 11
        # Calculate the product
        product = number * i
        # Print each line of the multiplication table
        print(f"{number} * {i} = {product}")

# Call the function to run the multiplication table generator
if __name__ == "__main__":
    generate_multiplication_table()
