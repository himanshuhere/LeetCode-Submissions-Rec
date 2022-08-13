class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #simple the thing is here even/odd count of -ve numbers, if they are even take the all array (check for 0 ofc), and if odd -ves, then you have two option to remove, either first -ve or second -ve. Any middle you cant chose as it will break the array size and possibly in lesser answer. so see
        #if even -ve, one loop is enough as both will do same thing, if odd -ve, first one would take the max prod till last and also wothout last -ve, and second loop will come from back so it ll have one res without first neg, and if in between 0, so that too ll be covered in both direction. so boom
        
#         res = max(nums)     #imp step
#         p = 1
#         for i in range(len(nums)):
#             p *= nums[i]
#             res = max(res, p)
#             if nums[i] == 0:
#                 p = 1
                
#         p = 1
#         for i in range(len(nums)-1, -1, -1):
#             p *= nums[i]
#             res = max(res, p)
#             if nums[i] == 0:
#                 p = 1
        
#         return res
        
        
#         #1 basic subarray- template brute - TLE
#         if len(nums) == 1:
#             return nums[0]
        
#         ans = 0
#         for i in range(len(nums)):
#             cur = 1
#             for j in range(i, len(nums)):
#                 cur *= nums[j]
#                 ans = max(cur, ans)
#         return ans
        #2
        #ofc kadanes but issue with here it what kadane work for max sum subarray but here two negatives might end up being max pos product. So kadane will fail when negatives generating max product. we need to calculate man and min prod both at every index and update the max of both in final lil modificatio
        
        res = max(nums)
        curmax = curmin = 1
        
        for i in range(len(nums)):
            if nums[i] == 0:
                curmax = curmin = 1
            
            #bcz it will overrite in curmax, thus save it before to use in cur min
            tmp = nums[i]*curmax
            
            curmax = max(nums[i]*curmax, nums[i]*curmin, nums[i])
            curmin = min(tmp, nums[i]*curmin, nums[i])
            
            res = max(res, curmax)
        return res