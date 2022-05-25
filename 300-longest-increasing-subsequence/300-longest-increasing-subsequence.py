class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        
#         #1
#         @lru_cache(None)
#         def f(idx, pre, ans = 0):
#             if idx == n:
#                 return ans
#             result = -math.inf
#             if pre == -1 or nums[pre] < nums[idx]:
#                 result = max(result, f(idx+1,idx,ans+1))
#             result = max(result, f(idx+1,pre,ans))
#             return result
        
#         return f(0, -1)
        
#           #2 - tabulation
#         dp = [[0]*(n+1) for _ in range(n+1)]
#         #base case handled
#         for i in range(n-1, 0, -1):
#             for j in range(i-1, -1, -1):        #prev can be from i-1 to -1
#                 l = dp[i+1][j+1]
#                 if j == -1 or nums[i] > nums[j]:
#                     l = max(l, 1+dp[i+1][i])
#                 dp[i][j] = l
#         return dp
    
#         #best tab - it is not intuitive you should know
#         #t - n^2 and s - n
        ans = [1]*n         #eveyone make 1 LIS
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    ans[i] = max(ans[i], 1+ans[j])
        return max(ans)
    
    
        #BS+DP - nlogn
        def lower_bound(a, key):
            l, r = 0, len(a)
            while l < r:
                m = (l+r)//2
                if a[m] >= key:
                    r = m
                else:
                    l = m+1
            return l
                    
        tmp = []
        tmp.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] > tmp[-1]:
                tmp.append(nums[i])
            else:
                ind = lower_bound(tmp, nums[i])
                tmp[ind] = nums[i]
        return len(tmp)