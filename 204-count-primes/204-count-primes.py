class Solution:
    def countPrimes(self, n: int) -> int:       #seive of eratosthenes
        if n < 3 : return 0
        
        num = [1] * n
        num[0] = num[1] = 0
        
        for i in range(2, int(n ** 0.5)+1):     #n+ --> root(n) + 1
            if num[i]:
                for j in range(i*i, n, i):    #i jump
                    num[j] = 0
                    
        return sum(num)