balance = 10000
amount = int(input("Enter the amount: "))
is_server_up = True

if is_server_up:
    if amount <= balance:
        print("Transaction Successful..")
    else:
        print("Insufficient Balance..")
else:
    print("Server is down....")