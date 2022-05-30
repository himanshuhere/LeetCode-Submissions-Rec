class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) == (divisor < 0)
        
        dividend, divisor = abs(dividend), abs(divisor)
        
        t = 0
        quot = 0
        for i in range(31, -1, -1): #31 to 0
            if t + (divisor << i) <= dividend:
                t += (divisor << i)
                quot = quot | 1 << i
                
        if not positive:
            quot = -quot
        return min(max(-2 ** 31, quot), 2 ** 31-1)