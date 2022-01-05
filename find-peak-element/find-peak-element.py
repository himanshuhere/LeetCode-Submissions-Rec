class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #Binary Search on answer - withoit sorted array
        if len(nums) == 1:  return 0
        
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            #edges
            if mid == 0 and nums[mid] > nums[mid + 1]:  return mid
            if mid == len(nums) - 1 and nums[mid] > nums[mid - 1]:  return mid   
            
            if nums[mid - 1] < nums[mid] > nums[mid + 1]: return mid        #accessing mid, thus TEMPlate 1
            
            elif nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1
                
                    