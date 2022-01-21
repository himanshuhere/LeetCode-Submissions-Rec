# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #here all values are +ve, thus 1+l+r always be bigger than 1+max(l,r), if -ves also make sure to capture max(1+l+r, 1+max(l,r), alreadyCapturedAns)
        
        def dfs(root):
            #base condition
            if not root:
                return 0
            
            #hypothesis
            l = dfs(root.left)
            r = dfs(root.right)
            
            #Induction/calc
            self.res = max(self.res, l + r) #if this root then,take ans in res and pass temp and see what recur has
            return 1 + max(l, r)        
        
        self.res = 0
        dfs(root)
        return self.res