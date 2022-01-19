class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # @lru_cache(None)    #dp
        # def f(i,j):
        #     if (i,j) == (m-1,n-1):
        #         return 1
        #     if i>=m or j>=n:
        #         return 0
        #     return f(i+1,j)+f(i,j+1)
        # return f(0,0)
        
        #2
        dp = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]
        return dp[m-1][n-1]
                