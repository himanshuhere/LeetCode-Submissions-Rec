# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return False
            
            l, r = dfs(root.left), dfs(root.right)
            
            if not l:
                root.left = None
            if not r:
                root.right = None
                
            if root.val == 1 or l or r:
                return True
            
            return False
        
        def dfs2(root):
            if not root:
                return None
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
            if root.left or root.right or root.val == 1:
               return root
            else:
               return None
            
        return root if dfs(root) else None
                