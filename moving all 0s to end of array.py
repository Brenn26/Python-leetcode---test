#move all 0s to the end of the array while maintaining order of non 0 numbers and without creating a second array

nums = [0, 1, 0, 3, 12]

for i in range(0,len(nums)):
    if nums[i] == 0:
        nums.remove(0)
        nums.append(0)
        

print(nums)