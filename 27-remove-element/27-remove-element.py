class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i
            
        
        
        
        
        
        
        j = len(nums)-1
        i = 0
        while i <= j:
            if nums[i] != val:
                i +=1
            elif nums[j] == val:
                j -= 1
            #elif nums[i] == val and nums[j] != val:
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1   
        return i