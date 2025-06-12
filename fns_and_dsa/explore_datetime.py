from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date # Return for potential use in other functions, though not explicitly required by prompt.

def calculate_future_date(current_date):
    """
    Prompts the user for a number of days and calculates a future date.

    Args:
        current_date (datetime): The starting date from which to calculate the future date.
    """
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        if days_to_add < 0:
            print("Please enter a non-negative number of days.")
            return

        future_date = current_date + timedelta(days=days_to_add)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")

def main():
    """Main function to run the datetime exploration tasks."""
    current_dt = display_current_datetime()
    calculate_future_date(current_dt)

if __name__ == "__main__":
    main()