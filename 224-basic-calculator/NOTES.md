st = []
i = 0
​
s = "+" + s
res, val, lsign = 0, 0, ''        #lastSign or sign before cur val
while i < len(s):
if s[i].isdigit():
val = 0
while i < len(s) and s[i].isdigit():
val = val*10 + int(s[i])
i += 1
i -= 1
res += val if lsign == '+' else -val
elif s[i] == '+':
lsign = '+'
elif s[i] == '-':
lsign = '-'
elif s[i] == '(':
st.append(res)
st.append(lsign)
res = 0
lsign = '+'
elif s[i] == ')':
sign = st.pop()
lastres = st.pop()
res = (lastres+res) if sign == '+' else (lastres-res)
lsign = '+'
i += 1
return sum(st) if st else res