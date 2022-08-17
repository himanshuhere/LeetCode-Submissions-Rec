class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #brute way to apply kadanes o(n) on array n times how? first 0 to n-1, then 1, n-1, 0 then 2 -n-1..1, till n times and update ans that will lead to o(n^2).
        #optimized
        #find max sub using kadanes assuiming ans in straight array
        #find another array if circular ans is possible - see notes for it sum(nums)-minSub
        #return max of both
        #one boundary condition, if all -ves algo will not work so for that return max(nums)
        
        mx = ans1 = nums[0]
        mn = ans2 = nums[0]
        total = nums[0]
        
        for i in range(1, len(nums)):
            mx = max(mx + nums[i], nums[i])
            ans1 = max(ans1, mx)
            
            mn = min(mn + nums[i], nums[i])
            ans2 = min(ans2, mn)
            
            total += nums[i]
        
        if total == ans2:   #if all negatives
            return ans1      #return max(nums)
        return max(ans1, total-ans2)
        
        