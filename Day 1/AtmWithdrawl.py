balance = 5000
withdraw = int(input("Enter the amount: "))

if withdraw <= balance:
    print("Transaction Successful")
else:
    print("Insufficient balance...")


# Output  
# Enter the amount: 2000
# Transaction Successful

#Enter the amount: 7000
#Insufficient balance...