# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maxsum = float('-inf')

        def dfs(node):
            nonlocal maxsum

            if not node:
                return 0
            
            left_max = dfs(node.left)
            right_max = dfs(node.right)

            left_max = max(left_max, 0)
            right_max = max(right_max, 0)

            maxsum = max(maxsum, left_max + node.val + right_max)

            return max(left_max + node.val, node.val + right_max)
        
        dfs(root)
        return maxsum


            


        