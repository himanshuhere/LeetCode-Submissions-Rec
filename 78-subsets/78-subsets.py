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
            
        ans = []
        sub(0, [])
        return ans