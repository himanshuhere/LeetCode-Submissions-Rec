# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        def dfs(root, target):
            if not root:
                return False
            
            if not root.left and not root.right:
                if root.val == target:
                    return True
            
            return dfs(root.left, target-root.val) or dfs(root.right, target-root.val)
            
        return dfs(root, target)