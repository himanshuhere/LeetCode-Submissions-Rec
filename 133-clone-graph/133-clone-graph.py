class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #DFS to clone. will use given graph to traverse over and keep creating deep copy parallely see
        
        if not node:
            return None
        
        #Only Graph traversal + map
        #DFS
        def dfs(old):

            copy = Node(old.val)
            old_to_copy[old] = copy
            
            for nei in old.neighbors:
                if nei not in old_to_copy:              #has already created, maybe visiting second time     
                    old_to_copy[nei] = dfs(nei)
                copy.neighbors.append(old_to_copy[nei])

            return copy
        
        old_to_copy = {}
        return dfs(node)
                    
        #DFS - Why map? see visiting cost of graph is V+E, because vertices will be visisted once but due to some extra edges we might visit same node again, like 1-2, 3-2. 2 can be visisted twice. If in first visit we have already created copy of 2, next time we would not want to oerate on that again so map can be useful getting previosly stored copies.