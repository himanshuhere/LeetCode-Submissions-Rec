class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = 0
        i = 1
        while x < num:      #mast math
            x+=i
            i+=2
        return x==num
    
        # 1*1 = 1       1 and 0 --> 1 = i , x = 0, i+2, x+i every iter
        # 2*2 = 4     -> 3 + 1
        # 3*3 = 9     -> 5 + 4
        # 4*4 = 16    -> 7 + 9
        # 5*5 = 25    -> 9 + 16
        # 6*6 = 36    -> 11 + 25
        # ...