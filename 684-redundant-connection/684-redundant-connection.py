class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        par = [i for i in range(n+1)]
        rank = [1]*(n+1)
        
        def find(n):
#             while par[n] != par[par[n]]:
#                 par[n] = par[par[n]]
#             return par[n]
            
            if par[n] == n:
                return par[n]
            return find(par[n])
        
        def union(a, b):
            p1, p2 = find(a), find(b)
            
            if p1 == p2:
                return False        #already connected
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u,v]