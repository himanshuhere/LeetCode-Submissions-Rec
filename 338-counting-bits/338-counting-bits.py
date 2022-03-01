class Solution:
    def countBits(self, n: int) -> List[int]:
        #nlogn
        # ans = []
        # for i in range(0, n+1):
        #     ans += [(bin(i)[2:]).count("1")]
        # return ans
        
        
        res = []
        for i in range(n+1):
            
            #karninghan algo
            count = 0
            while i != 0:
                i = i & ( i - 1 )
                count += 1
            res += [count]
            
        return res
    
        ans = [0]
        m = [0, 1, 1, 2, 1, 2, 2, 3]    
        for i in range(1, n+1):
            ans += [m[i%8] + i//8 if i%8!=0 else 1]
        return ans
        
        
        
        