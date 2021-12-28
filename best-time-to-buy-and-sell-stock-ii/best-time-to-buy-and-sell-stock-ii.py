class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #wow just buy and sell on sec day whenever profit else do nothing bcs y to hold if next price is smaller
        #so just sell the same stock bought on same day and buy next one samller one
        #we ll buy that so technically this code covers all this
        
        #note: you can buy it then immediately sell it on the same day.
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i]-prices[i-1]

        return profit