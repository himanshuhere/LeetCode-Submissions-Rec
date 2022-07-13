class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #its a subset sum problem man
        #of sum/2 - odd - no
        #if sum/2 - even = yes/no
        if sum(nums)&1:
            return False
        
        s = sum(nums)//2
        #1
        @cache
        def f(i, s):
            if s == 0:
                return True
            if i == len(nums) or s < 0:
                return False
            return f(i+1, s-nums[i]) or f(i+1, s)
        
        return f(0, s)
    
        #2 to make tab 
        s = sum(nums)//2
        #1
        @cache
        def f(i, s):
            if s == 0:
                return True
            #if i == -1 or s < 0:
            if i == 0 or s < 0:
                return False
            if nums[i-1] <= s:          #i-1 for i
                return f(i-1, s-nums[i-1]) or f(i-1, s)
            else:
                return f(i-1, s)
        
        #return f(len(nums)-1, s)
        return f(len(nums), s)
    
        n = len(nums)
        tot = sum(nums)//2
        
        dp = [[False for _ in range(tot+1)] for _ in range(len(nums)+1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                
                if i==0 and j==0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = False
                elif j == 0:
                    dp[i][j] = True
                else:
                    if nums[i-1] <= j:
                        dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                    else:
                        dp[i][j] = dp[i-1][j]
                    
        return dp[-1][-1]
                
        