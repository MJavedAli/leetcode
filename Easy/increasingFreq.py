from collections import defaultdict
from typing import List

def frequencySort(nums: List[int]) -> List[int]:
    num_Map = defaultdict(int)
    for num in nums:
        num_Map[num] += 1
    
    sorted_nums = sorted(nums, key=lambda x: (num_Map[x], -x))
    
    return sorted_nums






nums = [1,1,2,2,2,3]
print(frequencySort(nums))
