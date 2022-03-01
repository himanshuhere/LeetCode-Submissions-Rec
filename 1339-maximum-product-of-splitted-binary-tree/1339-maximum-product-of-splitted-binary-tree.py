# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = []
        def dfs(node):
            if node is None:
                return 0
            subtree_sum = dfs(node.left) + dfs(node.right) + node.val
            sums.append(subtree_sum)
            return subtree_sum
        
        m = 0
        total = dfs(root)
        for i in range(len(sums)):
            prod = sums[i] * (total-sums[i])
            if prod > m: 
                m = prod
        
        return m % int(1e9+7)
    
    #why sums[0] is not roots sum like graph, becsue its a tree sums array gets filled starting with leaf nodes so at 0th index you might get sum of any leaf nodes. Take care of binary tree thses things. Althought edge cut thing will work as we are checking of all nodes without checking for any order
        
        
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
        
        
        
        
        
        
        
        
        
        