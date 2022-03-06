class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 1_000_000_007
        
        #Top down
        #since pickeup has no constraints and first pickup and then deli is possible for N we have 2N spaces. so we ll pick one and go for delivery or pick three and go for delivery like open close brancket we have qes in backtrackng. Might be case then after one picku two deliveries gonne made, so wll take take with [to_deliver_yet > picked] to make a call for delivery.
        #ways 
        @lru_cache(None)
        def f(unpicked, undel):
            if unpicked == 0 and undel == 0:
                return 1
            if unpicked < 0 or undel < 0 or undel < unpicked:
                return 0
            
            ans = 0
            #if unpicked > 0:
            ans += unpicked*f(unpicked-1, undel)
            ans %= MOD
            
            #if undel > unpicked:
            ans += (undel - unpicked)*f(unpicked, undel-1)
            ans %= MOD
            
            return ans
    
        return f(n, n)
        
        #Tab
        dp = [[0] * (n + 1) for i in range(n + 1)]
        
        for unpicked in range(n + 1):
            for undelivered in range(0, n + 1):
                if unpicked > 0:
                    dp[unpicked][undelivered] += unpicked * dp[unpicked - 1][undelivered]
                dp[unpicked][undelivered] %= MOD
                
                if undelivered > unpicked:
                    dp[unpicked][undelivered] += (undelivered - unpicked) * dp[unpicked][undelivered - 1]
                dp[unpicked][undelivered] %= MOD
        
        return dp[n][n]
    