arr = stones
n = len(arr)
s=0
s=sum(arr)
dp=[[False for j in range(s+1)] for i in range(n+1)]
for i in range(n+1):
for j in range(s+1):
if i==0 and j==0:   dp[i][j]=True
elif j==0:          dp[i][j]=True
elif i==0:          dp[i][j]=False
for i in range(1,n+1):
for j in range(1,s+1):
if arr[i-1] <= j:
dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
else:
dp[i][j] = dp[i-1][j]
dif=sys.maxsize
for j in range(s//2,-1,-1):
if dp[n][j]==True:
dif=s-2*j
break;          #first closest value from centre wud be required s1 break
return dif