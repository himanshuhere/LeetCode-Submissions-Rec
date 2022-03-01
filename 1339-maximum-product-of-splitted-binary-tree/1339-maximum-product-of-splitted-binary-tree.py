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
        
        
        
        
        
        
        #cutedge, delete edge
        #its a tree, will do dfs tree algo, nit need visited because tree not graph, only par is enough. grah has cycle to keep visited
        #no par needed actually its a tree we wont go back up
        
        def dfs(node):
            nonlocal n
            subsum[n] = node.val
            n += 1
            #for child in g[node] - not a graphbut binary tree only two poss childs
            if node.left:
                tmp = dfs(node.left)
                subsum[n] += tmp
            if node.right:
                tmp = dfs(node.right)
                subsum[n] += tmp
            return subsum[n]
        
        # n = len(root)
        subsum = [0]*1000000 #cant define its lenght
        n = 1
        tmp = dfs(root)
        ans = 0
        mod = int(1e9+7)
        for i in range(2, n+1):
            sub1 = subsum[i]
            sub2 = subsum[1] - sub1
            ans = max(ans, (sub1*sub2)%mod)
        return ans%mod
        