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
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        res = []		
		# Perform LIS
        for _, h in envelopes:
            l,r=0,len(res)-1
			
            # find the insertion point in the Sort order -BIN SEARCH
            while l <= r:
                mid=(l+r)>>1
                if res[mid]>=h:
                    r=mid-1
                else:
                    l=mid+1        
            idx = l
            # BIN SEARCH END
            
            if idx == len(res):
                res.append(h)
            else:
                res[idx] = h
                
        return len(res)
                
        
            
        