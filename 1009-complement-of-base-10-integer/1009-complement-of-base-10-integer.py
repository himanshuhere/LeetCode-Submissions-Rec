class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        num = n
        c = 0
        while num:
            num = num >> 1
            c += 1
        return n ^ (1 << c) -1 