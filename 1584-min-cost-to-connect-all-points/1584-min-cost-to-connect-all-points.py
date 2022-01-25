class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #there is kruskal algo in notes for this problem
        #lets create every edges from every points with calculated distance
        g = defaultdict(list)
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                g[i].append([dist, j])
                g[j].append([dist, i])
        #edges done
        
        #Prim's
        vis = set()
        h = [(0,0)]  #minHeap, dist, start
        res = 0
        while len(vis) < n:
            cost, i = heapq.heappop(h)
            if i in vis:
                continue
            res += cost
            vis.add(i)
            for neiCost, nei in g[i]:
                if nei not in vis:
                    heapq.heappush(h, (neiCost, nei))
        return res
            
            