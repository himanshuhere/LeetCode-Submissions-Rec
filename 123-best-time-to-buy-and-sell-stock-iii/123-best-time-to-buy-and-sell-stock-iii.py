class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         buy1 = buy2 = 2**31-1
#         sell1p = sell2p = -2**31
        
#         for rate in prices:
#             buy1 = min(buy1, rate)          #whichevr minimum
#             sell1p = max(sell1p, rate-buy1)
            
#             buy2 = min(buy2, rate - sell1p) #u'r using first profit money to buy second stock
#             sell2p = max(sell2p, rate - buy2)
        
#         return sell2p
    
    
    #dp
        n = len(prices)
        
        @lru_cache(None)
        def dp(i, canBuy, cap):
            if cap == 0 or i == n:
                return 0            #profit whether we have bought or sold on last day
            
            profit = 0
            if canBuy:
                profit = max(-prices[i] + dp(i+1, False, cap), 0 + dp(i+1, True, cap))  # Buy (take/not take)
            else:
                profit = max(prices[i] + dp(i+1, True, cap-1), dp(i+1, False, cap))                # Sell
            return profit
        return dp(0, True, 2)
    
    
        #Tabulation
        dp = [[[0]*3 for _ in rage(2)] for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(0, 2):
                dp[i][j][0] = 0
                
        for i in range(2):
            for j in range(0, 3):
                dp[n][i][j] = 0
                
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