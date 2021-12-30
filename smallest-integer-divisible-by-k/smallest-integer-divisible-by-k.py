class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if not k & 1:   return -1       #if k is even,no chance of getting number with all 1s
        if k%5==0:  return -1
        
        num = 1
        n = 1
        while True:
            if num % k == 0:
                return n
            num = num*10+1
            n += 1
        return -1
        