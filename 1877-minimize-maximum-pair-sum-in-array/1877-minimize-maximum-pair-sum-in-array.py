class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        #sorting + two pointer
        ans = 0
        nums = sorted(nums)     #make sure to sort
        l, r = 0, len(nums)-1
        while l<r:
            ans = max(ans, nums[l]+nums[r])
            l+=1                #kayki bol rha max n/2 pairs and one ele only in one pair
            r-=1
        return ans