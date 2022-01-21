# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0
            l, r = max(dfs(root.left), 0), max(dfs(root.right), 0)
            
            #Induction
            self.res = max(self.res, l + r + root.val)
            return root.val + max(l, r)
        
        self.res = -math.inf
        dfs(root)
        return self.res