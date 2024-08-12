def majorityElement(nums):
    candidate = None
    count=0

    for num in nums:
        if count==0:
            candidate=num
        count+=(1 if num==candidate else -1)
        
    return candidate


nums=[2,2,3,3,3,3,2]
c=majorityElement(nums)
print(c)