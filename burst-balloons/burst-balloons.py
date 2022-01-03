class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #Divide n Conq DP
        @lru_cache(None)
        def dp(l, r):
            if l > r:
                return 0
            if (l,r) in memo:
                return memo[(l,r)]
            
            tmp = 0
            for i in range(l, r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                tmp = max(tmp, dp(l, i-1) + coins + dp(i+1, r) )
            memo[(l,r)] = tmp
            return tmp
        
        memo = {}
        nums = [1] + nums + [1]
        return dp(1, len(nums) - 2)