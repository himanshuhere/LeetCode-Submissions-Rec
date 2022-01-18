class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def dp(nums, i, j):
            #space optimized one-d dp
            prev2, prev = 0, 0
            for i in range(i, j):
                rob = nums[i] 
                if i > 1:
                    rob += prev2
                dontrob = prev
                cur = max(rob, dontrob)
                prev2 = prev
                prev = cur
            return prev
        
        if n == 1:
            return nums[0]
        return max(dp(nums, 1, n), dp(nums, 0, n-1))
    