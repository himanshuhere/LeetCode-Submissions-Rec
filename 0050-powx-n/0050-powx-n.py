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
    
        
        
        
        #recursive
        def function(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return function(base * base, exponent // 2)
            else:
                return base * function(base * base, (exponent - 1) // 2)    #ek step aage, nhi karna to better ek base case sayd 1

        f = function()
        
        return float(f) if n >= 0 else 1/f
    
        