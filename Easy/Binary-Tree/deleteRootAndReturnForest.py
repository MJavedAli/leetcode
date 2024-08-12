from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        to_delete=set(to_delete)
        res_set=set([root])

        def dfs(node):
            if not node:
                return None
            res=node
            if node.val in to_delete:
                res=None
                res_set.discard(node)
                if node.left: res_set.add(node.left)
                if node.right: res_set.add(node.right)
            node.left=dfs(node.left)
            node.right = dfs(node.right)
            return res
        dfs(root)
        return list(res_set)

    




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

sol = Solution()
result = sol.delNodes(root,[3,5])
for node in result:
    print(node.val)
