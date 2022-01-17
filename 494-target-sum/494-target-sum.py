class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dp(i, target):
            if i == len(nums):
                if target == 0: return 1
                return 0
            
            return dp(i+1, target+nums[i]) + dp(i+1, target-nums[i])
        
        return dp(0, target)
        
        