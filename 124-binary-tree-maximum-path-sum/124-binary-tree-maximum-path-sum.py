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
            l = max(dfs(root.left), 0)
            r = max(dfs(root.right), 0)
            
            #Induction
            self.res = max(self.res, l + r + root.val)
            
            return max(l, r) + root.val  
            
        
        self.res = -math.inf
        dfs(root)
        return self.res
    
    
    #This problem follows the Binary Tree Path Sum pattern and shares the algorithmic logic with Tree Diameter. We can follow the same DFS approach. The only difference will be to ignore the paths with negative sums. Since we need to find the overall maximum sum, we should ignore any path which has an overall negative sum.
    #0 is making sure of any ndoe to any node thing, like kadane if normal way giving neg ans, leave and start a new beginning with 0. if not 0 it will give leaf to leaf ans. think and learn