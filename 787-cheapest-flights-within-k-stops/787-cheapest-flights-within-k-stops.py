class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    
        
        #bfs with pq
        graph = collections.defaultdict(list)
        for s, d, w in flights:
            graph[s].append((d, w))
            
        pq = [(0, src, K)]
        vis = [0] * n
        while pq:
            w, x, k = heapq.heappop(pq)
            if x == dst:
                return w
            if vis[x] > k:
                continue
            vis[x] = k
            for y, dw in graph[x]:
                heapq.heappush(pq, (w+dw, y, k-1))
        return -1