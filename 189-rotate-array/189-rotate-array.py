class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        
        def reversed(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
                
        
        reversed(0, n-1)        
        reversed(0, k-1)
        reversed(k, n-1)
        
        
        
        # n = len(nums)
        # k = k % n       #imp to focus, if k is more rotation than n
        # nums[:] = nums[n-k:] + nums[:n-k]
        # return nums
    
       
        
        #best
#         for i in range(k):    #this will lead time limit
#             self.rotatebyone(nums)
#         return nums   
#     def rotatebyone(self, nums: List[int]) -> None:
#         last = nums[len(nums)-1]
#         for i in range(len(nums) - 2, -1, -1):
#             nums[i+1]=nums[i]
#         nums[0]= last