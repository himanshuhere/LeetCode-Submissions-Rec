class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @lru_cache(None)
        def dp(i, canBuy):
            
            if i >= len(prices):
                return 0
            
            cooldown = dp(i+1, canBuy)  # Skip
            
            if canBuy:
                ans = max(cooldown, dp(i+1, False) - prices[i] - fee)  # Buy
            else:
                ans = max(cooldown, dp(i+1, True) + prices[i])  # Sell
                
            return ans
                
        return dp(0, True)