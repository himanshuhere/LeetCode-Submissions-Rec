class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        #Brute 
#         self.ans = 0
#         def dfs(root, cur):
#             if not root:
#                 return
#             if not root.left and not root.right:
#                 cur += str(root.val)
#                 self.ans += int(cur, 2)
#                 return
#             cur += str(root.val)
#             dfs(root.left, cur)
#             dfs(root.right, cur)
        
#         dfs(root, "")
#         return self.ans
    
        #REAL SMOOTH SHIT - test, it works like really butter the binary thing 
        def dfs(root, sum_):
            if not root:
                return 0
            
            sum_ = sum_ * 2 + root.val          #works so good, try a test case
            
            if not root.left and not root.right:
                return sum_
            return dfs(root.left, sum_) + dfs(root.right, sum_)
        
        return dfs(root, 0)
        
    
                