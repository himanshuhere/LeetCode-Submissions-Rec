class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #CYCLIC SORT on small window. (which is in our hands)
        
        n = len(nums)
        i = 0 
        while i < n:
            j = nums[i] - 1
            #if (nums[i] > 0 and nums[i] <= n) and nums[i] != nums[j]:
            if (nums[i]-1 >= 0 and nums[i]-1 < n) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] - 1 != i:
                return i + 1
            
        return n + 1
    
        #This problem follows the Cyclic Sort pattern and shares similarities with Find the Missing Number with one big difference. In this problem, the numbers are not bound by any range so we can have any number in the input array.

#However, we will follow a similar approach though as discussed in Find the Missing Number to place the numbers on their correct indices and ignore all numbers that are out of the range of the array (i.e., all negative numbers and all numbers greater than or equal to the length of the array). Once we are done with the cyclic sort we will iterate the array and the first index that does not have the correct number will be the smallest missing positive number!

        #Okay how CYCLIC SORT, see quest wants smallest positive number right. we can skip all negatives, but but since data is not sorted we dont have all negatives on the left side right. Cool. but if we apply CYCLIC SORT(Lil modification), then we can atleast be confirm about the small window [start at smallest positive numbers to some extent] then after that out of bound +ve will start. Believe me if we find any thing wrong in our window that is SMALLEST POS missing, because window is starting from there only no, if not first after window is the ans. BELIEVE me it works.
        
        