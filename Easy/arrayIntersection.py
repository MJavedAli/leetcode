from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
   res = []
   for i in nums1:
        if i in nums2:
            res.append(i)
            nums2.remove(i)
   return res


nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersect(nums1,nums2))
