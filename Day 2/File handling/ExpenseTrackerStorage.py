def saveTransaction(type,amount):
    with open("transaction.txt","a") as file:
        file.write(f"{type}: {amount}\n")

saveTransaction("income","20000")
saveTransaction("expense","5000")

