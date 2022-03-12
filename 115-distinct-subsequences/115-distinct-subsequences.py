class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #See carefully, it is count ways so base case 0/1 and all state calls
        #two string, keep an index on both
        m, n = len(s), len(t)
        
        @lru_cache(None)
        def f(i, j):
            if j >= n:
                return 1
            if i >= m:
                return 0

            
            if s[i] == t[j]:
                return f(i+1, j) + f(i+1, j+1)
            else:
                return f(i+1, j)
        
        return f(0, 0)