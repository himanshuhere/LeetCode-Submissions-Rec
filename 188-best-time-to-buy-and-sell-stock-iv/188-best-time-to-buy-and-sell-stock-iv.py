class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # b = [inf] * (k + 1)
        # s = [0] * (k + 1)
        # for p in prices:
        #     for k in range(1, k+1):
        #         b[k] = min(b[k], p - s[k-1])
        #         s[k] = max(s[k], p - b[k])
        # return s[-1]
        
        #just like 3rd
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
        #return dp(0, True, k)
    
    
        #Tabulation
        dp = [[[0]*(k+1) for _ in range(2)] for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(0, 2):
                dp[i][j][0] = 0
                
        for i in range(2):
            for j in range(0, k+1):
                dp[n][i][j] = 0
                
        for i in range(n-1, -1, -1):
            for j in range(0, 2):
                for cap in range(1, k+1):
                    profit = 0
                    if j:
                        profit = max(-prices[i] + dp[i+1][0][cap], 0 + dp[i+1][1][cap])  # Buy (take/not take)
                    else:
                        profit = max(prices[i] + dp[i+1][1][cap-1], dp[i+1][0][cap])                # Sell
                    dp[i][j][cap] = profit
        return dp[0][1][k]
    
    
        #space opt
        ahead = [[0]*3 for _ in range(2)]          #two variables
        cur = [[0]*3 for _ in range(2)] 
        for i in range(n-1, -1, -1):
            for j in range(0, 2):
                for cap in range(1, 3):
                    profit = 0
                    if j:
                        profit = max(-prices[i] + ahead[0][cap], 0 + ahead[1][cap])  # Buy (take/not take)
                    else:
                        profit = max(prices[i] + ahead[1][cap-1], ahead[0][cap])                # Sell
                    cur[j][cap] = profit
            ahead = cur.copy()
        return ahead[1][2]
    
    
    #if want 2 dp better use trans like thing means lets remove canbuy and cap two spaces and use once tran. so if will be like if tran == 4: return 0, and every time buy and sell(take case) happens you do tran += 1, and how can we determine canbuy using tran, simple if tran%2==0 you can buy else sell.