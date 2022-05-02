class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)-1
        while i < j:
            while i<j and nums[i] & 1 == 0:    #even
                i += 1
            while i<j and nums[j] & 1 == 1:  #odd
                j -= 1
            #still
            if nums[i] & 1 == 1:        #if i is odd
                nums[i], nums[j] = nums[j], nums[i]
                i+=1 
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j-=1 
        return nums