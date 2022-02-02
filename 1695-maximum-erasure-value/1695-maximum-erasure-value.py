class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        #variable sliding window
        m = defaultdict(int)
        ans = 0
        i, j = 0, 0
        count = 0
        subsum = 0
        while j < len(nums):
            m[nums[j]] += 1
            subsum += nums[j]
            if m[nums[j]] == 1:
                count += 1
                
            if count == (j-i+1):
                ans = max(ans, subsum)
                
            while count < (j-i+1):
                #ans = max(ans, subsum)
                if nums[i] in m:
                    m[nums[i]] -= 1
                    if m[nums[i]] == 0:
                        count -= 1
                subsum -= nums[i]
                
                i+=1
            j += 1
            
        return ans
                