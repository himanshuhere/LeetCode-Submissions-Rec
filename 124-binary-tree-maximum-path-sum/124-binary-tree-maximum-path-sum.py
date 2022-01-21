# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #just like aditya diameter concept will lil focus on cases as HARD it is
        def dfs(root):
            if not root:
                return 0
            l, r = dfs(root.left), dfs(root.right)
            
            #Induction
            self.res = max(self.res, l + r + root.val)
            return max(root.val + max(l, r), 0)   
            #0 is making sure of any ndoe to any node thing, like kadane if normal way giving neg ans, leave and start a new beginning with 0. if not 0 it will give leaf to leaf ans. think and learn
        
        self.res = -math.inf
        dfs(root)
        return self.res