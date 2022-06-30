class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        #median and average could be possible thinking, but median make more sense to balance of the array
        nums.sort()
        
        med = 0
        if len(nums)%2==0:
            med = (nums[len(nums)//2-1]+nums[len(nums)//2])//2
        else:
            med = nums[len(nums)//2]
        
        ans = 0
        for n in nums:
            ans += abs(n-med)
        return ans