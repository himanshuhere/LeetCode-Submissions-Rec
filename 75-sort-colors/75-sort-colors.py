class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    #see notes
    #1 - sort - nlog | 2 - count 0,1,2 and modify - n | 3 - dutch national flag - n three pointer
        
        i, j = 0, len(nums)-1
        mid = 0
        
        #beg to mid = 0, mid to end = 1, else after end = 2
        
        while mid <= j:
            if nums[mid] == 0:
                nums[mid], nums[i] = nums[i], nums[mid]
                i += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[j] = nums[j], nums[mid]
                j -= 1              #dont inc mid, might possible 2,2 hi swap huye let mid be there
            else:
                mid += 1
        