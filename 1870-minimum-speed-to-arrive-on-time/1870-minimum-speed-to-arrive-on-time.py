class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def blackBox(s):
            h = 0
            for i in range(len(dist)-1):
                h += ceil(dist[i]/s)
            h += dist[-1]/s     #we dont need tp wait afte this, so optimizing out hours
            
            return h <= hour
        
        lo, hi = 1, 100000000           #10^7
        while lo < hi:
            mid = lo + (hi-lo)//2
            if(blackBox(mid)):
                hi = mid
            else:
                lo = mid + 1
        return lo if lo != 100000000 else -1
            