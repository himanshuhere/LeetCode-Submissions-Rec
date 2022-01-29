class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        #we ll do modified dijktra, will keep ways array with dist like kept parent array will dist in ques where asked to return the shortest path too, yes. see
        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append([v, w])
            adj[v].append([u, w])
        
        mod = int(1e9+7)
            
        dist = [math.inf]*n
        ways = [0]*n
        
        h = [[0,0]]     #distance, start
        dist[0] = 0
        ways[0] = 1
        
        #destination is n-1, so do for all
        while h:
            d, node = heappop(h)
            for k, curdist  in adj[node]:
                if d + curdist < dist[k]:
                    dist[k] = d + curdist
                    heappush(h, ([dist[k], k]))
                    ways[k] = ways[node]
                    
                elif d + curdist == dist[k]:
                    ways[k] = ways[k] + ways[node]
                    
        return ways[-1]%mod