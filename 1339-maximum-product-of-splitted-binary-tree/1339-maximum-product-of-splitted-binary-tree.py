# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal ans, rootSum
            if not root:
                return 0
            currSum = dfs(root.left) + dfs(root.right) + root.val
            ans = max(ans, currSum * (rootSum - currSum))
            return currSum

        ans, rootSum = 0, 0
        rootSum = dfs(root)  # Firstly, get total sum of all nodes in the Binary Tree
        dfs(root)       # Then dfs in post order to calculate sum of each subtree and its complement
        return ans%int(1e9+7)
        
        
    #same algo for graph see. same
        def dfs(node, par):
            subsum[node] = A[node]
            for child in graph[node]:   #yes adj list
                if child == par:    continue
                dfs(child, node)
                subsum[node] += subsum[child]
        n=len(A)+1
        subsum = [0]*n
        dfs(1)
        ans = 0
        for i in range(2, n):       #0 not counting, 1 is root leave it as we take i as we are cutting upper to i edge no no upper edge to root hence leave
            part1 = subsum[i]
            prt2 = subsum[1] - part1
            ans = max(ans, part*part2)
        return ans      
        
        
        
        
        
        
        
        
        
        