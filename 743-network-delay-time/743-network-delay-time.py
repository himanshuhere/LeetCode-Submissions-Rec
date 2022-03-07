class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #pls try dijktra
        
        dist = [float("inf") for _ in range(n)]
        dist[k-1] = 0
        
        for _ in range(n-1):
            for u, v, w in times:
                if dist[u-1] + w < dist[v-1]:
                    dist[v-1] = dist[u-1] + w
                    
        return max(dist) if max(dist) < float("inf") else -1
        #ofc dijktra would be more nice if -ve weights are not here, i guess not. 