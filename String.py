print("Navin")

# print('Navin's telusko'); it will no work

print("Navin's telusko")
print('navin\'s "telusko"')

print('Navin '*10)

# print('c:\users\navin') it will give an error = SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
print('c:\\users\\navin')

print('Navin'' telusko') #concat

name = 'navin'
# print(name 'telusko') SyntaxError: invalid syntax

print(name+' telusko')#concat

text = 'Maharshi'
print(text)
print(text[0]) # M
# print(text[8]) # IndexError: string index out of range
print(text[-2]) # h

print(text[2:7]) #harsh
print(text[0:5]) # Mahar
print(text[4:]) # rshi
print(text[:6]) # Mahars

# text[0:3]='MAH'
# print(text) you cant change the existing string

print(len(text)) # 8

text1 = "Telusko" 
print(text1[-6:6]) #elusk