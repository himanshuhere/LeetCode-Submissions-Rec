class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        #dfs
        n = len(graph)
        colored, vis = [None]*n, [0]*n
        
        def dfs(node, c):
            vis[node] = 1       #technically you can use colored as vis too, if none not visited. 
            colored[node] = c
            
            for k in graph[node]:
                if vis[k] == 0:
                    if dfs(k, c^1) == False:
                        return False
                else:       #visited, pehle se assigned color now check if right or not
                    if colored[k] == colored[node]:
                        return False
            return True
        
        for i in range(n):
            if vis[i] == 0:
                if not dfs(i, 0): 
                    return False
        return True
    
    
    #         #bfs
#         n, colored = len(graph), {}
        
#         for i in range(n):
#             if i not in colored:
#                 colored[i] = 0
#                 q = deque([i])
#                 while q:
#                     x = q.popleft()
                    
#                     for k in graph[x]:
#                         if k not in colored:
#                             colored[k] = 1-colored[x]
#                             q.append(k)
#                         elif colored[k] == colored[x]:
#                             return False
#         return True
        