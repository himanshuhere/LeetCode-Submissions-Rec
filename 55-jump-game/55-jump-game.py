class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #TLE
#         @lru_cache(None)
#         def f(i):
#             if i == len(nums)-1:
#                 return True
            
#             jumps = nums[i]
#             for j in range(1, jumps+1):
#                 if (i+j) < len(nums) and f(i+j):
#                     return True
#             return False
#         return f(0)
    
        # dp = [False]*len(nums)
        # dp[-1] = True
        # for i in range(len(nums)-2, -1, -1):
        #     jumps = nums[i]
        #     for j in range(1, jumps+1):
        #         if (i+j) < len(nums) and dp[i+j]:
        #             dp[i] = True
        #             break
        # return dp[0]
        
        #this shit looking for something else that out of the box algo see, btw dp giving TLE
        #GREEDY
        last = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            #if with one or more jump, can i cross or land at last index if yes one sub prob solved
            if nums[i] + i >= last:
                last = i
                
        if last == 0:
            return True
        return False