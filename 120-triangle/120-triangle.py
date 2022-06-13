class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 2
        # 3 4
        # 6 5 7
        # 4 1 8 3
        #technically there ll always be j and j+1 so no base boundary case for j but for i only
        @lru_cache(None)
        def f(i, j):
            if i == len(triangle)-1:
                return triangle[i][j]
            
            return triangle[i][j] + min(f(i+1, j) , f(i+1, j+1))
        #return f(0,0)
        
        
        #2d tabulation
#         n = len(triangle)
#         dp = [[0]*(i+1) for i in range(n)]
        
#         for j in range(n):
#             dp[n-1][j] = triangle[n-1][j]
        
#         for i in range(n-2, -1, -1):
#             for j in range(len(dp[i])):
#                 dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
#         return dp[0][0]
    
    
        #1d since i=1 everytime
        n = len(triangle)
        dp = [0]*n
        for j in range(n):
            dp[j] = triangle[n-1][j]
            
        #print(dp)
        for i in range(n-2, -1, -1):
            cur = [0]*(i+1)
            for j in range(len(cur)):
                cur[j] = triangle[i][j] + min(dp[j], dp[j+1])
            dp = cur
        return dp[0]
        
        
        