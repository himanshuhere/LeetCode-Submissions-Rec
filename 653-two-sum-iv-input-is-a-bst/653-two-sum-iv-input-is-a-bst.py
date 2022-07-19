# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        #easy cuz lot of ways to solve it in n space but interviewer will want h space bcs it uses binary property since its a binary tree so here
        self.sl, self.sr = [], []

        def createLeftItertor(root):
            while root:
                self.sl += [root]
                root = root.left
                
        def createRightItertor(root):
            while root:
                self.sr += [root]
                root = root.right

        def next() -> int:
            node = self.sl.pop()
            cur = node.right
            while cur:
                self.sl += [cur]
                cur = cur.left
            return node.val
        
        def prev() -> int:
            node = self.sr.pop()
            cur = node.left
            while cur:
                self.sr += [cur]
                cur = cur.right

            return node.val
        
        #time o(n), spcae o(h)
        createRightItertor(root)
        createLeftItertor(root)
        i = next()
        j = prev()
        
        while i<j:
            if i+j == k:    return True
            if i+j < k:
                i = next()
            else:
                j = prev()
        return False
        