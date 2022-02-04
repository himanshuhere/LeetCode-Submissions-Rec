class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #pls see notes, it is kind of ques u need to know first to solve it in o(n) else o(n^2) of trying every subarray is there left
        #buy sell stock - I, kinda have intuition here pls see notes for images behind simple logic
        
        count = 0
        ans = 0
        hmap = {0:-1}
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            
            if count in hmap:
                ans = max(ans, i - hmap[count])
            else:
                hmap[count] = i
        return ans
        
        
#         looks like variable sliding window, but blv me 400 nearly test cases ran but not alll why, because you cant decide actually where to strech and where to shrink the window, yes some test cases will fail if you chose to do one of the things, so if you cant make decision on shrink/strech kaha ka sliding variable window hua leave
#         def variableSlidingWindow():
#             i, j = 0, 0
#             ones, zeroes = 0, 0
#             ans = 0
#             while j < len(nums):
#                 if nums[j] == 1:    
#                     ones += 1
#                 else:   
#                     zeroes += 1

#                 if ones == zeroes:
#                     ans = max(ans, j-i+1)
#                     # if nums[i] == 1:
#                     #         ones -=1
#                     # else:
#                     #     zeroes -= 1
#                     # i += 1
#                 j += 1
#             return ans

        
