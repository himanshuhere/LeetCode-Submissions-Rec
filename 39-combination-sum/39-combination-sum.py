class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #backtracking
        
        def bt(i, target, tmp):
            
            if target == 0:
                ans.append(tmp[:])
                return
            
            if i == len(candidates) or target < 0:
                return
            
            for j in range(i, len(candidates)):
                tmp.append(candidates[j])
                bt(j, target - candidates[j], tmp)
                tmp.pop()
        
        ans = []
        bt(0, target, [])
        return ans
    
    #The same number may be chosen from candidates an unlimited number of times. thus again bt(j)