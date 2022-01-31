class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        count = 0
        ans = 0
        while j < len(nums):
            if nums[j] == 0:
                count += 1
            
            if count <= k:      #atmost
                ans = max(ans, j-i+1)
                j += 1
            elif count > k:
                while count > k:
                    if nums[i] == 0:
                        count -= 1
                    i += 1
                j += 1
                
        return ans