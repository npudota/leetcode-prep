# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        maxV = max(p.val, q.val)
        minV = min(p.val,q.val)

        while root:
            if minV <= root.val <= maxV:
                return root
            
            if root.val > maxV:
                root = root.left
            else:
                root = root.right
        
        return dfs(root)

       

        