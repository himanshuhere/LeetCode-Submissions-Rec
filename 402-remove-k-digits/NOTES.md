st = []
for i in range(len(num)):
while k and (st and st[-1] > num[i]):
st.pop()
k -= 1
#for leading zero, leading can only be when stack is empty and zero comes
if not st and num[i] == "0":    continue
st.append(num[i])
#for case like 1234, 1111, nothing will pop and k will still be there, so remove last elements
while k and st:
st.pop()
k -= 1
if not st:
return "0"
return "".join(st)