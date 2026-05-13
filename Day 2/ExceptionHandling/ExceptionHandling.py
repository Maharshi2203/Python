# Exception Handling (Writing Crash-Safe Code)

# In industry, code should not crash when something unexpected happens.

# Examples:

# User enters "abc" instead of a number.
# File does not exist.
# API is unavailable.

# Exception handling lets your program detect these errors and respond gracefully.

# 🧠 1. What is an Exception?

# An exception is a runtime error.

# Example:

# num = int("abc")

# Output:

# ValueError: invalid literal for int()

# 2. Common Exceptions
# Exception	When It Happens
# ValueError	Invalid type conversion
# FileNotFoundError	File not found
# ZeroDivisionError	Division by zero
# KeyError	Dictionary key missing
# IndexError	Invalid list index

#3. Multiple Exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ValueError:
    print("Invalid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# 4. else Block
# Runs only if no exception occurs.
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print("You entered:", num)


# 5. finally Block
# Runs whether an error occurs or not.

try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed.")

