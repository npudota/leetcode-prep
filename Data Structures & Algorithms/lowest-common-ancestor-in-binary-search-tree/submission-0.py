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

        def dfs(root, maxV, minV):

            if root.val <= maxV and root.val >= minV:
                return root
            
            if root.val > maxV:
                return dfs(root.left,maxV, minV)
            else:
                return dfs(root.right,maxV, minV)
        
        return dfs(root,maxV,minV)

       

        