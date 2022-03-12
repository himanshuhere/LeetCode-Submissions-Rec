@lru_cache(None)
def dfs(i, j):
if j == -1:          #we got one ans
return 1
if i == -1:          #nothing we got nothing s hi paar ho gyi j k pehle
return 0
if s[i]==t[j]:
return dfs(i-1, j-1) + dfs(i-1, j)
else:
return dfs(i-1, j)
return dfs(len(s)-1, len(t)-1)
m, n = len(s), len(t)
dp = [[0] * (n+1) for _ in range(m+1)]
for i in range(m+1):
for j in range(n+1):
if j == 0:
dp[i][j] = 1
elif i == 0:
dp[i][j] = 0
elif s[i-1]==t[j-1]:
dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
else:
dp[i][j] = dp[i-1][j]
return dp[-1][-1]