class Solution:
    def numberOfSteps(self, num: int) -> int:
        #brute
        # c = 0
        # while num:
        #     if num&1:
        #         num-=1
        #     else:
        #         num//=2
        #     c += 1
        # return c
    
        #bit
        if not num:
            return 0
        c = 0
        n=num
        while n:
            c += (1 if n&1==0 else 2)
            n >>= 1
        return c-1
    
        