from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:

    left = 0
    right = len(numbers)-1
    tempSum = 0
    
    while left < right:
        tempSum = numbers[left]+numbers[right]
        if tempSum==target:
            return [left+1,right+1]
        elif tempSum>target:
            right-=1
        else:
            left+=1
    return [-1,-1]




e1=[2,7,11,15]
t1=9
e2=[2,3,4]
t2=6

print(twoSum(e2,t2))