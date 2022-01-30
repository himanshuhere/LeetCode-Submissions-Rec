class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n       #imp to focus, if k is more rotation than n
        nums[:] = nums[n-k:] + nums[:n-k]
        return nums
    
    #brute with o(n) extra
        # res = [None]*n
        # for i in range(n):
        #     res[i] = nums[(i+k)%n]
        # return res
        
        #best
#         for i in range(k):    #this will lead time limit
#             self.rotatebyone(nums)
#         return nums   
#     def rotatebyone(self, nums: List[int]) -> None:
#         last = nums[len(nums)-1]
#         for i in range(len(nums) - 2, -1, -1):
#             nums[i+1]=nums[i]
#         nums[0]= last