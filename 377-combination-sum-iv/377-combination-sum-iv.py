class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def f(i, t):
            if t==0:
                return 1
            if t < 0 or i == len(nums):
                return 0
            ans = 0
            for j in range(len(nums)):
                ans += f(j, t-nums[j])
            return ans
        
        return f(0, target)
        