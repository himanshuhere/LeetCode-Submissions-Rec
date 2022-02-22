# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #here all values are +ve, thus 1+l+r always be bigger than 1+max(l,r), if -ves also make sure to capture max(1+l+r, 1+max(l,r), alreadyCapturedAns) -greedy
        
        def dfs(root):
            #base condition
            if not root:
                return 0
            
            #hypothesis
            l = dfs(root.left)
            r = dfs(root.right)
            
            #Induction/calc
            self.res = max(self.res, l + r) #keep updating max diameter, here in LC edges counts thus l+r else for nodes it is 1+l+r, make sure to be clear wthis
            return 1 + max(l, r)        
        
        self.res = 0
        dfs(root)
        return self.res
    
    
    
    #
#     def dfs(root):
#             if not root:
#                 return 0   
#             return 1 + max(l, r)   
#this is height code, we fill height to every node while coming back from recursion, at that time since we wud have heights, we can smartly calculate diamter and can capture it. will save time o(n) else o(n^2)