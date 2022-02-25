class Solution:
    def jump(self, nums: List[int]) -> int:
        #working but slow - worst o(n^2)
#         @lru_cache(None)
#         def f(i):
#             if i == len(nums)-1:
#                 return 0
            
#             jumps = nums[i]
#             ans = math.inf
#             for j in range(1, jumps+1):
#                 if (i+j) < len(nums):
#                     ans = min(ans, 1 + f(i+j))
#             return ans
#         return f(0)
        
    #working but slow - worst o(n^2)
        # dp = [0]*len(nums)
        # dp[-1] = 0
        # for i in range(len(nums)-2, -1, -1):
        #     jumps = nums[i]
        #     ans = math.inf
        #     for j in range(1, jumps+1):
        #         if (i+j) < len(nums):
        #             ans = min(ans, 1 + dp[i+j])
        #     dp[i] = ans
        # return dp[0]
        
        
        
        #Greedy fast
        
        jumps = 0
        l = r = 0   #window
        #because ques says it is sure u ll reach last index fo assume and do
        
        while r < len(nums)-1:  #not taking last as their we need to land not start
            farthest = -1
            for i in range(l, r+1):
                farthest = max(farthest, i+nums[i]) #find the max far in widnow
            
            l = r + 1
            r = farthest
            jumps += 1
         
        return jumps
    
    #it io(n) see while+for
            