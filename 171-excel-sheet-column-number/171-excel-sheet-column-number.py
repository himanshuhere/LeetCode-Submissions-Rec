class Solution:
    def titleToNumber(self, col: str) -> int:
        res = 0
        for ch in col:
            res = res*26 + (ord(ch) - ord('A') + 1)
        return res
    
    
    
    # It is like converting a decimal number to base26 except there is no zero in that we need to subtract 1 from n to make that adjustment to get the answer we get from convert a normal decimal number to any base.
# Time: O(k) - k is the numer of digits in the input
# Space: O(1)