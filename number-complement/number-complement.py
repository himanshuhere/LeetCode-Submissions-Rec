class Solution:
    def findComplement(self, num: int) -> int:
        ans = ''
        print(bin(num)[2:])
        for b in bin(num)[2:]:
            if b == '0':
                ans += '1'
            else:
                ans += '0'
        
        return int(ans, 2)