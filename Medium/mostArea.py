from typing import List


def maxArea(height: List[int]) -> int:
    maxArea=0
    right = len(height)-1
    left =0

    while left < right:
        currentArea = min(height[left],height[right])*right-left
        maxArea = max(maxArea,currentArea)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        left+=1
        right-=1
    return maxArea


h1=[4,3,2,1,4]

print(maxArea(h1))