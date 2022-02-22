# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        ans = []
        
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
            ans.append(cur/n)
        return ans