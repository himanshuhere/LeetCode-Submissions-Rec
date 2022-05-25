class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
                
        
#         env = sorted(envelopes, key = lambda x: (x[0], x[1]))
        
#         #Just LIS
#         @lru_cache(None)
#         def f(i, prevx, prevy):
#             if i == n:
#                 return 0
            
#             ans = -math.inf
#             if env[i][0] > prevx and env[i][1] > prevy:
#                 #print(i)
#                 ans = max(ans, 1+f(i+1, env[i][0], env[i][1]))
#             ans = max(f(i+1, prevx, prevy), ans)
#             return ans
        
        
        # return f(1, env[0][0], env[0][1])+1
        
        #NOTES PLS 
        
        #tab - LIS - TLE it needs nlogn binary search sol
        # env = sorted(envelopes)
        # n = len(env)
        # dp = [1]*n                   #ek russ doll to sabhi bana rhe
        # ans = 1
        # for i in range(n):
        #     for j in range(i-1, -1, -1):
        #         if env[j][0]<env[i][0] and env[j][1]<env[i][1]:
        #             dp[i] = max(dp[i], dp[j]+1)
        #             ans = max(ans, dp[i])
        # return ans     
        
        #nlog binary search and dp
        #YES LIS using BS is optimized incase of space time both, the data you l get will never be correct LIS seq but lenght in case of length you can always go for it and it is easy see
        
        #very easy n imp to understand
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        def lower_bound(a, key):
            l, r = 0, len(a)
            while l < r:
                mid = (l+r)//2
                if a[mid][1] >= key[1]:
                    r = mid
                else:
                    l = mid+1
            return l
        
        temp = []
        temp.append(envelopes[0])
        for i in range(1, len(envelopes)):
            if envelopes[i][0]>temp[-1][0] and envelopes[i][1]>temp[-1][1]:
                temp.append(envelopes[i])
            else:
                ind = lower_bound(temp, envelopes[i])
                temp[ind] = envelopes[i]
        return len(temp)
        