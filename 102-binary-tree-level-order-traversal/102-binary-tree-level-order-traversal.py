# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        ans = []
        while q:
            temp = []
            for _ in range(len(q)):
                x = q.popleft()
                temp.append(x.val)
                if x.left:
                    q+=[x.left]
                if x.right:
                    q+=[x.right]
            ans.append(temp)
        return ans