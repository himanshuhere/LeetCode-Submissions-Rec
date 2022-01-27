# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #to decide levels of nodes
#         def dfs(r):
#             if not r:
#                 return 0
#             l, r = dfs(r.left), dfs(r.right)
#             return max(l, r) + 1            #means leaf nodes is at level 1
        
        def dfs(r):
            if not r:
                return (r, 0)
            
            left, l_lev = dfs(r.left)
            right, r_lev = dfs(r.right)
            
            if l_lev == r_lev:
                return (r, l_lev + 1)
            if l_lev > r_lev:
                return (left, l_lev + 1)
            else:
                return (right, r_lev + 1)
        
        lca, lev = dfs(root)
        return lca