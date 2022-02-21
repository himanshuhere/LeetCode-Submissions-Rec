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