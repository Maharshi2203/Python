# 🧠 1. Why File Handling?
# Until now, your data disappears when program stops.
# balance = 5000
# 👉 When program closes → data gone.
# File handling lets us:
# ✅ save data permanently
# ✅ load it later

# 📂 2. Opening a File
# ✅ Syntax
# file = open("data.txt", "r")

# 🔍 Modes (VERY IMPORTANT)
# Mode	Meaning
# "r"	Read
# "w"	Write (overwrite)
# "a"	Append
# "x"	Create new file

#Writing a file
file = open("data.txt","w")

file.write("Hello maharshi")

file.close()

# ⚠️ Important
# file.close()

# 👉 Always close file
# Otherwise:

# memory issues
# data corruption

# ✅ Better Way (Industry Standard)
# Use with

with open("data.txt","w") as file:
    file.write("Hello my name is Maharshi MehtaThe primary reason we use f-strings (formatted string literals) in Python is that they offer a more concise, readable, and efficient way to embed expressions and variables directly into strings.Introduced in Python 3.6 via PEP 498, they have largely replaced older methods like formatting and the .format() method as the industry standard.")

# 👉 Automatically closes file

# ✅ This is the industry standard.

# Reading File
with open("data.txt","r") as file:
    data=file.read()

print(data)


with open("data.txt","r") as file:
    for line in file:
        print(line)
# 👉 Used in:

# logs
# CSV files
# reports

#Append Data
with open("data.txt","a") as file:
    file.write("\n New Trasaction")

# 🧠 Why .strip()?
# Removes extra newline/spaces.

with open("transactions.txt", "r") as file:
    for line in file:
        print(line.strip())


# Common Mistakes
# Opening non-existing file in "r" mode
# open("abc.txt", "r")
# ERROR if file doesn’t exist.

#Safe Approach
# try:
#     with open("abc.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found")




