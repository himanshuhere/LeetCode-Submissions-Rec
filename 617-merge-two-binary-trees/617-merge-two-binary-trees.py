# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not r1 and not r2:
            return None
        if not r1 and r2:
            return r2
        if r1 and not r2:
            return r1
        
        #thus both val is there
        r1.val += r2.val
        r1.left = self.mergeTrees(r1.left, r2.left)
        r1.right = self.mergeTrees(r1.right, r2.right)
        
        return r1
    
    #2 pehle likhe the
        def dfs(r1, r2):
            if not r1 and not r2:
                return
            r1.val += r2.val
            
            if not r1.left and r2.left:
                r1.left = r2.left
                return
            if not r1.right and r2.right:
                r1.right = r2.right
                return
            
            dfs(r1.left, r2.left)
            dfs(r1.right, r2.right)
        
        dfs(root1, root2)
        return root1
            