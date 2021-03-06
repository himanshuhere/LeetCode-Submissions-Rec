class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        def reversed(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
                
        n = len(nums)
        k = k%n
        
        reversed(0, n-1)        
        reversed(0, k-1)
        reversed(k, n-1)
        
        
        #nums = ----->---->      [1,2,3,4, 5,6,7]
        #nums = <----<-----      [7,6,5, 4,3,2,1]
        #nums = -----><-----     [5,6,7, 4,3,2,1]
        #nums = ---->---->       [5,6,7, 1,2,3,4]
        
        
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