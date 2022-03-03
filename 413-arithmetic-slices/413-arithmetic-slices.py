class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        dp = [0]*n
        #base case setting
        if nums[1]-nums[0] == nums[2]-nums[1]:
            dp[2] = 1
        
        for i in range(3, n):
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                dp[i] = dp[i-1] + 1
        return sum(dp)
        
    #short optimized
        res= 0
        for i in range(2, n):
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                dp[i] = dp[i-1] + 1
            res+=dp[i]
        return res
        
    #more optimized
        res= 0
        prev=0
        for i in range(2, n):
            cur=0
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                cur = prev+1
            res+=cur
            prev=cur
        return res
    
    
    #dp[i] is the number of valid arithmetic seq till nums[i]. 
    #so if till i-1, seq were dp[i-1], then as per condition if we found one more, so add one more.
    
    #Let dp[i] denote the number of arithmetic subarray ends at nums[i].
# If if nums[i-1] - nums[i-2] == nums[i] - nums[i-1] then we can form the Arithmetic subarray ends at nums[i].
# So dp[i] = dp[i-1] + 1.
# For example: nums = [1, 3, 5, 7, 9]
# dp[2] = 1 arithmetic subarrays are {1, 3, 5}
# dp[3] = dp[2] + 1 = 2, arithmetic subarrays are {1, 3, 5, 7}, {3, 5, 7}
# dp[4] = dp[3] + 1 = 3, arithmetic subarrays are {1, 3, 5, 7, 9}, {3, 5, 7, 9}, {5, 7, 9}