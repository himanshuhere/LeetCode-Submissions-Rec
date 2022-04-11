class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling? , cooldwon state will always be right branch option. always draw a tree
        # If Buy -> i + 1
        # If Sell -> i + 2
        
        n = len(prices)
        
        @lru_cache(None)
        def dp(i, canBuy):
            if i >= n:          #this will be 
                return 0            #profit whether we have bought or sold on last day
            
            profit = 0
            if canBuy:
                profit = max(-prices[i] + dp(i+1, False), 0 + dp(i+1, True))  # Buy (take/not take)
            else:
                profit = max(prices[i] + dp(i+2, True), dp(i+1, False))                # Sell
            return profit
        return dp(0, True)
    
    
    
        #Tabulation
        dp = [[0]*2 for _ in range(n+1)]
        dp[n][0] = dp[n][1] = 0
        for i in range(n-1, -1, -1):
            for j in range(0, 2):
                profit = 0
                if j:
                    profit = max(-prices[i] + dp[i+1][0], 0 + dp[i+1][1])  # Buy (take/not take)
                else:
                    profit = max(prices[i] + dp[i+1][1], dp[i+1][0])                # Sell
                dp[i][j] = profit
        #return dp[0][1]
    
        #space opt
        ahead = [0]*2           #two variables
        cur = [0]*2
        for i in range(n-1, -1, -1):
            for j in range(0, 2):
                profit = 0
                if j:
                    profit = max(-prices[i] + ahead[0], 0 + ahead[1])  # Buy (take/not take)
                else:
                    profit = max(prices[i] + ahead[1], ahead[0])                # Sell
                cur[j] = profit
            ahead = cur.copy()
        return ahead[1]
        
        
        #But greedy is better as you can do any num of transaction better keep checking if today > yest better count this profit. thats all