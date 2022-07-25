class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #1 - O(n) with space
#         suff = [x for x in nums]
#         for i in range(len(suff)-2, -1, -1):
#             suff[i] = suff[i]*suff[i+1]
        
#         ans = [1]*len(nums)
#         pref = 1
#         suff.append(1)
#         for i in range(len(nums)):
#             ans[i] = pref*suff[i+1]
#             pref *= nums[i]
#         return ans
        
        #2 o(n) without space
        res = [1]*len(nums)
        pref = 1
        for i in range(len(nums)):
            res[i] = pref
            pref *= nums[i]
        
        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res
             
        pref = 1