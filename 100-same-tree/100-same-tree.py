# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(p, q):
            if not p or not q:
                return p == q
            if p.val != q.val:
                return False
            return helper(p.left, q.left) and helper(p.right, q.right)
    
        #return helper(p, q)
    
    
        #2 - use bfs with queue or stack - same as both will procees same flow on trees
        stack = [(p, q)]
        while stack:
            l, r = stack.pop()
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            stack.append((l.left, r.left))
            stack.append((l.right, r.right))
        return True