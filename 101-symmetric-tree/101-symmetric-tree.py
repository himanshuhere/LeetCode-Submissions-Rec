# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSym(l, r):
            if not l or not r:
                return l == r
            if l.val != r.val:
                return False
            return isSym(l.left, r.right) and isSym(l.right, r.left)
        #return not root or isSym(root.left, root.right)
    
        
        
        
        
        #2 iter
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            l, r = stack.pop()
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
        return True