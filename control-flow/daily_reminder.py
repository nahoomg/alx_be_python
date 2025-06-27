# This script provides a personal daily reminder based on user input
# for a single task, its priority, and time sensitivity.

def daily_reminder():
    """
    Prompts the user for a single task's description, priority (high/medium/low),
    and whether it's time-bound (yes/no).
    It then provides a customized reminder using match-case and if statements.
    """
    # Prompt user for task description
    task = input("Enter your task: ")

    # Prompt user for task priority (convert to lowercase for case-insensitive comparison)
    priority = input("Priority (high/medium/low): ").lower()

    # Prompt user if the task is time-bound (convert to lowercase)
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    reminder_message = "" # Initialize reminder message

    # Use a match case statement to process the task based on its priority
    match priority:
        case "high":
            reminder_message = f"'{task}' is a high priority task"
        case "medium":
            reminder_message = f"'{task}' is a medium priority task"
        case "low":
            reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        case _: # Default case for invalid priority input
            print("Invalid priority entered. Please choose high, medium, or low.")
            return # Exit the function if priority is invalid

    # Check if the task is time-bound and modify the message accordingly
    if time_bound == "yes":
        # For high and medium priority, add the immediate attention phrase.
        # For low priority, the "consider completing" phrase is already in the match case,
        # so we don't add "immediate attention" to low priority tasks.
        if priority == "high" or priority == "medium":
            reminder_message += " that requires immediate attention today!"
        else:
            # If it's a time-bound low priority task, we might just emphasize it slightly,
            # or keep the default low priority message as per example.
            # The example shows no 'immediate attention' for low priority even if time-bound.
            # Sticking to the example output for low priority time-bound tasks.
            pass # No change needed for low priority based on example
    elif time_bound == "no":
        # If it's not time-bound, and it's high/medium, it's just a regular reminder.
        # The 'low' priority message already handles the non-time-bound case well.
        if priority == "high" or priority == "medium":
            reminder_message = f"'{task}' is a {priority} priority task. You can complete it today."
            # Adjusting the message for non-time-bound high/medium based on overall context
            # The prompt example only shows specific wording for high+time_bound and low+not_time_bound.
            # Let's align with the general spirit: if not time-bound, no "immediate attention"
            # For simplicity and adhering to examples, the initial match case for high/medium is sufficient
            # if no "immediate attention" is added. Let's re-evaluate.

            # Re-evaluation: The examples guide the output.
            # 1. High priority, time-bound: "high priority task that requires immediate attention today!"
            # 2. Low priority, not time-bound: "low priority task. Consider completing it when you have free time."
            # Other combinations are implicitly handled by the base messages from match-case,
            # and the *addition* of "immediate attention" only for time_bound "yes" AND high/medium.

            # Let's refine the logic to precisely match the examples' outcomes.
            # The original `reminder_message` for high/medium without the time-bound suffix is good.
            # The low priority message is also good.
            # The `if time_bound == "yes"` block *adds* the specific phrase.
            # So, if time_bound is "no", nothing additional is added, which matches the example.
            pass # No additional modification needed for 'no' based on examples
    else:
        print("Invalid input for time-bound. Please enter 'yes' or 'no'.")
        return # Exit if time_bound input is invalid

    # Print the customized reminder
    print(f"Reminder: {reminder_message}")

# Call the function to run the daily reminder program
if __name__ == "__main__":
    daily_reminder()
