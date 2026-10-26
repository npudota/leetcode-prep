# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            if res == False:
                return False
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            difference = abs(left_height - right_height)
            if difference > 1:

                res = False
            
            return 1 + max(left_height, right_height)
        dfs(root)
        return res
        