class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # xor = 0
        # for n in nums:
        #     xor ^= n
        # return xor
        
        #o(logn)
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = lo + (hi - lo)//2
            if mid&1==0 and nums[mid]==nums[mid+1] or mid&1==1 and nums[mid]==nums[mid-1]:
                lo = mid+1
            else:
                hi = mid
        return nums[lo]