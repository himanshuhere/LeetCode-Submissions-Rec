class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #Binary Search on answer - withoit sorted array
#         if len(nums) == 1:  return 0
        
#         lo, hi = 0, len(nums) - 1
#         while lo <= hi:
#             mid = lo + (hi - lo) // 2
            
#             #edges
#             if mid == 0 and nums[mid] > nums[mid + 1]:  return mid
#             if mid == len(nums) - 1 and nums[mid] > nums[mid - 1]:  return mid   
            
#             if nums[mid - 1] < nums[mid] > nums[mid + 1]: return mid        #accessing mid, thus TEMPlate 1
            
#             elif nums[mid] < nums[mid + 1]:
#                 lo = mid + 1
#             else:
#                 hi = mid - 1
#         return -1
                
        #2 Adv Template
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = lo + (hi-lo)//2
            if nums[mid] > nums[mid + 1]:
                hi = mid
            else:
                lo = mid + 1
        return lo
    
    #why this worked, advance temo bolke chale gye chutiye. isliye kuki if mid > mid+1, means mid can be ans but on what basis hum left me ja rhe esa kesa confidence bhiya, actually at that case it is proved that ans can be in left it can be in right or not maybe but pakka pakka lfet me hai how. see mid can be the ans then everything left to mid can have two type > <, than neighbour, if smaller then that will be peak, if greater like sorted on left bigger bigger then 0th has biggest then also 0th will be the peak acc to edge condition, same goes for right.
    #7,6,5,4 --- 7 is peak
    #7,8,5,4 --- any ele is maller then thats peak
    #proved isliye left ja rhe 