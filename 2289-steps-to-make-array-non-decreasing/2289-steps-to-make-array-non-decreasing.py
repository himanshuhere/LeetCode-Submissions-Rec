class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        res,stack = 0, []
        for i in range(len(nums)-1,-1,-1):
            cur = 0
            while stack and nums[stack[-1][0]]<nums[i]:
                _,v = stack.pop()
                cur=max(cur+1,v)
            res = max(res,cur)
            stack.append([i,cur])
        return res
    
    
    #ulta traverse kyu, bcs you cant pop elemetns from stack if you proceed l to r, so in r to l. you can pop elements if s[-1] <num[i], and can count continous operation.
    #while popping you cant doing c+1, yes but lets say some elemtns comes which took more than c+1 steps we have to follow stick that chain right so take that instead