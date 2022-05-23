class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @lru_cache(None)
        def f(i, m, n):
            if m < 0 or n < 0:
                return -1
            if not m+n or i == len(strs):
                return 0
            
            return max(1 + f(i+1, m-strs[i].count('0'), n-strs[i].count('1')), f(i+1, m, n))
        
        return f(0, m, n)