# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        #o(n) space
        def inorder(root, first):
            nonlocal i
            if not root:
                return
            inorder(root.left, first)
            if first:
                ino.append(root.val)
            else:
                if root.val != ino[i]:
                    root.val = ino[i]
                i += 1
            inorder(root.right, first)
        
        ino = []
        inorder(root, True)
        ino.sort()
        
        i = 0
        inorder(root, False)
        return root
        
        
        
        #o(1) space
        #o(n) stack space not o(h) for that do morris inorder traversal if u know4
        
        self.first = self.second = self.last = None
        self.prev = TreeNode(float('-inf'))
        
        def inorder(root):
            if not root:    return 
            inorder(root.left)
            
            #business
            if self.prev and root.val < self.prev.val:
                #first violation
                if not self.first:
                    self.first, self.second = self.prev, root
                #second violation
                else:  
                    self.last = root
            
            self.prev = root
            inorder(root.right)
        
        
        inorder(root)

        #now swaps
        if self.first and self.last:
            self.first.val, self.last.val = self.last.val, self.first.val
        elif self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val