class Solution:
def findTargetSumWays(self, nums: List[int], target: int) -> int:
#bottom up
arr = nums
n = len(arr)
s = target - sum(arr) // 2
if (sum(arr) + target) % 2 == 1: return 0
if (sum(arr) - target) % 2 == 1 or target > sum(arr):
return 0
dp=[[0 for j in range(s+1)] for i in range(n+1)]
for i in range(n+1):
for j in range(s+1):
if i==0 and j==0:   dp[i][j] = 1
elif j==0:          dp[i][j] = 1
elif i==0:          dp[i][j] = 1
for i in range(1, n+1):
for j in range(1, s+1):
if arr[i-1] <= j:
dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
else: