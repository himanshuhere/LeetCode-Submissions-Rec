# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root, cur):
            if not root:
                return
            if not root.left and not root.right:
                cur = cur*10 + root.val
                self.res += cur
                return
            
            helper(root.left, cur*10+root.val)
            helper(root.right, cur*10+root.val)
        
        self.res = 0
        helper(root, 0)
        return self.res