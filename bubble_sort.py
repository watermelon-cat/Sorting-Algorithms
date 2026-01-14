nums = [1, 8, 4, 2, 5, 9, 6, 3, 7]
temp = 0

for k in range(len(nums)-1):
    for i in range(len(nums)-k-1):#-1 to not go over the list
        if nums[i] > nums[i+1]:
            temp = nums[i] #dont let num[0] get erased
            nums[i] = nums[i+1] #puts the 2nd slot into the 1st slot
            nums[i+1] = temp #puts the 1st slot into the 2nd slot

print(nums)
