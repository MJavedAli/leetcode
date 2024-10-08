# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        child = set()
        nodes = {}
        for p, c, left in  descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)
            if left:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]
            child.add(c)
        for d in descriptions:
            if d[0] not in child:
                return nodes[d[0]]
        return None       
    

solution = Solution()
root = solution.createBinaryTree([[1, 2, 1], [2, 3, 0], [3, 4, 1]])
print(root.val)