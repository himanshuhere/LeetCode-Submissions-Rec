class Solution:
    def minimumCardPickup(self, s: List[int]) -> int:
        #variable sliding window, k not given but see, instead of len(map) you can use count logic you know right
        map_ = defaultdict(int)
        ans = math.inf
        start = -1
        
        for j in range(len(s)):
            if s[j] in map_:
                start = map_[s[j]]
                ans = min(ans, j-start+1)
            map_[s[j]] = j
            
        return ans if ans!=math.inf else -1
            