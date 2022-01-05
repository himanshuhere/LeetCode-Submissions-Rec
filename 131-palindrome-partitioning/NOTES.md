#check
def isPalind(i, j, s):
while i <= j:
if s[i] != s[j]:
return False
i += 1
j -= 1
return True
#Backtracking
def backtrack(i, tmp):
if i >= len(s):
res.append(tmp[:])
return
for j in range(i, len(s)):
if isPalind(i, j, s):
tmp.append(s[i:j+1])
backtrack(j+1, tmp)
tmp.pop()
res = []
tmp = []
backtrack(0, tmp)
return res