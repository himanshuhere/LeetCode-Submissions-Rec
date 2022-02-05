class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #variable sliding window
        i, j = 0, 0
        sm=0
        ans=0
        maxlen=math.inf
        while j < len(nums):
            sm+=nums[j]
            
            while sm >= target:
                maxlen=min(maxlen, j-i+1)
                sm-=nums[i]
                i+=1
            j+=1
        return maxlen if maxlen!=math.inf else 0
    
    #can also b done usinf binary search on ans range = [1, len]
    #feasible will be finding max sum for k widnow-fixed sliding window