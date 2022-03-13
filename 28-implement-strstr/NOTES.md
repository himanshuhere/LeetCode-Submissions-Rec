m = len(patt)
p = 13      #or any bigger
d = 26      #depends on data space, we have only small lettes cud cover in 26
​
powr=m-1
texth = 0
patth = 0
for i in range(m-1, -1, -1):
patth += ((ord(patt[i])*(d**powr))%p)      #cud have taken ord(ch)-ord('a') also
texth += ((ord(text[i])*(d**powr))%p)
powr-=1
for i in range(len(text)-m+1):
if patth == texth:
if text[i:i+m] == patt:
return i
else:
if i == len(text)-m:
return -1
texth -= ((ord(text[i])*(d**(m-1)))%p)
texth *= d          #base shift to left one
texth += ((ord(text[i+m])*(d**0))%p)
return -1