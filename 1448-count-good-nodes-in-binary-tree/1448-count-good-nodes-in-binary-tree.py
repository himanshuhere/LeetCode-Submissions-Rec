#Did in one shot. Backtracking actually

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0 
        
        def dfs(root, pathmax):
            nonlocal ans
            if not root:
                return 
            
            if root.val >= pathmax:
                ans += 1
            
            prepathmax = pathmax
            dfs(root.left, max(pathmax, root.val))
            pathmax = prepathmax
            
            prepathmax = pathmax
            dfs(root.right, max(pathmax, root.val))
            pathmax = prepathmax
        
        dfs(root, -inf)
        return ans
            