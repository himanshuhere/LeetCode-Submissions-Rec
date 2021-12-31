class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        #Brute force - some at node now go back to all its ancestor and check update res, o(n^2), same idea will keep passing values for which we are supposed to climb upto root and extra N traversal, better pass those values
        #For each subtree, find the minimum value and maximum value of its descendants.
        #pls see, kinda twisting to learn how did this operation
        #for every cur node, we ll see that whats the max and min value its ancestor got all the way to root
        #we need to pass the max and min to childs from root and update at every step, so child will use and update the result.
        
        def dfs(root, curmax, curmin):
            if not root:
                return
            
            ans = max(abs(root.val-curmax), abs(root.val-curmin))
            self.res = max(self.res, ans)
            
            dfs(root.left, max(curmax, root.val), min(curmin, root.val))
            dfs(root.right, max(curmax, root.val), min(curmin, root.val))
            
        self.res = 0
        dfs(root, root.val, root.val)
        return self.res