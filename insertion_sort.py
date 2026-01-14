nums = [3, 5, 8, 1, 2, 7, 4, 6]

for i in range(1, len(nums)):
    #The key is the element we're looking at this iteration
    key = nums[i]

    #start comparing with the element just before the key
    prev = i - 1

    while prev >= 0 and key < nums[prev]:
        nums[prev + 1] = nums[prev] #swap the slot we're looking at with the one in front
        prev -= 1#decrement j
    #once out of the loop, place the key at after the last compared
    nums[prev + 1] = key

print(nums)
    
