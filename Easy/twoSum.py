from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    numMap={}
    n=len(nums)
    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement],i]
        numMap[nums[i]] = i
    return []
    



nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))