# 🧠 1. How to THINK in Conditions (Important)

# Instead of writing code directly, think like:

# 👉 Input → Condition → Output

# Example:

# Input: balance, withdraw amount
# Condition: withdraw ≤ balance
# Output: success / fail

#Secure login system
username = input("Enter the username: ")
password = int(input("Enter the password: "))

if username=="Admin":
    if password == 12345:
        print("Login Successfully...")
    else:
        print("Invalid Password....")
else: 
    print("User Not Found")

# 💼 Real-world Use:
# Banking apps
# Admin panels
# Role-based systems

# BAD APPROACH
# if age >= 18:
#     if country == "India":
#         print("Eligible")

#✅ Better (clean + industry)
# if age >= 18 and country == "India":
#     print("Eligible")

# Python treats some values as False automatically:

# ❌ Falsy values:
# 0
# "" (empty string)
# None
# [] (empty list)

name = ""

if name:
    print("Valid")
else:
    print("Empty name")


# Short-hand Conditions (Clean code)
age = 20
status= "Adult" if age > 18 else "minor"
print(status)

# 👉 Used in:

# UI logic
# APIs
# Fast decisions


# ⚠️ Common Industry Mistakes
# ❌ Writing too many nested ifs

# 👉 Makes code unreadable

# ❌ Not validating input

# 👉 Causes crashes

# ❌ Hardcoding values

# 👉 Not scalable