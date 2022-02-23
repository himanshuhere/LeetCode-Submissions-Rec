class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        p = 1
        ans = 0
        while j < len(nums):
            p *= nums[j]
            
            while i <= j and p >= k:
                p //= nums[i]
                i += 1
                
            ans += (j-i+1) 
            j += 1
            
        return ans 