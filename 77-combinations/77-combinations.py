class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        temp = []
        
        def comb(temp, k, index):
            if k == 0:
                res.append(temp.copy())
                return
            
            for i in range(index, n+1): #i=index;i<=n
                temp.append(i)
                comb(temp, k-1, i+1)
                temp.pop()      #backtrack
                
        comb(temp, k, 1)
        return res
    
    #You may return the answer in any order.

    #but ans will be already sorted always
    
    #brute force plus backtrak = kn^k TC