class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #brute two loops and generate subarray and update res
        # Kadane's algorithm, O(n)
        res = cur = nums[0]
        for i in range(1, len(nums)):
            cur += nums[i]
            if nums[i] > cur:
                cur = nums[i]
            res = max(res, cur)
        return res