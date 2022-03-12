class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        @lru_cache(None)
        def f(i, j):
            if i < 0:
                return j+1
            if j < 0:
                return i+1
            if s1[i] == s2[j]:
                return f(i-1, j-1)
            else:
                return 1 + min(f(i, j-1),
                               f(i-1, j),
                               f(i-1, j-1))
            
        m, n = len(s1), len(s2)
        return f(m-1, n-1)