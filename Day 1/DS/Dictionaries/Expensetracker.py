transactions=[]
def add_transaction(type,amount):
    transactions.append({
        "type":type,
        "amount":amount
    })

add_transaction("income", 1000)
add_transaction("expense", 200)

for t in transactions:
    print(t["type"],t["amount"])