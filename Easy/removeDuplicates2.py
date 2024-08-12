def removeDuplicates2(nums):
    if not nums:
        return 0
    
    j=0
    count=1
    
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]:
            count=count+1
        else:
            count=1
        if count<=2:
            j+=1
            nums[j]=nums[i]
    return j+1


nums = [0,0,1,1,1,1,2,3,3]
k=removeDuplicates2(nums)
print(k)
print(nums[:k])
