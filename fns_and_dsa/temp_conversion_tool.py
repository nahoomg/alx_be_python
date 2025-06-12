
def convert_to_celsius(fahrenheit):
  
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
   
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    
    try:
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
    except ValueError:
        # Raise a ValueError if the input is not a numeric value
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    elif unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()