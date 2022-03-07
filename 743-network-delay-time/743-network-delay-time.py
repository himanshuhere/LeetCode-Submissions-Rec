class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, src: int) -> int:
        #Dijktra
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
    
        