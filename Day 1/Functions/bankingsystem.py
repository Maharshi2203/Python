def withdraw(balance,amount):
    if balance >= amount:
        return balance - amount
    else:
        print("Insufficient Balance...")

print(withdraw(5000,1000)) #4000