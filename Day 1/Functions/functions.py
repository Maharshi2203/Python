# 🧠 1. What is a Function?

# A function is a reusable block of code.

# 👉 Think like industry:

# Instead of writing the same logic again and again
# You write it once → reuse everywhere

def greet():
    print("Hello")

greet()

# Function with Parameters
def greet(name):
    print("Hello", name)

greet("Maharshi") #Hello Maharshi

#return values
def add(a,b):
    return a+b

result = add(12,3)
print(result)#15


# Default Parameters
def greet(name="User"):
    print("Hello",name)

greet()
greet("Maharshi")

#Multiple Returns (Advanced Thinking)
def calc(a,b):
    return a+b,a-b #Hello Maharshi

sum_val,diff_val = calc(10,2)
print(sum_val,diff_val)# 12 8

#Function Inside Loop
def process_transaction(t):
    return t*2

transaction=[10,20,30]

for t in transaction:
    print(process_transaction(t))
# 👉 Used in:

# Data processing
# Pipelines
# APIs

# ⚠️ Common Mistakes

# ❌ Not using functions → messy code
# ❌ Using print instead of return
# ❌ Writing huge functions (bad practice)


# 🧠 Industry Rule

# 👉 One function = one responsibility

#Bad Approach ❌
# def everything():
#     # login + payment + print + save 

#Better Approach
def login(): pass
def process_payment(): pass
def save_data(): pass