class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        #two pointer approach
        #even at 0. odd at 1. move two both aage
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if nums[i] & 1 == 0:    #even
                i += 2
            elif nums[j] & 1 == 1:  #odd
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i+=2
                j-=2
        return nums