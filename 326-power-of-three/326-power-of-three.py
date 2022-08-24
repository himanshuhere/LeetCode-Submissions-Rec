class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #bit operation not possible 
        
        if n < 1: return False
        #bcs limit start from [1 .. n]
        
        #logn
        while n%3==0:
            n = n//3
        
        if n == 1:
            return True
        return False