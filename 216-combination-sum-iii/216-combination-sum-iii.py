class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        #A = [1,2,3,4,5,6,7,8,9]
        res = []
        tmp = []
        
        def backtrack(i, k, target, tmp):
            if k < 0 or target < 0:
                return
            
            if k == 0 and target == 0:
                res.append(tmp[:])
                return
            
            for num in range(i, 10):
                tmp.append(num)
                backtrack(num+1, k-1, target-num, tmp)
                tmp.pop()
        
        backtrack(1, k, n, tmp)
        return res