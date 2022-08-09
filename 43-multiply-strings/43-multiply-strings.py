class Solution:
    def multiply(self, a: str, b: str) -> str:
        #return str(int(num1) * int(num2))
        #see copy notes
        if "0" in [a, b]:
            return "0"
        
        res = [0] * (len(a) + len(b))   #3*2 for 3, 3 lenght string and + 1 for carry so len(a)+len(b)
        a = a[::-1]
        b = b[::-1]
        
        for i1 in range(len(a)):
            for i2 in range(len(b)):
                
                mul = int(a[i1]) * int(b[i2])
                addition = res[i1 + i2] + mul
                
                res[i1 + i2] = addition % 10
                res[i1 + i2 + 1] += addition // 10         #carry
                
        res = res[::-1]     #reverse it and orignal ans
        beg = 0     #lets remove leading zero if any
        while beg < len(res) and res[beg] == 0:
            beg += 1
        
        res = map(str, res[beg:])
        return "".join(res)