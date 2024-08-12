def removeDuplicates(nums):
    if not nums:
        return 0
    
    i = 0
    for j in range(1,len(nums)):
        if nums[j]!=nums[i]:
            i+=1
            nums[i]=nums[j]
    return i+1
    # unique_elements = set()
    # k = 0  
    # for num in nums:
    #     if num not in unique_elements:
    #         unique_elements.add(num)
    #         nums[k] = num
    #         k += 1
    
    # return k


nums = [0,0,1,1,1,2,2,3,3,4]
k=removeDuplicates(nums)
print(k)
print(nums[:k])


