class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # inplace
        pos = 0             # alone mastermind variable
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        
        #2
        count = 0
        for i in range(len(nums)):
            if nums[count] != 0:
                nums[count] = nums[i]
                count += 1
        
        while count < len(nums):
            nums[count] = 0
            count += 1
        
        
        
        
                
            
    