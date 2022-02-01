class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = math.inf
        profit = 0
        for price in prices:
            mini = min(mini, price)
            profit = max(profit, price - mini)
        return profit
    
    #you cant sell on day1 so buying is only possibiliy
        buy = prices[0]
        pro = 0
        
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                pro = max(pro, prices[i]-buy)
        return pro