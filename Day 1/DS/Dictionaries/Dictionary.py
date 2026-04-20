# 👉 What is a Dictionary?

# Stores data in key : value format

# 👉 Like JSON (VERY IMPORTANT)

#syntax
user = {
    "name": "Maharshi",
    "age": 20,
    "balance": 5000
}

print(user["name"])
print(user["age"])
print(user["balance"])

#Modify Data
user["balance"] = 6000
print(user["balance"])

#add new Key
user["city"] = "Ahmedabad"
print(user)

#remove key
del user["age"]
print(user)

#Loop Through Dictionary
for key, value in user.items():
    print(key, value)

# List of Dictionaries (REAL INDUSTRY DATA)
users = [
    {"name": "Maharshi", "balance": 5000},
    {"name": "Rahul", "balance": 3000}
]

for user in users:
    print(user["name"], user["balance"])

# 👉 Used in:

# Databases
# APIs
# Dashboards

# 👉 Most real systems = list of dictionaries

    # Example:

    # Users
    # Orders
    # Transactions
    # API responses