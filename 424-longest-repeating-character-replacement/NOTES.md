#variable sliding window
m = defaultdict(int)
i, j = 0, 0
ans = 0
count = 0
while j < len(s):
m[s[j]] +=1
window = j-i+1
if window - max(m.values()) <= k:
ans = max(ans, j-i+1)
if window - max(m.values()) > k:
if s[i] in m:
m[s[i]] -=1
i += 1
j += 1
return ans
#window - max(m.values()), we want to long the string so we should look for replacing the least count chars in window, so that we can save more k for others, use k less and raise yuour widnow size thats y