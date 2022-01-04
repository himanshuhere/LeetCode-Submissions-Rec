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
    
        #mask = (1<<c)-1
        #return n XOR mask
#         so, like 8 has 1000 binary, do 8-1 = 7 u ll get 0111 bnary, 3 digit mask. We need mask to XOR with number then all bit will get flipped. Now mask you ll get by checking the MSB last left using while loop and then -1 and then 2^c-1 == 1<<c-1.
        