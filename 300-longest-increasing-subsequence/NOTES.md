class Solution:
def lengthOfLIS(self, nums: List[int]) -> int:
n = len(nums)
​
#1
@lru_cache(None)
def f(i, previ):
if i == n:
return 0
​
l = 0 + f(i+1, previ)       #not take
if previ == -1 or nums[i] > nums[previ]:
l = max(l, 1 + f(i+1, i))   #take
return l
​
return f(0, -1)
​
#2 - tabulation
dp = [[0]*(n+1) for _ in range(n+1)]
base case handled
for i in range(n-1, 0, -1):
for j in range(i-1, -1, -1):        #prev can be from i-1 to -1
l = dp[i+1][j+1]
if j == -1 or nums[i] > nums[j]:
l = max(l, 1+dp[i+1][i])
dp[i][j] = l
return dp
​
#         #best tab - it is not intuitive you should know
#         #t - n^2 and s - n
ans = [1]*n         #eveyone make 1 LIS
for i in range(n):
for j in range(i):
if nums[i] > nums[j]:
ans[i] = max(ans[i], 1+ans[j])
return max(ans)
​