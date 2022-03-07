class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, src: int) -> int:
        #pls try dijktra
        g = defaultdict(list)
        for u, v, w in times:
            g[u].append((v, w))

        dist = [float("inf")]*(n+1)
        dist[src] = 0
        h = [(0, src)]
        while h:
            cost, u = heappop(h)
            for k, w in g[u]:
                if cost + w < dist[k]:
                    dist[k] = cost + w
                    heappush(h, (dist[k], k))
        
        return max(dist[1:]) if max(dist[1:]) < float("inf") else -1
    
        
#         dist = [float("inf") for _ in range(n)]
#         dist[k-1] = 0
        
#         for _ in range(n-1):
#             for u, v, w in times:
#                 if dist[u-1] + w < dist[v-1]:
#                     dist[v-1] = dist[u-1] + w
                    
#         return max(dist) if max(dist) < float("inf") else -1
#         #ofc dijktra would be more nice if -ve weights are not here, i guess not. 