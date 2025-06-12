def safe_divide(numerator, denominator):
    """
    Performs division, robustly handling potential errors like division by zero
    and non-numeric inputs.

    Args:
        numerator (str/int/float): The numerator for the division.
        denominator (str/int/float): The denominator for the division.

    Returns:
        str: An error message if an error occurs, otherwise the result of the division.
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."