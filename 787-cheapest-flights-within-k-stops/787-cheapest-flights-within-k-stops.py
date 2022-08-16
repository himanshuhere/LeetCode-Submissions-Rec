class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    
        
        #bfs with pq
        graph = collections.defaultdict(list)
        for s, d, w in flights:
            graph[s].append((d, w))
            
        pq = [(0, src, 0)]
        vis = [K] * n
        vis[src] = 1
        
        while pq:
            w, x, stops = heapq.heappop(pq)
            if x == dst:
                return w
            if vis[x] < stops:
                continue
            vis[x] = stops
            for y, dw in graph[x]:
                heapq.heappush(pq, (w+dw, y, stops+1))
        return -1