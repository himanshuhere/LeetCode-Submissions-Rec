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
#         dp = [math.inf]*len(nums)
#         dp[-1] = 0
#         for i in range(len(nums)-2, -1, -1):
#             jumps = nums[i]
#             ans = math.inf
#             for j in range(1, jumps+1):
#                 if (i+j) < len(nums):
#                     ans = min(ans, 1 + dp[i+j])
#             dp[i] = ans
#         return dp[0]
        
        
        
        #Greedy fast
        if len(nums) == 1:
            return 0
        
        steps = nums[0]
        jumps = 0
        maxReach = nums[0] + 0
        
        for i in range(1, len(nums)-1):     #because any number cant be 0, min 1
            steps -= 1
            maxReach = max(maxReach, i+nums[i])
            if steps == 0:
                steps = maxReach - i
                jumps += 1
        return jumps+1