# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        #dfs
        def preorder(orig, clone):
            if not orig:
                return
            if orig is target:
                self.ans = clone
            
            preorder(orig.left, clone.left)
            preorder(orig.right, clone.right)
        
        self.ans = None
        preorder(original, cloned)
        return self.ans