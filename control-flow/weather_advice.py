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
        # Handle cases where the input does not match the predefined conditions
        print("Sorry, I don't have recommendations for this weather.")

# Call the function to run the program
if __name__ == "__main__":
    get_weather_recommendation()
