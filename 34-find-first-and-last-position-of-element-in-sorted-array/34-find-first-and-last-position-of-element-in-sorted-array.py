class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        #smart
        lo, hi = 0, len(nums)-1
    
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        
        if nums[lo] != target:      #not even one elements present, to kayka left right
            return [-1, -1]
        
        ans = [lo]
        
        hi = len(nums)-1        #now dont need to reset lo
        
        while lo < hi:
            mid = lo + (hi - lo) // 2 + 1       #mid biased to right
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid
        ans.append(hi)
        
        return ans
        
#         result = []
#         result.append(self.getfirstposition(nums, target))
#         result.append(self.getlastposition(nums, target))
#         return result
        
#     def getfirstposition(self, nums, target):
#         index = -1
#         low = 0 
#         high = len(nums) - 1
#         while low <= high:
#             midposition = low + (high-low)//2
#             if nums[midposition] == target:
#                 index = midposition
#             #we cant do it else if. after finding we have idnex then we wll check on left side
#             if nums[midposition] >= target:     ####
#                 high = midposition - 1
#             else:
#                 low = midposition + 1
#         return index
    
    
#     def getlastposition(self, nums, target):
#         index = -1
#         low = 0 
#         high = len(nums) - 1
#         while low <= high:
#             midposition = low + (high-low)//2
#             if nums[midposition] == target:
#                 index = midposition
#             #we cant do it else if. after finding we have idnex then we wll check on left side
  
#             if nums[midposition] <= target:      ###
#                 low = midposition + 1
#             else:
#                 high = midposition - 1
#         return index
        