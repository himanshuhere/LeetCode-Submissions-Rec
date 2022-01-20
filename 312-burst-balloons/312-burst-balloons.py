class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #MCM - Classic MCM
        
        @lru_cache(None)
        def mcm(i, j):
            if i > j:
                return 0
            
            coins = 0
            for k in range(i, j):       #i to j-1
                tmp = mcm(i, k) + mcm(k+1, j) + (nums[i-1]*nums[k]*nums[j])
                coins = max(coins, tmp)
            
            return coins
        
        nums = [1] + nums + [1]
        return mcm(1, len(nums)-1)      #for loop range is till j-1 so j wud be left for multipication
    
    #1. 3 1 5 8 .1