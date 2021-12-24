class Solution:
    def numWays(self, s: int, n: int) -> int:
        #khud se kiya, ek bar me\U0001f622
        
        
        @lru_cache(None)
        def dp(s, i):
            if i<0 or i>=n:
                return 0
            if s==0:
                return 1 if i == 0 else 0

            return dp(s-1, i-1)+dp(s-1, i+1)+dp(s-1, i)

        return dp(s, 0)%int(1e9+7)