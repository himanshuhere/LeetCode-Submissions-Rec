class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #DFS to clone. will use given graph to traverse over and keep creating deep copy parallely see
        
        if not node:
            return None
        
        #DFS
        def dfs(old):
            if old in old_to_copy:
                return old_to_copy[old]
            
            copy = Node(old.val)
            old_to_copy[old] = copy
            
            for nei in old.neighbors:
                old_to_copy[nei] = dfs(nei)
                copy.neighbors.append(old_to_copy[nei])
            
            return copy
        
        old_to_copy = {}
        return dfs(node)
                    