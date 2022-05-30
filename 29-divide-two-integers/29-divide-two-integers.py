class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) == (divisor < 0)
        
        dividend, divisor = abs(dividend), abs(divisor)
        
        quot = 0
        while divisor <= dividend:
            val = divisor
            mult = 1
            while val + val <= dividend:
                val += val
                mult += mult
            dividend -= val
            quot += mult
            
        if not positive:
            quot = -quot
            
        return min(max(-2 ** 31, quot), 2 ** 31-1)