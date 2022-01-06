class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        result.append(self.getfirstposition(nums, target))
        result.append(self.getlastposition(nums, target))
        return result
        
    def getfirstposition(self, nums, target):
        index = -1
        low = 0 
        high = len(nums) - 1
        while low <= high:
            midposition = low + (high-low)//2
            if nums[midposition] == target:
                index = midposition
            #we cant do it else if. after finding we have idnex then we wll check on left side
            if nums[midposition] >= target:     ####
                high = midposition - 1
            else:
                low = midposition + 1
        return index
    
    
    def getlastposition(self, nums, target):
        index = -1
        low = 0 
        high = len(nums) - 1
        while low <= high:
            midposition = low + (high-low)//2
            if nums[midposition] == target:
                index = midposition
            #we cant do it else if. after finding we have idnex then we wll check on left side
  
            if nums[midposition] <= target:      ###
                low = midposition + 1
            else:
                high = midposition - 1
        return index
        