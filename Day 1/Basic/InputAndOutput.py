#Input and output
name = input("Enter your name: ")
#output : Enter your name : 

age = input("Enter your age: ")
# by this age will be store in string not in integer 

#so for that we have to do type conversion or type casting
age = int(input("Enter your age: "))
x = int("10")      # string → int
y = float("5.5")   # string → float
z = str(100)       # int → string

print("Hello") # Hello

name = "Maharshi"
age = 20

print("Name:", name, "Age:", age) # Name:Maharshi Age:20
print(f"Name: {name}, Age: {age}")# Name:Maharshi Age:20

age = input("Enter age: ")
print(age + 10)   # ERROR

age = int(input("Enter age: "))
print(age + 10) # if age = 20 then output = 30

age = input("Enter age: ")

if age.isdigit():
    age = int(age)
    print("Valid age")
else:
    print("Invalid input") 
# 👉 Used in:
# Forms
# APIs
# Payment systems
