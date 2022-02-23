class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        #1. Brute Force: O(nlogn) ~ O(n^2)
        
        # 1.1 High level walk-through:
        # (Define return) Define a global var: self.numOfPaths in the main function.
        # (1st layer DFS) Use recursive traverse to go through each node (can be any order: pre, in, post all fine).
        # (2nd layer DFS) For each node, walk all paths. If a path sum equals to the target: self.numOfPaths += 1
        # Return result: return self.numOfPaths
        
        def dfs(node):
            if node is None:
                return 

            test(node, target)         # you can move the line to any order, here is pre-order
            dfs(node.left)
            dfs(node.right)

        def test(node, target):
            if node is None:
                return
            
            if node.val == target:          #at any node, not only leaf
                self.numOfPaths += 1        #The path does not need to start or end at the root or a leaf,                                                  but it must go downwards                 
            
            test(node.left, target-node.val)
            test(node.right, target-node.val)
        
        self.numOfPaths = 0
        # 1st layer DFS to go through each node
        dfs(root)
        return self.numOfPaths