class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #DFS to close. will use given graph to traverse over and keep creating deep copy parallely see
        
        def dfsclone(old_node):
            if old_node in map_:            #if clone already done
                return map_[old_node]
            
            copy = Node(old_node.val)
            map_[old_node] = copy
            
            #now connect neigbours
            for nei in old_node.neighbors:
                copy.neighbors.append(dfsclone(nei))
            return copy
        
        map_ = {}
        return dfsclone(node) if node else None