class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #wow just buy and sell on sec day whenever profit else do nothing bcs y to hold if next price is smaller
        #so just sell the same stock bought on same day and buy next one samller one
        #we ll buy that so technically this code covers all this
        
        #note: you can buy it then immediately sell it on the same day.
        
#         profit = 0
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i-1]:
#                 profit += prices[i]-prices[i-1]

#         return profit
    
        
        #dp
        n = len(prices)
        
        @lru_cache(None)
        def dp(i, canBuy):
            if i == n:
                return 0            #profit whether we have bought or sold on last day
            
            profit = 0
            if canBuy:
                profit = max(-prices[i] + dp(i+1, False), 0 + dp(i+1, True))  # Buy (take/not take)
            else:
                profit = max(prices[i] + dp(i+1, True), dp(i+1, False))                # Sell
            return profit
        return dp(0, True)