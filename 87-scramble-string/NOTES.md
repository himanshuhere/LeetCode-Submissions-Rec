#MCM catch - lil tricky - really hard to approach
#Insteadof indices will pass string smaller string directly and k will be there for len of strings
#indices wud be complex, problem itself is complex lets stick to string passing for now
if len(s1) != len(s2):
return False
if sorted(s1) != sorted(s2):
return False
@lru_cache(None)
def mcm(s1, s2):
#if len(s1) != len(s2):  return False    #non necesarry
# if s1 == s2:      #less calls but more time as it will compare.
#     return True
if len(s1)==len(s2)==1:     #more branches but o(1) transaction
return s1==s2
if sorted(s1) != sorted(s2):
return False
n = len(s1)     #or s2 any length
for k in range(1, n):
swap = mcm(s1[:k], s2[-k:]) and mcm(s1[k:], s2[:-k])
noswap = mcm(s1[:k], s2[:k]) and mcm(s1[k:], s2[k:])
if swap or noswap:
return True
return False
return mcm(s1, s2)