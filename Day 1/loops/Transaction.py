# 💻 Build: Transaction Processor
# Create a list of transactions:
# [1000, -200, 500, -100]
# Calculate:
# Total balance
# Count of expenses (negative values)

transactions = [1000, -200, 500, -100]

balance = 0
expense_count = 0

for amount in transactions:
    balance += amount
    
    if amount < 0:
        expense_count += 1

print("Total Balance:", balance)
print("Total Expenses Count:", expense_count)


