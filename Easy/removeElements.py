nums = [3,2,2,1]
val=2

def removeElement(nums, val):
    k=0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[k]=nums[i]
            k+=1
    return k        

removeElement(nums,val)
