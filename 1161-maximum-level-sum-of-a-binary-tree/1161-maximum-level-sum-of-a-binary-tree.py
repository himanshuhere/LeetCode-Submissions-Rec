# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        q = deque([root])
        maxi = -math.inf
        ans = -1
        l = 1
        
        while q:
            cur = 0
            n = len(q)
            for _ in range(n):
                x = q.popleft()
                cur += x.val
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
                    
            if cur > maxi:
                maxi = cur
                ans = l
            l += 1
        return ans