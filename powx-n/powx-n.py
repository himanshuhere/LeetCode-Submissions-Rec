class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1                     #double
        power = n
        
        if power < 0: power = -1 * power     #make it positive for now
            
        while power > 0:
            if power % 2 == 0:
                x = x * x           # 4^8 = (4*4)^4 = 16^4
                power //= 2
            else:
                ans = ans * x       # 4^9 = 4 * (4^8)
                power = power - 1
                
        if n < 0: ans = 1 / ans #if power was neg
        return ans
    
        