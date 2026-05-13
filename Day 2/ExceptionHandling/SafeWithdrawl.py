balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount.")
    elif amount <= balance:
        balance -= amount
        print("Withdrawal successful.")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance.")

except ValueError:
    print("Please enter a valid number.")