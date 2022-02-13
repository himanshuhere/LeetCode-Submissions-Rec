class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dp(i, target):
            if i == len(nums):
                if target == 0: return 1
                return 0
            
            return dp(i+1, target+nums[i]) + dp(i+1, target-nums[i])
        
        return dp(0, target)
        
        #this i did, considering 01 knapsack that we have two choice for every ele that +/-, so whatevr not going to be target=0 will return 0 else 1.
        #This works, but aditya's logic is that we have assign half elements as +vs other half -ve
        #so tecnically it is s1-s2 as [1,2,3,2,3] so [+1,+2,+3] and [-2,-3] sp == [1,2,3] - [2,3]
        #so it is reduced to finding the number of subsets with diff as target
        # s1 - s2 = target, this and since s1+s2 = sum(arr) and cancelling eq will give us s1 = target(diff)+sum(arr)//2 , so just find out "count subsets with sum as target"
    #here target = s1 = target(diff)+sum(arr)//2
    
    #yes it gets reduced to s1-s2=target problem, on solvig the eq we get s1 = target+sum
        
        s1 = (sum(nums)+target)//2
        if target > sum(nums) or s1%2==1:
            return 0
        
        t = [[0 for _ in range(s1+1)] for _ in range(len(nums)+1) ]
        
        for i in range(len(nums)+1):
            for j in range(s1+1):
                if i==0 and j==0:   t[i][j] = 1
                elif i==0:  t[i][j] = 0
                elif j==0:  t[i][j] = 1
                elif nums[i-1] == 0:     #if zero in arr dont take it
                    t[i][j] = t[i-1][j]
                elif nums[i-1] <= j:
                    t[i][j] = t[i-1][j-nums[i-1]] + t[i-1][j]
                else:
                    t[i][j] = t[i-1][j]
        
        cnt = nums.count(0)
        return t[-1][-1]*pow(2, cnt)