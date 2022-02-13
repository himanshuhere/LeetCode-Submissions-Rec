class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        def sub(i, tmp, preChosen):
            if i == n:
                ans.append(tmp[:])
                return
            
            #no take
            sub(i+1, tmp, False)
            
            #take
            if i > 0 and not preChosen and nums[i] == nums[i-1]:  return 
            tmp.append(nums[i])
            sub(i+1, tmp, True)
            tmp.pop()
            
            
            
            
            
#         def sub2(i, tmp):
#             if i == n:
#                 ans.append(tmp[:])
#                 return
#             for j in range(i, len(nums)):
#                 tmp.append(nums[j])
#                 sub2(j+1, tmp)
#                 tmp.pop()
        
        nums.sort()
        ans = []
        sub(0, [], False)
        return ans