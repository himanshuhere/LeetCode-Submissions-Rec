class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
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