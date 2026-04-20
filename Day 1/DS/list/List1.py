# 👉 What is a List?

# A list stores multiple values in one variable.

nums = [10, 20, 30]
print(nums[0])   # 10
print(nums[1])   # 20

#Add element
nums.append(40)
print(nums) #[10, 20, 30, 40]

#Remove element
nums.remove(20)
print(nums) #[10, 30, 40]

#Length
print(len(nums))

# 👉 Used in real world:

# Expense tracker
# Banking apps
# Logs

# Loop Through List

transactions = [1000, -200, 500]
for t in transactions:
     print(t)

