class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        p = 1
        ans = 0
        while j < len(nums):
            p *= nums[j]
            
            while i < len(nums) and p >= k:
                p //= nums[i]
                i += 1
                
            ans += (j-i+1)  #i could cross j and results in -ve lenght
            j += 1
            
        return ans if ans >= 0 else 0