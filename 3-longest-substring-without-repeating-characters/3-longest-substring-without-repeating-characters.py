class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #variable sliding window, k not given but see, instead of len(map) you can use count logic you know right
        i, j = 0, 0
        map_ = defaultdict(int)
        len_ = 0
        ans = 0
        count = 0
        
        while j < len(s):
            map_[s[j]] += 1
            if map_[s[j]] == 1:
                len_ += 1
            
            while len_ < j-i+1:
                map_[s[i]] -= 1
                if map_[s[i]] == 0:
                    len_ -= 1
                    del map_[s[i]]
                i += 1
                    
            ans = max(ans, j-i+1)                
            j += 1
        return ans
            