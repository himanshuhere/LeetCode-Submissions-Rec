class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #laready given adj list
        
        def dfs(node, path):
            if node == len(graph)-1:
                res.append(path+[node])
                return
            
            path+=[node]
            for k in graph[node]:
                dfs(k, path)
            path.pop()
            
        res = []
        vis = set()
        dfs(0, [])
        return res
                
                
            
            