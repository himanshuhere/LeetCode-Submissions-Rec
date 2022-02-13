class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        def sub(i, tmp):
            if i == n:
                ans.append(tmp[:])
                return
            #take
            tmp.append(nums[i])
            sub(i+1, tmp)
            tmp.pop()
            
            #not take
            sub(i+1, tmp)
            
#         def sub2(i, tmp):
#             if i == n:
#                 ans.append(tmp[:])
#                 return
#             for j in range(i, len(nums)):
#                 tmp.append(nums[j])
#                 sub2(j+1, tmp)
#                 tmp.pop()
            
        ans = []
        sub(0, [])
        return ans