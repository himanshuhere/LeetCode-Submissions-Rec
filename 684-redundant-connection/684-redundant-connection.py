class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #why union-find, because once n nodes are done connected with n-1 edges after that union will make sure to return false saying already is connnected somehow then that is redundant connection so return that. Actually there always will be one connected componect in  graph thats y union find is working. see lil trick and tweek
        n = len(edges)
        par = [i for i in range(n+1)]   #0th will not be used
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