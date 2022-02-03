#3 sum is n^2, will do same
#as per constraint size will be min 3 so consider all them as res
res = A[0] + A[1] + A[2]
A= sorted(A)
for i in range(len(A)-2):
l, r = i+1, len(A)-1
while l < r:
cursum = A[i]+A[l]+A[r]
if cursum > target:
r-=1
else:
l+=1
if abs(res-target) > abs(cursum-target):
res = cursum
return res