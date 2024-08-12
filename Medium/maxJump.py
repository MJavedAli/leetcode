from typing import List


def jumpGame(nums: List[int]) -> bool:
    max_reach = 0  
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False  
        max_reach = max(max_reach, i + jump)  
        if max_reach >= len(nums) - 1:
            return True  
    
    return False   

def jumpGame2(nums: List[int]) -> int:
    if len(nums) <= 1:
        return 0
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])       
        if i == current_end:
            jumps += 1
            current_end = farthest    
        if current_end >= len(nums) - 1:
            break

    return jumps


nums = [2,3,0,1,4]
print(jumpGame2(nums))