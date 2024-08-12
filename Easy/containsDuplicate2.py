from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    num_map = {}
    for i in range(len(nums)):
        if nums[i] in num_map:
            if (i - num_map[nums[i]]) <= k:
                return True
        num_map[nums[i]] = i
    return False



nums = [1,2,3,1,2,3]
k = 2

print(containsNearbyDuplicate(nums,k))