class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i, j = 0, 0
        sm, ans = 0, -math.inf
        while j < len(nums):
            sm += nums[j]
            if j-i+1 == k:
                ans = max(ans, sm/(j-i+1))
                sm -= nums[i]
                i+=1
            j+=1
        return ans