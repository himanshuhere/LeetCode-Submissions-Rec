# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, minv, maxv):
            if not root:
                return True
            if root.val >= maxv or root.val <= minv:
                return False
            
            return helper(root.left, minv, root.val) and helper(root.right, root.val, maxv)
        
        return helper(root, float('-inf'), float('inf'))
        