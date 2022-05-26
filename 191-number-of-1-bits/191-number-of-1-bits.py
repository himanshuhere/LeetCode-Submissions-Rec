class Solution:
    # def hammingWeight(self, n: int) -> int:
    #     cnt = 0        
    #     while(True):            #o(32/64)
    #         if n == 0: 
    #             break
    #         if n & 1 == 1: #check whether the last bit is 1
    #             cnt += 1
    #         n >>= 1
    #     return cnt
    
    #solution 2
    def hammingWeight(self, n: int) -> int:   
        cnt = 0        
        while(n != 0):          #0(count(1s))
            n = n & (n - 1)
            cnt += 1
        return cnt