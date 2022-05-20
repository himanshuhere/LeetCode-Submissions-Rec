class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:
        m,n = len(A), len(A[0])
        
        @lru_cache(None)    #dp
        def f(i,j):
            if i>=m or j>=n or A[i][j] == 1:
                return 0
            if (i,j) == (m-1,n-1):
                return 1
            return f(i+1,j)+f(i,j+1)
        #return f(0,0)
        
        #2
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if A[i][j] == 0:
                    if i==m-1 and j==n-1:
                        dp[i][j] = 1
                    elif i == m-1:
                        dp[i][j] = dp[i][j+1]
                    elif j == n-1:
                        dp[i][j] = dp[i+1][j]
                    else:
                        dp[i][j] = dp[i+1][j] + dp[i][j+1]
            
        return dp[0][0]
                