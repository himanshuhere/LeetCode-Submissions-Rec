# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(root):
            if not root:
                return math.inf
            
            if not root.left and not root.right:        #this is very imp, as leaf will return inf from both side thus min will be inf only and will pass to higher level uptp the root
                return 1
            
            l, r = dfs(root.left), dfs(root.right)
            return 1 + min(l, r)
        
        return dfs(root)