password = input("Enter the password: ")

if len(password) >= 8:
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password )
    
    if has_digit and has_upper:
        print("Strong Password")
    else:
        print("Weak password")
else:
    print("Too short")

