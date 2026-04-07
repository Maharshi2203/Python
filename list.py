nums = [45,70,80,55,38]
print(nums[0]) #[45]
print(nums[2:4]) #[80,55]

names = ['max','jack','magoto','sky']
print(names[0])# max

mix=[[45,70,80,55,38],['max','jack','magoto','sky']]
print(mix[0]) #[45,70,80,55,38]

print(mix[0][2]) #80
print(mix[1][3]) #sky

mix= nums + names
print(mix)

nums.append(33)
print(nums)#[45, 70, 80, 55, 38, 33]

nums.insert(2,10)
print(nums)#[45, 70, 10, 80, 55, 38, 33]

nums.remove(38)
print(nums)#[45, 70, 10, 80, 55, 33]

nums.pop(4)
print(nums)#[45, 70, 10, 80, 33]

del nums[2:4]
print(nums)#[45, 70, 33]

nums.extend([23,46,78])
print(nums)#[45, 70, 33, 23, 46, 78]

nums[2:4] = [54,55]
print(nums)#[45, 70, 54, 55, 46, 78]

nums.reverse()
print(nums)#[78, 46, 55, 54, 70, 45]

nums.sort()
print(nums)