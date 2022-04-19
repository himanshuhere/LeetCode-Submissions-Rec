# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        #o(n) space
#         def inorder(root, first):
#             nonlocal i
#             if not root:
#                 return
#             inorder(root.left, first)
#             if first:
#                 ino.append(root.val)
#             else:
#                 if root.val != ino[i]:
#                     root.val = ino[i]
#                 i += 1
#             inorder(root.right, first)
        
#         ino = []
#         inorder(root, True)
#         ino.sort()
        
#         i = 0
#         inorder(root, False)
#         return root
        
        
        
        #o(1) space
        #o(n) stack space not o(h) for that do morris inorder traversal if u know4
        
        f = s = None
        prev = None
        
        def inorder(root):
            nonlocal prev, f, s
            if not root:    
                return 
            inorder(root.left)
            
            #business
            if prev and root.val < prev.val:        #first time root would not go
                #first violation
                if not f:
                    f = prev
                #second violation
                s = root
            
            prev = root
            inorder(root.right)
        
        
        inorder(root)
        f.val, s.val = s.val, f.val