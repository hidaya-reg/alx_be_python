def safe_divide(numerator, denominator):
    try:
        return f"The result of the division is {float(numerator) / float(denominator)}"
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")