# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
                #inorder isliye kuki sorted data me hi closesnt aspas honge aur ans k chances jada hai

#         def dfs(root):
#             if not root:
#                 return
#             dfs(root.left)
#             least.append(root.val)
#             dfs(root.right)
        
#         least = []
#         dfs(root)
#         mn = math.inf
#         for i in range(1, len(least)):
#             mn = min(mn, least[i]-least[i-1])
#         return mn
    
    
        def dfs(root):
            nonlocal pre, res
            if not root:
                return
            dfs(root.left)
            res = min(res, root.val-pre)
            pre = root.val
            dfs(root.right)
        
        pre, res = -math.inf, math.inf      #ye pre = -inf bahit imp tha bhaiya
        dfs(root)
        return res
                
            