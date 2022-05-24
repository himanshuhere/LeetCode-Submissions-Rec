class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #Same as Combination Sum - I, so lets first use counter to tackle the duplicacy issue leave it. Use sorting first, so all element same will be adjacent and we can skip them see
        
        A = candidates
        
        res = []
        tmp = []
        def backtrack(i, tmp, target):
            if target < 0:
                return
            if target == 0:
                res.append(sorted(tmp[:]))
                return
            
            for j in range(i, len(A)):
                if j > i and A[j] == A[j-1]:
                    continue
                
                tmp.append(A[j])
                backtrack(j+1, tmp, target-A[j])    #j+1 bcs Each number in candidates may only be used once in the combination.

#else j is there if 1 1 1 1 1 1 1 etc
                tmp.pop()
        
        A.sort()
        backtrack(0, tmp, target)
        return res