# 🧠 1. What is a Loop?

# A loop lets you repeat a task automatically.

# 👉 Think real-world:

# Sending emails to 1000 users
# Processing transactions
# Reading data line by line

# 2. for Loop (MOST USED)
for i in range(5):
    print(i) #0 1 2 3 4

# How range() works
range(5)        # 0 to 4
range(1, 5)     # 1 to 4
range(1, 10, 2) # step = 2

# while Loop (Condition-based Loop)
i=0

while i<5:
    print(i)
    i+=1

# Running System Until Exit
while True:
    command = input("Enter the command: ")

    if command == "Exit":
        break

# 👉 Used in:

# Servers
# Chat systems
# CLI apps


# break & continue
# break → stops loop
for i in range(10):
    if i == 5:
        break
    print(i)

# continue → skip current iteration
for i in range(10):
    if i == 5:
        continue
    print(i)

# Looping Through Data Structures
# ✅ List
nums =[10,20,30]
for i in nums:
    print(i)

#✅ Dictionary
user = {"name": "Maharshi", "age": 20}

for key, value in user.items():
       print(key, value)
# 👉 Real-world:

# JSON processing
# API data handling

#Nested loop
for i in range(3):
    for j in range(2):
        print(i, j)
# 👉 Used in:

# Matrix operations
# Grid systems
# Games

# ❌ Infinite loop:
while True:
    print("Hello")   # never stops

# ✅ Fix:
# while True:
#     break

# 🧠 Industry Thinking

# Loops = data processing engine

# Every system:

# Reads data
# Loops through it
# Applies logic



