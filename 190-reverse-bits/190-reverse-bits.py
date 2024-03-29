class Solution:
    def reverseBits(self, n: int) -> int:
        #1
        res = 0
        for i in range(32):
            if n>>i & 1:
                res |= 1<<(31-i)
        return res
            
        
#         #2
#         ans = 0
#         for _ in range(31):
#             if n&1 == 1:
#                 ans |= 1        #last bit on karni hai : ans = ans OR 1 / ans += 1
#                 #ans += 1
#             ans <<= 1
#             n >>= 1
        
#         ans += n&1 # add the last bit 
#         return ans