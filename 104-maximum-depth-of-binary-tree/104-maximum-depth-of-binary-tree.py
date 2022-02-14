# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def f(root):
            if not root:    return 0
            return 1 + max(f(root.left), f(root.right))
        return f(root)
        
    
        #BFS
        if not root:
            return 0
        q = deque([[root, 1]])
        res = 0
        while q:
            for _ in range(len(q)):
                x, h = q.popleft()
                res = max(res, h)
                if x.left:
                    q.append([x.left, h+1])
                if x.right:
                    q.append([x.right, h+1])
        return res