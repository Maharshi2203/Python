email = input("Enter the email: ")

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")