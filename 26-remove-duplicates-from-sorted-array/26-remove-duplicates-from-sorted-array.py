class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 1
        j = 1
        while j < len(nums):
            if nums[i-1] != nums[j]:
                nums[i] = nums[j]
                i += 1
            j += 1
        
        return i
    
        #Remove Duplicates from Sorted Array I
        i = 0
        for num in nums:
            if i < 1 or num > nums[i-1]:
                nums[i] = num
                i += 1
        return i
        
        #80. Remove Duplicates from Sorted Array II
        i = 0
        for num in nums:
            if i < 2 or num > nums[i-2]:
                nums[i] = num
                i += 1
        return i