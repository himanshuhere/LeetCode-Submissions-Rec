class Solution:
    def canJump(self, nums: List[int]) -> bool:
#         def fn(i):
#             if i > len(nums)-1:
#                 return False
#             if i == len(nums)-1:
#                 return True
#             if (i, nums[i]) in self.m:
#                 return self.m[(i, nums[i])]
            
#             for j in range(1, nums[i]+1):
#                 if fn(i+j):
#                     self.m[(i, nums[i])] = True
#                     return True
#             self.m[(i, nums[i])] = False
#             return False
        
#         self.m = {}  
#         return fn(0)

#this shit looking for something else that out of the box algo see, btw dp giving TLE
        last = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            #if with one or more jump, can i cross or land at last index if yes one sub prob solved
            if nums[i] + i >= last:
                last = i
                
        if last == 0:
            return True
        return False