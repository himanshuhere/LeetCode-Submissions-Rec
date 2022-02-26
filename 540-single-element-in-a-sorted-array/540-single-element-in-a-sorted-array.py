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
    
    #Logic is simple.
    #if pair is available in array like 1,1 so every pairs first ele will be at even index and second at odd index. If any of the culprit is present in between this pattern will break.
    #we just need to check if patter holds then left side list is good go on right
    #else goon left
    #just check = if mid is even and duplicate is on right good or if mid is odd dupicate is in left fine. move right
    #else move left