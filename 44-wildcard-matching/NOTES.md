if len(p) - p.count('*') > len(s):
return False
m, n = len(s), len(p)
i = j = 0
star = match = None
​
while i < m:
if j < n and (p[j] == '?' or s[i] == p[j]):
i += 1
j += 1
​
elif j < n and p[j] == '*':
star = j
j += 1
match = i
​
elif star is not None:
j = star + 1
match += 1
i = match
​
else:
return False
​
while j<n and p[j] == '*':
j += 1
return j == n