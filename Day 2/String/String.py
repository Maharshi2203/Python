# 🧠 1. What is a String?

# A string is just text data.

name = "Maharshi"

# 👉 Used in:

# usernames
# passwords
# messages
# API data

#Accessing Characters
print(name[0]) # M
print(name[1]) # a

#🔁 3. Loop Through String
for char in "Maharshi":
    print(char)

# 👉 Used in:

# password checks
# parsing input

#⚡ 4. Important String Methods
#1.Lower/upper
print(name.lower()) #maharshi
print(name.upper()) #MAHARSHI
# 👉 Use:

# login systems (case-insensitive)

#2.Strip (remove spaces)
text=" hello "
print(text.strip())
# 👉 Use:
# cleaning user input

#3.Split
data = "apple,mango,banana"
fruits = data.split(",")

print(fruits) #['apple', 'mango', 'banana']
#👉 Used in:
# CSV
# APIs
# parsing data

#4 Replace
text = "Hello World"
print(text.replace("World","Maharshi")) #Hello Maharshi

#5.Find
text = "Hello"
print(text.find("e")) #1

#String Slicing
name = "Maharshi"
print(name[0:4]) #Maha
print(name[:4])  # Maha
print(name[4:])  # rshi

#   6. String + Conditions + Loops
text = "maharshi"

count = 0

for ch in text:
    if ch in "aeiou":
        count += 1

print("Vowels:", count)

#f-Strings (Industry Standard)
name = "Maharshi"
age = 20

print(f"My name is {name} and I am {age}")

# 👉 Used in:

# logging
# APIs
# backend

# ⚠️ Common Mistakes

# ❌ Forgetting string is immutable

# name[0] = "X"   # ERROR

# ❌ Not cleaning input
# 👉 leads to bugs in real apps