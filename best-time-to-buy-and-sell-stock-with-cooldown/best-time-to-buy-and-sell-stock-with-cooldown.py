class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling? , cooldwon state will always be right branch option. always draw a tree
        # If Buy -> i + 1
        # If Sell -> i + 2
        
        @lru_cache(None)
        def helper(flag, ind):            
            if ind == len(prices):
                return 0
            if flag == 'cooldown': # we can either buy or skip buying
                return max(helper('bought',ind + 1)- prices[ind],  helper('cooldown',ind + 1))
            
            if flag == 'bought': # we can keep the stock or sell it
                return max(helper('bought',  ind + 1), helper('sold', ind + 1)+ prices[ind])
            
            if flag == 'sold': # we need to proceed to the next day
                return helper('cooldown', ind + 1)
        
        
        return helper('cooldown',  0)