class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @lru_cache(None)
        def f(i, m, n):
            if m < 0 or n < 0:
                return -1
            if (m==0 and n==0) or i == len(strs):  # at most m 0's and n 1's in the subset.
                return 0
            
            return max(1 + f(i+1, m-strs[i].count('0'), n-strs[i].count('1')), f(i+1, m, n))
        
        return f(0, m, n)
