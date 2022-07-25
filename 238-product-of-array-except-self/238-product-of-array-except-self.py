class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suff = [x for x in nums]
        for i in range(len(suff)-2, -1, -1):
            suff[i] = suff[i]*suff[i+1]
        
        ans = [1]*len(nums)
        pref = 1
        suff.append(1)
        for i in range(len(nums)):
            ans[i] = pref*suff[i+1]
            pref *= nums[i]
        return ans