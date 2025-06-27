# This script draws a square pattern of asterisks using nested loops.

def draw_pattern():
    """
    Prompts the user for a positive integer representing the pattern size,
    then draws a square pattern of asterisks (*) of that size using
    nested while and for loops.
    Handles invalid input gracefully.
    """
    while True:
        try:
            # Prompt the user for the size of the pattern
            size = int(input("Enter the size of the pattern: "))
            if size <= 0:
                print("Please enter a positive integer.")
            else:
                break # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    row_count = 0
    # Outer while loop iterates through each row of the pattern
    while row_count < size:
        # Inner for loop prints asterisks for the current row
        for _ in range(size):
            # Print an asterisk without moving to a new line
            print("*", end="")
        
        # After printing all asterisks for the current row, print a newline
        # to move to the next row
        print()
        
        # Increment the row counter
        row_count += 1

# Call the function to run the pattern drawing program
if __name__ == "__main__":
    draw_pattern()
