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
                i = i & ( i - 1 )       #off the last bit
                count += 1
            res += [count]
        return res
    
        #Index : 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

        #num : 0 1 1 2  1 2 2 3  1 2 2 3  2 3 3 4
        #dp[0]=0, dp[1]=dp[0]+1, d[2]=dp[0]+1, dp[3]=dp[2]+1...dp[4]=dp[0]+1, dp[8]=dp[0]+1
        #dp[i] = dp[i-offset]+1, offset will change inly when offset x 2 == i, then it will be same like 2, 4, 8, 16
        
        offset = 1
        dp = [0]*(n+1)
        for i in range(n+1):
            if offset * 2 == i:
                offset = offset * 2
            dp[i] = dp[i-offset] + 1
        return dp
        
        
        