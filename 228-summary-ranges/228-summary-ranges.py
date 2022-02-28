class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i=0
        ans=[]
        while i<len(nums):
            j=i
            while j<len(nums)-1 and nums[j]+1==nums[j+1]:
                j+=1
            if i!= j:
                ans.append(str(nums[i])+"->" + str(nums[j]))
            else:
                ans.append(str(nums[i]))
            i=j+1
        return ans
        