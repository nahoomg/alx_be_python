# Prompt the user to enter their current age.
# The input() function reads data as a string, so we convert it to an integer
# using int() for numerical calculations.
current_age = int(input("How old are you? "))

# Calculate the age in the year 2050.
# Assuming the current year is 2023, the difference to 2050 is 27 years (2050 - 2023 = 27).
age_in_2050 = current_age + 27

# Print the calculated age in 2050 using an f-string for easy formatting.
print(f"In 2050, you will be {age_in_2050} years old.")
