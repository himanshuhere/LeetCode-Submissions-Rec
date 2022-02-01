class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #variable sliding window
        sm= 0
        i,j =0,0
        ans =math.inf
        while j< len(nums):
            sm+=nums[j]
            if sm < target:
                j+=1
            # elif sm>=target:
            else:
                while sm>=target:
                    ans = min(ans, j-i+1)
                    sm-=nums[i]
                    i+=1
                j+=1
            #j+=1
        return ans if ans!=math.inf else 0
    
    #can also b done usinf binary search on ans range = [1, len]
    #feasible will be finding max sum for k widnow-fixed sliding window