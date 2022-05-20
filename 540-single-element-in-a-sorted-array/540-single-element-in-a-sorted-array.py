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
    
    
    #lets make solution considering that our left of mid is always correct thus only right side has the culprint(that single ele), just assume. So if left is fine now there are two cases if my mid index is first of two elements (like 4,4 and my mid is first 4) so imagine if every element appears twice in left side means always first occurent of duplicates will take even index like 0,2,4,6 and second occurance will always take odd indices like 1, 3, 5. so two case is
    #if a[mid]==a[mid-1], means our mid is at second occurence of duplicates and it should be odd index right,
    #similarly, if a[mid+1]==a[mid], means our mid is first one, so index should be even, if any of this condition met means left side is fine lets move to right one else left side is wrong and has the single elements (that ruined our even/odd index logic) so bhai chalo chalo pakdo bhen k lode ko left me hi hai bas