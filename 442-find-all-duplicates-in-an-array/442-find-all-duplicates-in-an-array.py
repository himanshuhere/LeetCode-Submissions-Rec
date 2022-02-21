class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        #very easy just to know the trick and remember it as a pattern next time
        #last problem 287. Find the Duplicate Number has contraint that we cant modify array
        #this problem dsnt have any such issue so go on
        #we ll make visited index negative 
        ans = [] 
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0: 
                ans.append(abs(nums[i]) - 1 + 1)
            nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
        return ans
    
    #or dekh ke CYCLIC SORT yad aaya hoga lets do with that
        i = 0
        n = len(nums)
        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        ans= []
        for i in range(n):
            if nums[i] - 1 != i:
                ans.append(nums[i])
        return ans