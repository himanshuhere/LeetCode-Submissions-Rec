class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #1 <= nums.length <= 200    4 sum constraint
        #1 <= nums.length <= 3000   3 sum constraint
        #1 <= nums.length <= 10^4    2 sum constraint
        
        nums.sort()
        N = len(nums)
        ans = []
        
        for i in range(N):
            if i > 0 and nums[i]==nums[i-1]: continue
                
            for j in range(i+1, N):
                if j > 0 and nums[j]==nums[j-1] and i!=j-1: continue
                l = j+1
                r = N-1
                
                while l < r:
                    s = nums[i]+nums[j]+nums[l]+nums[r]
                    
                    if s > target:
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        
                        while l<r and nums[l]==nums[l+1]: l+=1
                        while l<r and nums[r]==nums[r-1]: r-=1
                        
                        r -= 1
                        l += 1
        return ans