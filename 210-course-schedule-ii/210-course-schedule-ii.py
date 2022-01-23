class Solution:
    def findOrder(self, n: int, pr: List[List[int]]) -> List[int]:
        #Kahn's BFS Topo Algo - DFS is also easy to work on this, make sure to merge topo + detect cycle algo
        adj = collections.defaultdict(list)
        indegree = [0]*n
        q = []   
        
        for u,v in pr:
            adj[v].append(u)
            indegree[u] += 1
        
        for i in range(len(indegree)):   
            if indegree[i] == 0:
                q.append(i)
        
        c = 0
        while c < len(q):
            x = q[c]      
            c += 1
            for k in adj[x]:
                indegree[k] -= 1
                if indegree[k] == 0:
                    q.append(k)
                    
        return q if c==n else []
