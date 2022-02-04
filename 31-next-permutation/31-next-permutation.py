class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        #https://www.youtube.com/watch?v=LuLCLgMElus pls watch pls pls
        #creating all perm will lead n!
        #we ll find next perm using smart tricky intuition explained in above link
        
        ind1 = ind2 = len(nums)-1
        
        while ind1 > 0 and nums[ind1-1] >= nums[ind1]:
            ind1 -= 1
        
        if ind1 == 0:   # nums are in descending order, edge case
            nums.reverse()
            return 
    
        k = ind1 - 1    # find the last "ascending" position
        
        while nums[ind2] <= nums[k]:
            ind2 -= 1
            
        nums[k], nums[ind2] = nums[ind2], nums[k] #swap those twos/done with prefix part
        
        l, r = k+1, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1
            
            
#     def reverse(L, start, end):
#             while start < end:
#                 L[start], L[end] = L[end], L[start]
#                 start, end = start + 1, end - 1
        
#         i, n = len(nums) - 1, len(nums)
#         while i >= 1 and nums[i] <= nums[i-1]:
#             i -= 1
            
#         if i != 0:
#             j = i
#             while j + 1 < n and nums[j+1] > nums[i - 1]:
#                 j += 1
            
#             nums[i-1], nums[j] = nums[j], nums[i-1]
        
#         reverse(nums, i, n - 1)
        
#         return nums
