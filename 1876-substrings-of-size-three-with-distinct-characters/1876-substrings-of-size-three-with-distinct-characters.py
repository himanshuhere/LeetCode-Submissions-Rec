class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i, j = 0, 0
        m = defaultdict(int)
        ans, count = 0, 0
        while j < len(s):
            m[s[j]] += 1
            if m[s[j]] == 1:
                count += 1
            
            if j-i+1 == 3:
                if count == j-i+1:
                    ans+=1
                if s[i] in m:
                    m[s[i]] -= 1
                    if m[s[i]] == 0:
                        count -= 1
                i+=1
            j+=1
        return ans