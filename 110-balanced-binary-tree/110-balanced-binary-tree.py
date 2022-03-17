# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def f(r):
            nonlocal ans
            if not ans:
                return -math.inf
            
            if not r:
                return 0
            l, r = f(r.left), f(r.right)
            if abs(l-r)>1:
                ans = False
            return 1 + max(l, r)
        
        ans = True
        f(root)
        return ans