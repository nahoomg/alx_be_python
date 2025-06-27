# This script asks the user about the current weather conditions
# and provides clothing recommendations based on the input.

def get_weather_recommendation():
    """
    Prompts the user for current weather conditions (sunny/rainy/cold)
    and prints appropriate clothing recommendations.
    Handles unexpected input with a default message.
    """
    # Prompt the user to input the current weather condition
    weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

    # Provide clothing recommendations based on the user's input
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")

# Call the function to run the program
if __name__ == "__main__":
    get_weather_recommendation()
# This script provides clothing recommendations based on the current weather conditions.

# It handles unexpected input gracefully by providing a default message.
# The user is prompted to input the weather condition, and the script responds accordingly.# The recommendations are tailored to common weather conditions: sunny, rainy, and cold.
# If the input does not match any of these conditions, a default message is displayed.  
else:
    print("Invalid input. Please enter sunny, rainy, or cold.")
