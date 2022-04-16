# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #reverse inorder traversal
        sum_values = 0
    
        def dfs(root):
            nonlocal sum_values
            
            if not root:
                return None
            dfs(root.right)
            sum_values += root.val
            root.val = sum_values
            dfs(root.left)
            return root
        
        return dfs(root)