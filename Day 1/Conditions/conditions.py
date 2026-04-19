# 🧠 1. What are Conditions?

# Conditions allow your program to make decisions.

# 👉 Think:

# ATM → check balance
# Login → check password
# App → check user access


# if condition:
# code runs if condition is True
age = 18
if age >= 18:
    print("You can vote")

balance = 500

#if-else:👉 Real-world: Banking system
if balance > 1000:
    print("You can withdraw")
else:
    print("Insufficient balance")

# if - elif - else (Multiple Conditions):
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")

#  Comparison Operators
# Operator	Meaning
# ==	    equal
# !=	    not equal
# >	        greater
# <	        smaller
# >=	    greater equal
# <=	    smaller equal

#Logical Operators
#1. And
age = 20
is_id_verified = True

if age >= 18 and is_id_verified:
    print("Allowed")
#2. Or
if age >= 18 or is_id_verified:
    print("Allowed")
#3. Not
is_logged_in = False

if not is_logged_in:
    print("Please login")

# 🧠 Industry Thinking

# Always think:

# 👉 “What conditions control this system?”

# Example:

# Login → username + password
# Payment → balance + limits
# App → user role (admin/user)
