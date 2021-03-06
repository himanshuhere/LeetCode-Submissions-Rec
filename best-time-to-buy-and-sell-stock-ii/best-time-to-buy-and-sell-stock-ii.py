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
    
        
        n = len(prices)
        
        @lru_cache(None)
        def dp(i, canBuy):
            if i == n:
                return 0
            ans = dp(i+1, canBuy)  # Skip
            if canBuy:
                ans = max(ans, dp(i+1, False) - prices[i])  # Buy
            else:
                ans = max(ans, dp(i+1, True) + prices[i])  # Sell
            return ans
        
        return dp(0, True)