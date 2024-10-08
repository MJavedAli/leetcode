# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        
        if not p or not q or p.val!=q.val:
            return False
        
        else:
            lsol = self.isSameTree(p.left,q.left)
            if lsol:
                return self.isSameTree(p.right,q.right)
            else:
                return False

