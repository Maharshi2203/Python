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