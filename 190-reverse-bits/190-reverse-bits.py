class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for _ in range(31):
            if n&1 == 1:
                ans |= 1        #last bit on karni hai : ans = ans OR 1 / ans += 1
                #ans += 1
            ans <<= 1
            n >>= 1
        
        ans += n&1 # add the last bit 
        return ans