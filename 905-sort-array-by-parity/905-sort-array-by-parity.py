class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] & 1 == 0:    #even
                i += 1
            elif nums[j] & 1 == 1:  #odd
                j -= 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1 
                j-=1
        return nums