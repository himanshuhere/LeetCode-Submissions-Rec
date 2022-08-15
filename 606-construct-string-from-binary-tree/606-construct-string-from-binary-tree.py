# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(r):
            if not r:
                return ''
            if not r.left and not r.right:
                return str(r.val)
            if r.left and not r.right:
                return str(r.val) + '('+ dfs(r.left) + ')'
            if not r.left and r.right:
                return str(r.val) + '()('+ dfs(r.right) + ')'

            return str(r.val) + '('+ dfs(r.left) + ')(' + dfs(r.right) + ')'
        
        return dfs(root)