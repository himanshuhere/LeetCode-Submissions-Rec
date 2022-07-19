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
    
    
        #2
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        
        deq = deque([(p, q)])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False         
            if p and q:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        return True