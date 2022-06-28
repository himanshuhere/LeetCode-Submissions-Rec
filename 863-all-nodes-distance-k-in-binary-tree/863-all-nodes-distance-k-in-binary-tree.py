class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        # dfs preorder traversal to map each node to its parent
        def get_parent(node, parent):
            if not node: 
                return
            hashmap[node] = parent
            get_parent(node.left, node)
            get_parent(node.right, node)
            
        
        def search(node, distance):
            if not node or node in visited: 
                return
            
            visited.add(node)
            
            if distance == K: 
                answer.append(node.val)
                return
                
            search(hashmap[node], distance+1)
            search(node.left, distance+1)
            search(node.right, distance+1)
                
        
        hashmap, answer, visited = {}, [], set()
        get_parent(root, None)      #parent to root is None
        search(target, 0)
        return answer