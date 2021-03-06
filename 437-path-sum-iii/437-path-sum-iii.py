class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
    #BRUTE Force: O(nlogn) ~ O(n^2)
        def brute():    
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
                    self.numOfPaths += 1
                                      #The path does not need to start or end at the root or a leaf,    but it must go downwards, return mt marna aage b path ho sakte h same line me(val -ve +ve hai) inhi baato ko toh dhyan rakhna hai                 

                test(node.left, target-node.val)
                test(node.right, target-node.val)

            self.numOfPaths = 0
            # 1st layer DFS to go through each node
            dfs(root)
            return self.numOfPaths
        
            #this is any to any (root to leaf, root to any, any to leaf, any to any)
            #positives value me we can write return after operation (if not leaf node) but negatives me nahi thats y see on line 24 we dot have any return. ans is possible keep going
        
        def memoized():
            #same as subarray sum to target k
            #there we memoized sum as sum[i:j] = sum[0:j] - su[0:i], count all frequence bcs negatives
            
            def dfs(root, curPathsum):
                if not root:
                    return 
                
                curPathsum += root.val
                if curPathsum - target in self.m:
                    self.count += self.m[curPathsum - target]
                self.m[curPathsum] += 1
                
                dfs(root.left, curPathsum)
                dfs(root.right, curPathsum)
                
                self.m[curPathsum] -= 1             #backtrack
                
            dfs(root, 0)
        
        self.m, self.count = defaultdict(int), 0
        self.m[0] = 1               #this is imp, as root to cur node path needs 1 as count
        memoized()
        return self.count
            
                    